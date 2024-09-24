# My Field App

## Technologies
- Python
- Django
- Java Script
- JSON
- HTML
- CSS

## Installation

To use the project you need to clone it from Github.
You need to have Python and Django installed on your computer.

Install all required dependencies using the requirements.txt file:
```bash
pip install -r requirements.txt
```

To configure the environment settings, create an .env file in the project root directory and add the following entry:
```text
  DJANGO_SECRET_KEY=your_secret_key_here
```

To generate a SECRET_KEY, you can use the following command in Python:
```python
  from django.core.management.utils import get_random_secret_key
  print(get_random_secret_key())
```
Copy the generated key and paste it into the .env file.

To start the local development server, use the following command:
```bash
  python manage.py runserver
```

The server will run on the default port 8000, so you can access the application in your browser at the address:
http://127.0.0.1:8000


## Screenshots
<img src="screenshot.png" alt=""/>
