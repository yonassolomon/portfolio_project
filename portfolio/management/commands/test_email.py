from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings

class Command(BaseCommand):
    help = 'Test email sending functionality'

    def handle(self, *args, **options):
        try:
            send_mail(
                subject='Test Email from Portfolio',
                message='This is a test email to verify email configuration is working.',
                from_email=settings.ADMIN_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=False,
            )
            self.stdout.write(
                self.style.SUCCESS('Email sent successfully! Check your console output.')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Email sending failed: {e}')
            )