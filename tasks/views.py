# # tasks/views.py
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django.utils.timezone import now
from dateutil.relativedelta import relativedelta
from django.http import JsonResponse
from .models import PhoneNumber
from .tasks import charge_user

def purchase_phone_number(request):
    user = "NaidrAli2"  # Assume authenticated user
    phone = PhoneNumber.objects.create(user=user, phone_number='1234567893130')

    # Create or get an interval schedule for 1 minute
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=1,  # Every 1 minute
        period=IntervalSchedule.MINUTES  # In minutes
    )

    # Create a periodic task to run every minute
    PeriodicTask.objects.create(
        interval=schedule,
        name=f'Charge user for phone {phone.phone_number}',
        task='tasks.tasks.charge_user',
        kwargs=f'{{"phone_number_id": {phone.id}}}', 
    )

    return JsonResponse({'message': 'Phone number purchased and periodic billing scheduled'})
