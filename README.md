# task-manager-django
A Django-based task management application with dark mode support, advanced filtering, and Bootstrap templates.

###Core Functionality###

Full CRUD Operations - Create, Read, Update, Delete tasks
Task Assignment - Assign tasks to multiple team members
Priority Management - Set task priority (Low, Medium, High, Urgent)
Deadline Tracking - Set and monitor task deadlines
Task Filtering - Filter by position, task type, and priority
Status Management - Mark tasks as completed or in progress
Dashboard Statistics - View total, completed, and in-progress tasks

###UI/UX Features###

Dark/Light Theme - Toggle between themes with localStorage persistence
Design - Bootstrap 5 with custom gradient styling 
Responsive Layout - Works seamlessly on desktop and mobile
Bootstrap Icons - Beautiful iconography throughout


###Database Structure###
Models
Task

name - Task title
description - Detailed task description
task_type - Type of task (Bug, Feature, Testing, etc.)
priority - Task priority level
deadline - Due date
assignees - Team members assigned to the task
is_completed - Completion status
created_at, updated_at - Timestamps

TaskType
name - Name of the task type (Bug, New Feature, Design, etc.)
Worker (from accounts app)
Extends Django's AbstractUser
position - Job position/role
Position (from accounts app)
name - Position name (Developer, Designer, DevOps, etc.)

###Installation & Setup
Backend: Django 6.0.1
Frontend: Bootstrap 5.3.0, Bootstrap Icons 1.11.3
Database: SQLite (development), PostgreSQL-ready for production
Python: 3.13.6

Prerequisites
pip (Python package manager)
virtualenv (recommended)

###Installation Steps

#Clone the repository
git clone https://github.com/yourusername/task_manager_django.git
   cd task_manager_django

#Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

#Install dependencies
pip install -r requirements.txt

#Apply migrations
python manage.py migrate

#Create superuser
python manage.py createsuperuser

#Run development server
python manage.py runserver

#Access the application
Main app: http://127.0.0.1:8000/tasks/
Admin panel: http://127.0.0.1:8000/admin/

###Project Structure
task_manager_django/
├── manage.py
├── README.md
├── requirements.txt
├── task_manager_django/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/
│   ├── models.py      # Worker, Position models
│   
├── tasks/
│   ├── models.py      # Task, TaskType models
│   ├── views.py       # Task views
│   ├── forms.py       # Task forms
│   ├── urls.py        # URL routing
│   └── templates/
│       ├── base.html
│       └── tasks/
│           ├── home.html
│           ├── task_list.html
│           ├── task_detail.html
│           └── task_form.html
└── db.sqlite3 



Navigate to "Create Task" in the navbar
Fill in task details (name, description, type, priority, deadline)
Assign team members
Click "Create"

Filtering Tasks

Go to Dashboard
Use dropdown filters for Position, Task Type, or Priority
Click "Apply Filters"

Managing Tasks

View: Click on any task card to see details
Edit: Click "Edit Task" button on task detail page
Delete: Available through the detail page
Complete: Use the checkbox when editing a task

Admin Panel
Access the Django admin panel at /admin/ to manage:

Tasks
Task Types
Workers
Positions
User permissions

Future Enhancements

 Task comments and discussion threads
 File attachments for tasks
 Email notifications for deadlines
 Task history and audit log
 Kanban board view
 Time tracking
 Task dependencies
 Export tasks to CSV/PDF

Contributing

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request


This project is part of a portfolio project for educational purposes.
Author
Anastasiia Savchenko
GitHub: @nastasi

