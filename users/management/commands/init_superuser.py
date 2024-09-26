from django.conf import settings
from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        email = "admin@gmail.com"
        password = settings.SUPER_ADMIN_PASS

        if User.objects.filter(email__iexact=email).exists():
            u = User.objects.get(email=email)
            u.name = "SuperAdmin"
            u.set_password(password)
            u.is_superuser = True
            u.is_staff = True
            u.is_active = True
            u.save()
            self.stdout.write(
                "The admin account has already existed. Password will be reset."
            )
        else:
            User.objects.create_superuser(email, password)
            self.stdout.write("The admin account has been created.")
