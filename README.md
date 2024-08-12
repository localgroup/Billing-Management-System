
# Mall Billing System

**Mall Billing System** is an application built using Django for the backend and incorporating HTML, CSS, and basic JavaScript for the frontend. It is designed to manage billing operations efficiently within a mall, providing a user-friendly interface for administrators and staff.

## Features

- **Customer Management**: Add, update, and view customer information.
- **Product Management**: Manage the inventory by adding, updating, and listing products.
- **Billing**: Generate and manage billing slips for customers.
- **Order Management**: Handle and manage orders placed by customers.
- **Responsive Design**: The application includes basic responsive design elements to ensure usability on different devices.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default, but can be switched to another database)
- **Version Control**: Git

## Setup and Installation

### Prerequisites

- **Python**: Version 3.10 or later
- **Django**: Install via pip
- **Git**: To clone the repository and manage version control

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd mall_billing_system
   ```

2. **Install dependencies**:
   ```bash
   pip install django
   ```

3. **Set up the database**:
   ```bash
   python manage.py migrate
   ```

4. **Run the development server**:
   ```bash
   python manage.py runserver
   ```
   Access the application at `http://127.0.0.1:8000/`.

5. **Create a superuser for admin access**:
   ```bash
   python manage.py createsuperuser
   ```
   Log in at `http://127.0.0.1:8000/admin/` with the credentials you set up.
