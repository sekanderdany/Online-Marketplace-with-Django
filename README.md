# Online Marketplace with Django

This is a basic Django project for building an online marketplace using Python and the Django web framework.

---

## 🚀 Project Setup Instructions

Follow the steps below to set up and run the project:

### 1. Clone the Repository
```bash
git clone https://github.com/sekanderdany/Online-Marketplace-with-Django.git
cd your-repo-name
```

### 2. Set Up Python Virtual Environment
```bash
python -m venv env
```

### 3. Activate Virtual Environment
- **Windows**
```bash
env\Scripts\activate
```
- **Mac/Linux**
```bash
source env/bin/activate
```

### 4. Install Django
```bash
pip install django
```

### 5. Upgrade pip (optional)
```bash
python -m pip install --upgrade pip
```

---

## 🛠️ Project Structure & Development

### 6. Start Django Project
```bash
django-admin startproject puddle
cd puddle
```

### 7. Run Development Server (Initial Check)
```bash
python manage.py runserver
```

### 8. Create the Core App
```bash
python manage.py startapp core
```

### 9. Set Up Templates Directory
Create the directory:
```
puddle/core/templates/core
```

- Your HTML templates should be stored here.
- The `index.html` will be located at:
```
puddle/core/templates/core/index.html
```

### 10. Configure URLs
Edit `puddle/core/urls.py` and wire them up in the `puddle/urls.py`.

---

## 🛍️ Add the Item App

### 11. Create Item App
```bash
python manage.py startapp item
```

### 12. Define Models
Edit `item/models.py` to define your database models.

### 13. Create Migrations
```bash
python manage.py makemigrations
```

### 14. Apply Migrations
```bash
python manage.py migrate
```

---

## ▶️ Final Run

Start the development server again to check your progress:
```bash
python manage.py runserver
```

---

## ✅ Notes

- Ensure all apps are added to `INSTALLED_APPS` in `settings.py`.
- Place your templates in the correct directory structure.
- Always run `makemigrations` and `migrate` after model changes.

---

## 📂 Directory Overview (Example)
```
puddle/
├── core/
│   ├── templates/
│   │   └── core/
│   │       └── index.html
├── item/
├── manage.py
```

---

## 📌 License
This project is for learning and demonstration purposes.

---

## 🙏 Special Thanks

This project was completed by following the tutorial by [Stein Ove Helset](https://github.com/SteinOveHelset) available on [freeCodeCamp.org](https://www.freecodecamp.org/) YouTube channel.

🎥 Watch the full tutorial here: [Build an Online Marketplace with Django](https://www.youtube.com/watch?v=ZxMB6Njs3ck)

Thanks to:
- **Stein Ove Helset** for the detailed walkthrough and project inspiration.
- **freeCodeCamp** for making high-quality, free content accessible to everyone.

