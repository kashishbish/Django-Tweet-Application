# Django Tweet Application
A social media web application built with Django where users can create, edit, delete, and share tweets with text and photos. The application includes user authentication, profile management, and a secure tweet management system.

# Project Overview

This is a full-stack Django web application that demonstrates:
User authentication (registration, login, logout)
CRUD operations (Create, Read, Update, Delete tweets)
Database relationships and referential integrity
Template-based frontend with Bootstrap styling
Security features (CSRF protection, user authorization)
Image handling and file uploads

# Features:
User Management
User registration with email and password validation
Secure login and logout functionality
Session-based authentication
User profile association with tweets


# Tweet Management
Create new tweets with text (max 240 characters) and optional photo
View all tweets in chronological order (newest first)
Edit only your own tweets
Delete only your own tweets
Photo upload functionality with Pillow image processing

# User Interface
Responsive Bootstrap design
Dark mode support
Navigation bar with authentication status
Navbar shows different options for logged-in and logged-out users
Tweet form for creating and editing tweets
Tweet list view with all user tweets

Security Features:
CSRF token protection on all forms
User authorization (users can only edit/delete their own tweets)
Password hashing and validation
Django's built-in authentication system
Referential integrity with database CASCADE delete

## Technical Stack

# Backend
Python 3.x
Django 6.0
SQLite3 (database)


# Frontend
HTML5
Bootstrap 5.3.8
Django Templates (Jinja2 templating)


# Dependencies
asgiref==3.11.0
Django==6.0
pillow==12.0.0 (image processing)
sqlparse==0.5.5
tzdata==2025.3


# Tools
Git/GitHub (version control)
Python virtual environment

## Project Structure

Bishtheadq/                          # Main project folder
├── Bishtheadq/                      # Django project settings
│   ├── settings.py                 # Project configuration
│   ├── urls.py                     # Main URL routing
│   ├── wsgi.py                     # Server configuration
│   └── asgi.py
├── tweet/                           # Django app for tweet functionality
│   ├── migrations/                 # Database migrations
│   ├── templates/
│   │   ├── tweet_list.html        # Display all tweets
│   │   ├── tweet_form.html        # Create/edit tweet form
│   │   ├── tweet_confirm_delete.html
│   │   └── registration/
│   │       ├── login.html         # Login page
│   │       ├── register.html      # Registration page
│   │       └── logged_out.html    # Logout confirmation
│   ├── static/                     # CSS, JS, images
│   ├── media/                      # User uploaded photos
│   ├── admin.py                    # Django admin configuration
│   ├── apps.py                     # App configuration
│   ├── forms.py                    # Django forms (TweetForm, UserRegistrationForm)
│   ├── models.py                   # Database models (Tweet, User)
│   ├── urls.py                     # App URL patterns
│   ├── views.py                    # View functions
│   └── tests.py
├── templates/
│   ├── layout.html                 # Base template (navbar, footer)
│   └── index.html                  # Home page
├── static/                          # Project-level static files
├── media/                           # Project-level media files
├── manage.py                        # Django management utility
├── db.sqlite3                       # SQLite database (generated)
├── requirements.txt                 # Python dependencies
└── .env                            # Environment variables (not in git)

Database Models

Tweet Model

- user (ForeignKey to User) - Links tweet to user
- text (TextField) - Tweet content (max 240 characters)
- photo (ImageField) - Optional tweet image
- created_at (DateTimeField) - Auto-set creation timestamp
- updated_at (DateTimeField) - Auto-update modification timestamp

User Model
Uses Django's built-in User model
Fields: username, email, password, first_name, last_name, etc.

Installation & Setup
Prerequisites
Python 3.8 or higher
pip (Python package manager)
Git


Create virtual environment
bashpython -m venv venv
Activate virtual environment
bash# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
Install dependencies
bashpip install -r requirements.txt

Apply migrations
bashpython manage.py migrate

Create superuser (admin account)
bashpython manage.py createsuperuser
# Follow prompts to create admin credentials
Run development server
bashpython manage.py runserver

Access the application
Open browser and go to: http://127.0.0.1:8000/
Admin panel: http://127.0.0.1:8000/admin/


How to Use
As a New User
Go to home page
Click "Register" button
Fill in username, email, and password
Submit the form
You will be automatically logged in

# Creating a Tweet
Click "Tweet Home" in navbar
Click "Create Tweet" button
Enter tweet text (max 240 characters)
Optionally upload a photo
Click "Post" to publish


# Editing a Tweet
Go to your tweet
Click "Edit" button
Modify text or photo
Click "Update" to save changes


# Deleting a Tweet
Go to your tweet
Click "Delete" button
Confirm deletion
Tweet is permanently removed

# Viewing Tweets
Click "Tweet Home" in navbar
View all tweets from all users
Tweets are sorted by newest first
Click on user profile to see user's tweets

# URL Patterns

/ - Home page
/tweet/ - Tweet list view (all tweets)
/tweet/create/ - Create new tweet form
/tweet/<int:tweet_id>/edit/ - Edit tweet
/tweet/<int:tweet_id>/delete/ - Delete tweet
/accounts/login/ - Login page
/accounts/logout/ - Logout
/accounts/password_change/ - Change password
/tweet/register/ - User registration
/admin/ - Django admin panel

# Key Features Explained

Authentication System
Uses Django's built-in authentication backend
Passwords are hashed using PBKDF2 algorithm
Login required decorator on sensitive views
Session-based authentication


# Authorization System
Users can only edit their own tweets
Uses get_object_or_404 with user filter for security
CASCADE delete ensures orphaned tweets are removed if user is deleted


# Image Handling
Pillow library for image processing
Photos stored in media/photos/ directory
Images are optional (blank=True, null=True)
File type validation through Django


# Template Inheritance
base template (layout.html) with navbar and footer
Child templates extend layout.html
DRY principle (Don't Repeat Yourself) applied
Jinja2 templating engine



# Form Validation
Django forms auto-validate data
CSRF tokens prevent cross-site attacks
Password validation on registration
Email format validation


# Development Notes
Database Queries
The application uses Django ORM for all database operations:
Tweet.objects.all() - Get all tweets
Tweet.objects.filter(user=request.user) - Get user's tweets
Tweet.objects.order_by('-created_at') - Order by newest first


# Static Files
To collect static files for production:
bashpython manage.py collectstatic

# Creating Database Backups
bash# Export data to JSON
python manage.py dumpdata > backup.json

# Import data from JSON
python manage.py loaddata backup.json

Testing

Run tests with:

bashpython manage.py test tweet/

To run specific test:

bashpython manage.py test tweet.tests.TweetModelTest

Deployment

To deploy this application:


Set DEBUG = False in settings.py
Update ALLOWED_HOSTS with your domain
Use environment variables for SECRET_KEY
Configure a production database (PostgreSQL recommended)
Use Gunicorn as application server
Use Nginx as reverse proxy
Enable HTTPS/SSL certificate


Deploy to Render/Railway/Heroku

Refer to respective platform documentation for Django deployment.

Security Considerations


Never commit .env file with secrets
Always use CSRF tokens in forms
Validate all user input
Use HTTPS in production
Keep Django and dependencies updated
Use environment variables for sensitive data
Implement rate limiting for APIs
Regular security audits


# Future Enhancements
Add tweet likes and comments
Implement tweet retweets
User follow system
Tweet search functionality
Trending tweets
Direct messaging
Notifications system
Tweet hashtags
User profiles with bio
Tweet analytics


