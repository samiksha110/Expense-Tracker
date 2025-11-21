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

## Usage

1. Register a new user account or log in with existing credentials.
2. Navigate to the dashboard to view your financial summary, recent transactions, and goal progress.
3. Add new transactions (income or expense) using the transaction form.
4. Create financial goals to track your savings targets.
5. View and manage your transactions in the transaction list.

## Technologies Used

- **Backend**: Django 4.2.11
- **Database**: SQLite (default Django database)
- **Authentication**: Django Allauth
- **Frontend**: HTML, CSS, Bootstrap (in templates)
- **Other**: Python 3.x

## Project Structure

- `expensetracker/`: Main Django project settings
- `expense/`: Django app containing models, views, forms, and templates
- `templates/`: HTML templates for the web interface
- `static/`: Static files (CSS, JS, images)

## Future Enhancements

Based on the TODO list, planned features include:

- Responsive UI for mobile devices
- Enhanced data validation
- Search and filter functionality for transactions
- Charts and graphs for data visualization
- Unit tests for models and views
- API endpoints for mobile app integration
- Multi-language support
- Dark mode theme
- Backup and restore functionality
- User profile management
- Recurring transactions
- Advanced analytics and AI-powered insights

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
