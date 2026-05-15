# 🚀 SwiftLink | Modern URL Shortener

A minimalist, high-performance URL shortener built with **Django**. SwiftLink provides a clean interface to transform long, unwieldy URLs into concise, shareable links.

![UI Preview](https://img.shields.io/badge/UI-Minimalist-blue)
![Backend](https://img.shields.io/badge/Backend-Django-green)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey)

## ✨ Features

- **Instant Shortening**: Convert long URLs in one click.
- **Minimalist Design**: A centered, dark-mode UI focused on speed and simplicity.
- **Redirection**: Fast UUID-based redirection to your original destination.
- **Duplicate Detection**: Smart logic to reuse existing short links for the same long URL.
- **Mobile Responsive**: Works perfectly on desktops, tablets, and phones.

## 🛠️ Tech Stack

- **Framework**: Django 6.0+
- **Frontend**: HTML5, CSS3 (Modern Flexbox & Glassmorphism)
- **Database**: SQLite (Default)
- **Environment Management**: `uv`

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- `uv` (recommended) or `pip`

### Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sumant-shekhar/URL-Shortener-Project.git
   cd URL-Shortener-Project
   ```

2. **Set up the virtual environment**:
   Using `uv`:
   ```bash
   uv venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   uv pip install django
   ```

4. **Run Migrations**:
   ```bash
   cd shortner
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000` in your browser to start shortening!

## 📂 Project Structure

```text
URL-Shortener-Project/
├── shortner/               # Main Django project directory
│   ├── shortner/           # Project settings and root URLs
│   ├── urls/               # URL Shortener application logic
│   │   ├── models.py       # URL and UUID database schema
│   │   ├── views.py        # Creation and Redirection logic
│   │   └── urls.py         # App-level routing
│   └── templates/          # HTML Templates
│       └── index.html      # Main minimalist UI
├── .venv/                  # Virtual environment
└── README.md               # Project documentation
```

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---
Built with ❤️ by [Suman](https://github.com/sumant-shekhar)
