from smtplib import SMTPException

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from config import settings
from django.core.mail import send_mail

from newsletter.models import NewsletterMessage, NewsletterSettings, NewsletterLog
from django.utils.timezone import now

scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)


def send_newsletter(newsletter: NewsletterSettings):
    """
    Отправка сообщения на почту
    :param newsletter: Модель настроек рассылки
    :return:
    """
    newsletter_message = NewsletterMessage.objects.get(newsletter_id=newsletter.id)
    clients = newsletter.client.all()
    for client in clients:
        try:
            send_mail(
                newsletter_message.title,
                newsletter_message.body,
                settings.EMAIL_HOST_USER,
                [client.email],
            )
            newsletter.last_sent_date = now()
            newsletter.status = 'LD'
            newsletter.save()
            NewsletterLog.objects.create_log(newsletter.status, newsletter, now(), '200')

        except SMTPException as error:
            NewsletterLog.objects.create_log('ошибка', newsletter, now(), error.args[0])


def check_task(newsletter: NewsletterSettings):
    """
    Проверяет статус активности рассылки и время начала
    :param newsletter: Модель настроек рассылки
    :return:
    """
    if newsletter.is_active:
        if newsletter.newsletter_time_from <= now():
            if now() <= newsletter.newsletter_time_to:
                return True
            else:
                newsletter.status = 'ED'
                newsletter.save()
                NewsletterLog.objects.create_log(newsletter.status, newsletter, now(), '')
                return False
        else:
            return False
    else:
        return False


def get_schedule(scheduler):
    """
    Добавление рассылки в очередь задач, если она не завершена.
    Постановка рассылки на паузу в очереди задач, если она не активна
    :param scheduler: Менеджер отправки
    """
    newsletters = NewsletterSettings.objects.all()
    if newsletters:
        for newsletter in newsletters:
            if not newsletter.status == 'ED':
                job_id = newsletter.id
                if check_task(newsletter):
                    create_task(scheduler, newsletter)
                else:
                    # Итоговое удаление рассылки
                    if scheduler.get_job(job_id):
                        scheduler.pause_job(job_id)
                        newsletter.status = 'приостановлена'
                        newsletter.save()
                        NewsletterLog.objects.create(now(), newsletter.status, '', newsletter)


def create_task(scheduler, newsletter: NewsletterSettings):
    """
    Создает задачу с заданной периодичностью настроек рассылки
    :param scheduler: Менеджер отправки
    :param newsletter: Модель настроек рассылки
    :return:
    """
    newsletter.task_id = newsletter.id
    newsletter.save()
    if newsletter.periodicity == 'OD':
        scheduler.add_job(
            send_newsletter,
            trigger=CronTrigger(second='*/10'),
            id=str(newsletter.id),
            max_instances=1,
            replace_existing=True,
            args=(newsletter,)
        )
    elif newsletter.periodicity == 'OW':
        scheduler.add_job(
            send_newsletter,
            trigger=CronTrigger(second='*/20'),
            id=str(newsletter.id),
            max_instances=1,
            replace_existing=True,
            args=(newsletter,)
        )
    elif newsletter.periodicity == 'OM':
        scheduler.add_job(
            send_newsletter,
            trigger=CronTrigger(second='*/30'),
            id=str(newsletter.id),
            max_instances=1,
            replace_existing=True,
            args=(newsletter,)
        )
