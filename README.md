## Project Overview
TaskFlow is a Django-based task management system that enables teams to create, track, and manage tasks efficiently. The application features a modern UI with dark/light theme support, comprehensive filtering, and intuitive task management.
## Live Demo
Deployed project: [https://task-manager-django-5qcs.onrender.com](https://task-manager-django-5qcs.onrender.com)

### Test Credentials
- Username: user
- Password: user12345


##Implemented Features

### Core Functionality
Full CRUD Operations - Create, Read, Update, Delete tasks
Task Assignment - Assign multiple workers to tasks
Priority System - Low, Medium, High, Urgent priority levels
Deadline Management - Track task due dates
Status Tracking - Mark tasks as In Progress or Completed
Advanced Filtering - Filter by Position, Task Type, and Priority
Dashboard Statistics - View total, completed, and in-progress task counts

### UI/UX Features
Dark/Light Theme Toggle - Persistent theme selection with localStorage
Modern Bootstrap 5 Design - Professional gradient styling
Fully Responsive - Works on desktop, tablet, and mobile

### Admin Features
**Django Admin Panel** - Full administrative interface for:
Task management
Task Type configuration
Worker administration
Position management

##Database Models

### Task Model
`name` - CharField (task title)
`description` - TextField (detailed description)
`task_type` - ForeignKey to TaskType
`priority` - CharField with choices (Low/Medium/High/Urgent)
`deadline` - DateField
`assignees` - ManyToManyField to Worker
`is_completed` - BooleanField
`created_at`, `updated_at` - Auto timestamp fields

### TaskType Model
`name` - CharField (Bug, New Feature, Design, Testing, Refactoring, Breaking Change, DevOps)

### Worker Model (from accounts app)
Extends Django AbstractUser
`position` - ForeignKey to Position

### Position Model (from accounts app)
`name` - CharField (Developer, Designer, DevOps, QA)

### Database Relationships
Task → TaskType (Many-to-One)
Task → Worker (Many-to-Many)
Worker → Position (Many-to-One)

## Technology Stack
Backend: Django 6.0.1
Frontend: Bootstrap 5.3.0, Bootstrap Icons 1.11.3
Database: SQLite3 (development)
Python: 3.13.6

## Project Structure
task_manager_django/
├── accounts/          # User authentication and Worker models
├── tasks/             # Task management app
│   ├── models.py      # Task and TaskType models
│   ├── views.py       # CRUD views
│   ├── forms.py       # Task forms with Bootstrap styling
│   ├── urls.py        # URL routing
│   └── templates/
│       ├── base.html  # Base template with dark/light theme
│       └── tasks/     # Task-specific templates
├── README.md          # Comprehensive project documentation
├── requirements.txt   # Project dependencies
└── manage.py


## Screenshots
### Dashboard
Overview with task statistics
Filter panel for Position, Task Type, Priority
Color-coded task cards
Quick access to all tasks

### Task List
Comprehensive table view
Status badges (In Progress, Completed)
Priority indicators
Quick action buttons

### Create/Edit Task Form
Gradient header design
Icon-labeled form fields
Date picker for deadlines
Multi-select for assignees
Mark as completed checkbox (edit only)

### Dark Mode
Complete dark theme implementation
Consistent styling across all components
Easy toggle in navbar

## Key Implementation Details
Class-Based Views: for CRUD operations (CreateView, UpdateView, DeleteView)
Function-Based Views: for dashboard and listing
Django Forms: with Bootstrap widget customization
Template Inheritance:for DRY code
CSS Custom Properties:for theme switching

##Setup Instructions
```bash
# Clone repository
git clone <repository-url>
cd task_manager_django

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

Author: Anastasiia Savchenko 
