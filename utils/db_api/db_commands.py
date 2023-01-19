from asgiref.sync import sync_to_async

from admin_panel.telebot.models import Clients


@sync_to_async()
def create_client(telegram_id, username, name):
    Clients.objects.get_or_create(telegram_id=telegram_id, username=username, name=name)


@sync_to_async()
def get_client_telegram_id(telegram_id):
    return Clients.objects.filter(telegram_id=telegram_id).first()


@sync_to_async()
def get_all_clients():
    return Clients.objects.all()
