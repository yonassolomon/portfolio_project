from django.shortcuts import render

def home(request):
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