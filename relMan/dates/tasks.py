from celery import shared_task


@shared_task(bind=True)
def test_func(self):
    for i in range(5):
        print(i)
    return "Done"
