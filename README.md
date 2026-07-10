# LITRevu

Django web application for requesting and publishing book/article reviews between users who follow each other.

## Features

- Registration, login (form built into the home page) and logout
- Create a ticket (request a review for a book or article, with an optional image)
- Publish a review in response to an existing ticket
- Create a ticket and its review in a single action
- Edit and delete your own tickets and reviews (« Posts » page)
- Follow / unfollow other users
- Personalized feed: tickets and reviews from the user and the people they follow, sorted by date

## Tech stack

- Python 3.14, Django 6
- SQLite database (default)
- Tailwind CSS 4 via [django-tailwind](https://github.com/timonweb/django-tailwind) (standalone build, no Node required)

## Installation

```bash
# 1. Clone the repository and move into it
git clone <repo-url>
cd Dev-Django

# 2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS / Linux

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. (optional) create an admin account
python manage.py createsuperuser

# 6. Build the Tailwind CSS
python manage.py tailwind build

# 7. Run the development server
python manage.py runserver
```

The application is then available at <http://127.0.0.1:8000>.

During development, `python manage.py tailwind start` recompiles the CSS automatically whenever templates change.

## Project structure

| App | Role |
| --- | --- |
| `LITRevu_project/` | Django configuration (settings, root URLs) |
| `authentication/` | Registration and logout |
| `reviews/` | `Ticket`, `Review`, `UserFollows` models; feed, posts, create/edit/delete, follows |
| `home/` | Home page: login form and registration call-to-action for visitors, redirect to the feed for logged-in users |
| `theme/` | Tailwind CSS configuration, logo and base template (`base.html`) |
| `litrevu/` | Legacy app kept only for migration history (models moved to `reviews`) |
