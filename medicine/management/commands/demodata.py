from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from medicine.models import Doctor

class Command(BaseCommand):
    help = 'Created user with full permissions and append example doctors'

    def handle(self, *args, **options):
        if User.objects.filter(username='admin').count() > 0:
            self.stdout.write('User admin exists')
        else:
            user = User(username='admin', email="admin@admin.ru")
            user.set_password('admin')
            user.is_superuser = True
            user.is_staff = True
            user.save()

            self.stdout.write('Super user with name "admin" created')

            doctors_name = ['Kostya (surgeon)',
                            'Victor (dentist)',
                            'Nikita (neurologist)',
                            'Anya (psychologist)',
                            'Dasha (ophthalmologist)']

            for name in doctors_name:
                doctor = Doctor(name=name)
                doctor.save()

            self.stdout.write('Added simple doctors')