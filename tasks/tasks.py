# tasks/tasks.py
from celery import shared_task
import time

@shared_task
def add_numbers(x, y):
    print("shared_task", shared_task)
    """A simple task that adds two numbers with a delay to simulate processing."""
    time.sleep(5)  # Simulate time-consuming work
    return x + y