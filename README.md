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

# 4. Configure environment variables
cp .env.example .env        # macOS / Linux
copy .env.example .env      # Windows
# Then edit .env and set DJANGO_SECRET_KEY to a freshly generated value:
python -c "import secrets; print(secrets.token_urlsafe(50))"

# 5. Apply migrations
python manage.py migrate

# 6. (optional) create an admin account
python manage.py createsuperuser

# 7. Build the Tailwind CSS
python manage.py tailwind build

# 8. Run the development server
python manage.py runserver
```

The application is then available at <http://127.0.0.1:8000>.

During development, `python manage.py tailwind start` recompiles the CSS automatically whenever templates change.

## Configuration

The app reads its configuration from environment variables (loaded from a local `.env`
file via `python-dotenv`). See [.env.example](.env.example) for the full list. `.env` is
gitignored and must never be committed — each environment (dev, staging, prod) keeps its
own copy.

| Variable | Purpose | Example |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | Django's cryptographic signing key (required, no default) | generated with `secrets.token_urlsafe(50)` |
| `DJANGO_DEBUG` | Enables Django's debug mode; must be `False` in production | `True` |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated list of hosts allowed to serve the app | `example.com,www.example.com` |

## Code quality

Formatting and linting are enforced with [Black](https://black.readthedocs.io/) and
[Flake8](https://flake8.pycqa.org/) (configured in `pyproject.toml` / `setup.cfg`).

```bash
pip install -r requirements-dev.txt
python -m black .
python -m flake8 .
```

## Project structure

| App | Role |
| --- | --- |
| `LITRevu_project/` | Django configuration (settings, root URLs) |
| `authentication/` | Registration and logout |
| `reviews/` | `Ticket`, `Review`, `UserFollows` models; feed, posts, create/edit/delete, follows |
| `home/` | Home page: login form and registration call-to-action for visitors, redirect to the feed for logged-in users |
| `theme/` | Tailwind CSS configuration, logo and base template (`base.html`) |
| `litrevu/` | Legacy app kept only for migration history (models moved to `reviews`) |
