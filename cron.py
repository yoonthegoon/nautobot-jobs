from celery.schedules import crontab


def crontra(cron: str):
    """
    Translates crontab syntax to celery crontab

    ↑↑↓↓←→←→ba+
    :return: crontab
    """

    try:
        minute, hour, day_of_month, month_of_year, day_of_week = cron.split(' ')
        return crontab(minute=minute, hour=hour, day_of_month=day_of_month, month_of_year=month_of_year,
                       day_of_week=day_of_week)
    except Exception as e:
        return e


if __name__ == '__main__':
    print(
        crontra(
            cron='*  * * * *'
        )
    )
