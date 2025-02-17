from django.core.management.base import BaseCommand
from celery.backends.database.session import ResultModelBase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from django.conf import settings
import os

class Command(BaseCommand):
    help = "Create necessary Celery tables in PostgreSQL"

    def handle(self, *args, **kwargs):
        engine = create_engine(os.getenv('CREATE_ENGINE'))
        Session = sessionmaker(bind=engine)
        session = Session()
        ResultModelBase.metadata.create_all(engine)
        session.commit()
        session.close()
        self.stdout.write(self.style.SUCCESS("Successfully created Celery tables in PostgreSQL"))
