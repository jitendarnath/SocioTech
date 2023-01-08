# SocioTech
## A B2B web application built using Django with social login feature.

### Setup Instructions
1. Clone this repository either by downloading the ZIP or by using :

```bash
$ git clone https://github.com/jitendarnath/SocioTech.git
```
2. Open terminal from the SocioTech project directory and run the following to install the required dependencies.

```bash
$ pip install -r requirements.txt
```
3. Inorder to keep the database schema in sync with the Django models, Run:

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

4. Create an admin user : 

```bash
$ python manage.py createsuperuser
```

5. Start the server locally:

```bash
$ python manage.py runserver
```

Once the server is hosted, head over to http://127.0.0.1:8000/ to check the project working live.
