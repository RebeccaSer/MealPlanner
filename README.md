🎉 MealPlanner – Mokone Meal Diaries 🥘


A Django-based Meal Planner and Recipe Organizer 📅🍽️

🚀 Project Overview


MealPlanner (“Mokone Meal Diaries”) is a modern, responsive web application built with Django that helps you:

    🗓️ Plan weekly meals in a user-friendly table

    📸 Browse recipes and meal details displayed as visual cards

    🛒 Generate grocery lists automatically based on your meal plan

    🔄 Review & edit your plan with a clear summary view


Designed for home cooks and food enthusiasts, MealPlanner streamlines your kitchen routine and brings joy back to meal planning. 😊🎉

✨ Key Features

    Weekly Meal Planner 📋: Input breakfast, lunch, dinner, and snacks for each day of the week via an intuitive table form.

    Plan Summary 🔍: View a read-only summary page of your entire week’s meals.

    Recipe Cards 🍝: Display recipes with images and descriptions in a responsive grid layout.

    Static Assets Management 🎨: Leverage Django’s static files system for CSS, images, and fonts (Pinyon Script for headings, Open Sans for body text).

    Dynamic Templates 🧩: Use Django’s template language for {% url %}, {% static %}, and loops to render content dynamically.

    Custom Styling 🌈: Clean, modern design with Google Fonts, CSS Grid, and Flexbox.

    Extensible Architecture 🏗️: Ready for database-backed models, formsets, and CRUD operations.

🛠️ Built With

    Python 3.12 🐍 & Django 5.2.3

    HTML5, CSS3 (Grid + Flexbox) 🎨

    Google Fonts: Pinyon Script, Open Sans 🖋️

    JavaScript (for dynamic interactions) ⚙️

    Git & GitHub for version control 🕹️

📂 Project Structure

MealPlanner/                # Django project root
├── MealPlanner/            # Project settings and URLs
├── meals/                  # Main app for meal planning
│   ├── static/meals/       # CSS, images, PDF assets
│   ├── templates/meals/    # HTML templates
│   ├── models.py           # (optional) future models
│   ├── views.py            # Views: plan, summary, recipes
│   ├── urls.py             # App-level URL routing
│   └── tests.py            # Automated tests for views
├── env/                    # Python virtual environment
├── manage.py               # Django CLI utility
├── requirements.txt        # Project dependencies
└── README.md 📖             # Project documentation (this file)

🔧 Installation & Setup

    Clone the repository:

git clone https://github.com/RebeccaSer/MealPlanner.git
cd MealPlanner


    Create & activate a virtual environment:

python3 -m venv env
source ~/env/bin/activate  # or your path


    Install dependencies:

pip install -r requirements.txt


    Apply database migrations (SQLite by default):

python manage.py migrate


    Run the development server:

python manage.py runserver

    Visit http://127.0.0.1:8000/plan/ to access the meal planner. 🍽️

🎯 Usage

    Plan your meals: 🍳 Fill out the table form for each day and submit.

    Review your plan: 📊 The summary page shows all entries in a read-only table.

    Explore recipes: 🍲 Navigate to recipe cards for inspiration.

    Extend functionality: ➕ Add new views, connect a database model for persistent storage, or integrate third-party APIs for nutrition data.


📄 License


This project is open-source and available under the MIT License. 📝

📞 Contact


Developer: Serepa Selaelo Rebecca

    GitHub: @RebeccaSer 🌐

    Email: serepasr06@gmail.com ✉️
