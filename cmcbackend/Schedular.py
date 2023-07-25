from apscheduler.schedulers.background import BackgroundScheduler
from .views import update_coins_data, update_currency_data

schedular = BackgroundScheduler()

schedular.add_job(
    update_coins_data, "interval", seconds=10000000000
)  # Update data every 60 second

schedular.add_job(update_currency_data, "interval", seconds=1000000000)
