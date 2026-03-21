# Email Configuration Guide

## Development (Current Setup)
The project is currently configured to print emails to the console using:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

## Production Setup (Gmail SMTP)

To send real emails, update `settings.py`:

```python
# Replace the console backend with SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

### Gmail Setup Steps:

1. **Enable 2-Factor Authentication** on your Gmail account
2. **Generate App Password**:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate password for "Mail"
   - Use this 16-character password (not your regular password)

3. **Update settings.py** with your email and app password

### Alternative Email Providers:

**SendGrid**:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = 'your-sendgrid-api-key'
```

**Mailgun**:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-mailgun-smtp-username'
EMAIL_HOST_PASSWORD = 'your-mailgun-smtp-password'
```

## Testing Email

Run the test command:
```bash
python manage.py test_email
```

This will send a test email using your configured backend.

## Contact Form Email Format

When someone submits the contact form, you'll receive an email with:
- Subject: "New Contact Form Message from [Name]"
- Body contains: Name, Email, Message, and timestamp

## Troubleshooting

- **Emails not sending**: Check EMAIL_HOST_PASSWORD and EMAIL_HOST_USER
- **Gmail blocking**: Make sure you're using an App Password, not your regular password
- **Port issues**: Try port 465 with EMAIL_USE_SSL = True instead of TLS
- **SPF/DKIM**: For production, set up proper email authentication