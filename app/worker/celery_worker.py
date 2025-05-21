from celery import Celery
from app.worker.alarm_checker import check_alarms

celery_app = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1",
)

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60.0, check_alarms_task.s(), name="Her 1 dakikada alarm kontrol")

@celery_app.task
def check_alarms_task():
    loop = asyncio.get_event_loop()
    triggered = loop.run_until_complete(check_alarms())
    # Gelecekte burada e-posta/sms/telegram bildirimi veya frontend'e işaretleme yapılabilir.
    return triggered