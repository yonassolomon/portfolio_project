from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            # Save to database
            contact_message = ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )
            
            # Send email notification
            try:
                subject = f'New Contact Form Message from {name}'
                email_message = f"""
New contact form submission:

Name: {name}
Email: {email}
Message:
{message}

Sent at: {contact_message.created_at}
"""
                send_mail(
                    subject=subject,
                    message=email_message,
                    from_email=settings.ADMIN_EMAIL,
                    recipient_list=[settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, 'Thank you for your message! I\'ll get back to you soon.')
            except Exception as e:
                # Log the error but still show success to user
                print(f"Email sending failed: {e}")
                messages.success(request, 'Thank you for your message! I\'ll get back to you soon.')
            
            return redirect('home')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    skills = [
        {'name': 'Java', 'icon': 'fab fa-java', 'level': 85},
        {'name': 'Django', 'icon': 'fab fa-python', 'level': 90},
        {'name': 'React', 'icon': 'fab fa-react', 'level': 80},
        {'name': 'Postman', 'icon': 'fas fa-tools', 'level': 85},
        {'name': 'HTML/CSS', 'icon': 'fab fa-html5', 'level': 88},
        {'name': 'JavaScript', 'icon': 'fab fa-js', 'level': 82},
    ]
    
    projects = [
        {
            'title': 'E-Commerce Platform',
            'description': 'A full-stack e-commerce platform built with Django and React',
            'tech_stack': ['Django', 'React', 'PostgreSQL', 'Redis'],
            'github_url': 'https://github.com/yourusername/ecommerce',
            'image': 'images/project1.jpg'
        },
        {
            'title': 'Task Management API',
            'description': 'RESTful API for task management with JWT authentication',
            'tech_stack': ['Django REST', 'JWT', 'PostgreSQL'],
            'github_url': 'https://github.com/yonassolomon/taskmanager-django.git',
            'image': 'images/project2.jpg'
        },
        {
            'title': 'Portfolio Website',
            'description': 'Modern responsive portfolio with Django and vanilla JS',
            'tech_stack': ['Django', 'JavaScript', 'CSS3'],
            'github_url': 'https://github.com/yonassolomon/portfolio',
            'image': 'images/project3.jpg'
        },
        {
            'title': 'Weather App',
            'description': 'Real-time weather application using OpenWeather API',
            'tech_stack': ['React', 'API Integration', 'CSS'],
            'github_url': 'https://github.com/yonassolomon/weather-app',
            'image': 'images/project4.jpg'
        },
        {
            'title': 'Blog Platform',
            'description': 'Feature-rich blog platform with markdown support and deployed on Railway 🔥',
            'tech_stack': ['Django', 'Markdown', 'Bootstrap'],
            'github_url': 'https://github.com/yonassolomon/django-blog.git',
            'image': 'images/project5.jpg'
        },
        {
            'title': 'Authentication System',
            'description': 'Custom authentication system with email verification',
            'tech_stack': ['Django', 'Celery', 'Redis'],
            'github_url': 'https://github.com/yonassolomon/auth-system',
            'image': 'images/project6.jpg'
        },
    ]
    
    context = {
        'name': 'YONAS SOLOMON', 
        'title': 'Software Engineering Student / Backend Developer',
        'tagline': 'Building scalable web applications with Django',
        'skills': skills,
        'projects': projects,
    }
    return render(request, 'portfolio/home.html', context)