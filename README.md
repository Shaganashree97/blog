This is a simple Blog Application using Django Framework. It allows users to create, edit, delete and bookmark posts. It also allows users to comment on posts. The application has a simple authentication system that allows users to sign up, log in, and log out. The application also has an admin panel that allows the admin to manage users, posts, and comments.

Tech Stacks:
- Django
- HTML
- CSS
- Bootstrap

Functionalities: (in simple terms)
- User can create an account
- User can log in and log out
- User can create, edit, delete, and bookmark posts
- User can comment on posts
- Admin can manage users, posts, and comments

## Installation
1. Clone the repository:
```bash
git clone https://github.com/Shaganashree97/blog.git
cd blog
```
2. Create a virtual environment and activate it:
```bash
pip install virtualenv
virtualenv env
source env/bin/activate  # for Linux/MacOS
env\Scripts\activate.bat  # for Windows
```
3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file in the root directory of the project and add the following variables:
```bash
SECRET_KEY=secret
DEBUG=True
```
5. Run the migrations & migrate:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser account:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

8. Open your browser and go to http://localhost:8000/admin to access the admin panel. 
Log in with the superuser account you created earlier.