from celery.schedules import crontab


def crontra(cron: str):
    """
    Translates crontab syntax to celery crontab

    Supports following symbols:

    • Asterisk (*) - signifies all possible values
    • Comma (,) - lists multiple values
    • Hyphen (-) - determine a range of values
    • Slash (/) - divide a value ({* */12 * * *} runs every 12 hours)

    No support for Last (L), Weekday (W), Number symbol (#), Question mark (?), and special @ strings.

    ↑↑↓↓←→←→ba+

    :return: crontab
    """

    try:
        minute, hour, day_of_month, month_of_year, day_of_week = cron.split(' ')
        return crontab(minute=minute, hour=hour, day_of_month=day_of_month, month_of_year=month_of_year,
                       day_of_week=day_of_week)
    except Exception as e:
        return e
