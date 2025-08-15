# Encrypted_Negative_Password
Use authentication by encrypted negative password.
# 🔐 Encrypted Negative Password Authentication

A Django-based authentication system implementing **Encrypted Negative Password (ENP)** for secure password storage.  
This method ensures that plaintext passwords are never stored and uses an innovative *negative password + encryption* approach to protect user credentials.

---

## 📌 Overview

The system follows these steps for password protection:

1. **Hashing** – User passwords are hashed using a cryptographic hash (e.g., SHA-256).
2. **Negation** – The hash is transformed into a *negative password* representation.
3. **Encryption** – The negative password is encrypted using a symmetric key cipher (AES).
4. **Storage** – The final encrypted value is stored in the database.

This method is resistant to **rainbow table** and **dictionary attacks**, even if the database is compromised.

---

## ✨ Features

- Plaintext passwords are **never** stored.
- Resistant to precomputation and brute-force attacks.
- No salt storage required — encryption adds randomness.
- Django web interface for signup/login.
- Modular Python implementation for encryption, hashing, and negation.

---

## 📂 Project Structure

```
Encrypted_Negative_Password/
├── App/                     # Django app containing authentication logic
│   ├── migrations/          # Database migrations
│   ├── static/              # Static assets (CSS/JS/images)
│   ├── templates/           # HTML templates (signup, signin, success pages)
│   ├── admin.py              # Django admin configuration
│   ├── aes.py                # AES encryption logic
│   ├── ereg.py               # Email/Regex validation
│   ├── gui.py                # GUI-related utilities
│   ├── hashneg.py            # Negative password hashing
│   ├── models.py             # Django models
│   ├── modulegui.py          # GUI module integration
│   ├── mytest_n.py           # Testing script
│   ├── tests.py              # Unit tests
│   └── views.py              # Request handling and authentication logic
│
├── EnNeDa/                   # Main Django project settings
│   ├── settings.py           # Django settings
│   ├── urls.py               # URL routing
│   └── wsgi.py               # WSGI entry point
│
├── db.sqlite3                # SQLite database (development)
├── manage.py                 # Django management script
└── README.md                 # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+**
- **Django** (version 2.x or 3.x)
- **cryptography** Python library

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### Running the Project

1. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

2. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

3. **Run the server**
   ```bash
   python manage.py runserver
   ```

4. Open your browser and visit:
   ```
   http://127.0.0.1:8000/
   ```

---

## 🔑 How It Works

1. **User Signup** → Password hashed → Negative password generated → AES encryption applied → Stored in DB.
2. **User Login** → Entered password undergoes the same process → Compared with stored ENP → If match, login successful.

---

## 🛡 Security Notes

- Use **strong encryption keys** and store them securely (do not commit them to the repo).
- Periodically review and update cryptographic algorithms.
- Use HTTPS in production.
- Implement login rate-limiting to prevent brute-force attacks.

---

## 📄 License

This project is licensed under the MIT License.

