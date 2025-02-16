# tasks/views.py
from django.http import JsonResponse
from .tasks import add_numbers

def trigger_task(request):
    """View to trigger our example task."""
    task = add_numbers.delay(4, 4)
    return JsonResponse({
        "message": "Task has been scheduled",
        "task_id": task.id
    })