# Expense Tracker

A Django-based web application for tracking personal expenses and financial goals.

## Features

- User registration and authentication using Django Allauth
- Dashboard with financial overview including total income, expenses, net savings, and goal progress
- Transaction management: Add income or expense transactions with categories
- Goal tracking: Set financial goals with target amounts and deadlines, view progress
- Transaction listing and management
- Responsive web interface

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd Expense-Tracker
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Apply database migrations:
   ```
   python manage.py migrate
   ```

4. (Optional) Create a superuser for admin access:
   ```
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

Visit `http://localhost:8000` in your browser to access the application.

