# tasks/tasks.py
import logging
from celery import shared_task
from django.utils.timezone import now
from dateutil.relativedelta import relativedelta
from .models import PhoneNumber

logger = logging.getLogger(__name__)

@shared_task(bind=True)
def charge_user(self, phone_number_id):
    logger.info(f'Task ID: {self.request.id} - Starting charge_user for phone_number_id: {phone_number_id}')
    try:
        phone = PhoneNumber.objects.get(id=phone_number_id)
        logger.info(f'Processing charge for phone number: {phone.phone_number}')
        
        # Update next billing date to be 1 minute later
        phone.next_billing_date = now() + relativedelta(minutes=1)
        phone.save()
        logger.info(f'Successfully updated billing date for phone: {phone.phone_number}')
        
    except PhoneNumber.DoesNotExist:
        logger.error(f'Phone number with id {phone_number_id} not found')
    except Exception as e:
        logger.error(f'Unexpected error in charge_user: {str(e)}')
        raise