import random
from datetime import timedelta, datetime
from random import randint

from django.core.management import BaseCommand
from django_seed import Seed
from faker import Faker
from plogging.models import PloggingLog


class Command(BaseCommand):

    def add_arguments(self, parser):
        help = '이 커맨드를 통해 랜덤한 데이터 생성'
        parser.add_argument(
            "--total",
            default=2,
            type=int,
            help='몇 개의 로그 데이터를 만드냐',
        )

    def handle(self, *args, **options):
        total = options.get("total")
        seeder = Seed.seeder()

        temp_date = datetime.now() - timedelta(days=random.randint(0, 3), minutes=random.randint(0, 300))
        seeder.add_entity(
            PloggingLog,
            total,
            {
                "userid": lambda x: randint(0, 50),
                "distance": lambda x: randint(30, 1000),
                "starttime": lambda x: temp_date,
                "endtime": lambda x:  temp_date + timedelta(minutes=random.randint(0, 120)),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{total}명의 유저가 작성되었습니다."))
