Overview

The Smart Task Analyzer (STA) is a productivity tool designed to help users prioritize their tasks dynamically based on key metrics: Importance, Effort, and Urgency (derived from the Due Date).

 1. Setup Instructions

This guide assumes you have Python 3.10+ and Git installed on your system.

1.1. Clone the Repository

git clone [https://github.com/Jagritisinghh/task-analyzer.git](https://github.com/Jagritisinghh/task-analyzer.git)
cd task-analyzer


1.2. Create and Activate Virtual Environment

It is critical to isolate project dependencies using a virtual environment.

# Create the environment
python -m venv venv

# Activate the environment (Linux/macOS)
source venv/bin/activate

# Activate the environment (Windows)
venv\Scripts\activate


1.3. Install Dependencies

Install all required Python packages (Django, etc.) using the requirements.txt file.

pip install -r requirements.txt


1.4. Database Setup

The project uses a local SQLite database (db.sqlite3) for development.

Run Migrations: Apply the necessary database schema changes.

python manage.py makemigrations
python manage.py migrate


Create Superuser (Optional): If you need access to the Django Admin interface.

python manage.py createsuperuser


1.5. Run the Application

Start the Django development server:

python manage.py runserver


The application will be accessible in your web browser at: http://127.0.0.1:8000/

⭐ 5. Future Improvements

With more time, the following features would significantly enhance the application:

User Authentication: Implement Firebase Authentication (or Django Auth) to provide secure, private task lists for each user.

User-Tunable Weights: Allow users to adjust the weights ($\text{W}_I, \text{W}_E, \text{W}_U$) in the settings, enabling them to customize the priority formula to match their personal work style (e.g., heavily favor low-effort tasks).

Visualization: Add a small bar chart or radar chart visualization to show how the Importance, Effort, and Urgency scores combine to form the final priority, increasing user trust and understanding of the sorting mechanism.

Task Completion History: Track task completion data to provide weekly/monthly reports on productivity trends.