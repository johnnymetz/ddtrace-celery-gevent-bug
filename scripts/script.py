from core.tasks import debug_task


debug_task.delay()


def run():
    print("Done")
