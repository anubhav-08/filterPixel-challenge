
# Filter Pixel - Classification of Images

An end to end web app, where we fetched images from AWS S3 Bucket and Google Drive then displayed them seprately using Angular Application.

**For Frontend** - Please refer this [repository](https://github.com/anubhav-08/FilterPixel-Frontend)


## Tech Stack

**Client:** Angular version 15.1.1

**Server:** Django, Django Rest Framework, Python version 3.9.6


## Installation Backend 

Create a virtual environment and run.

```bash
pip install virtualenv
python -m virtualenv venv
venv\Scripts\activate
```

Install Project dependencies

```bash
pip install -r requirements.txt
```

Create Database migrations and migrate them
```bash
python manage.py makemigrations
python manage.py migrate
```
Run the Development Server

```bash
python manage.py runserver
```

## Installation Frontend 

Install dependencies by following command in frontend directory

```bash
npm i
```

Run Development Server
```bash
ng serve
```
## Configurations
Generate Oauth client id from Google API Console and Enable the google drive api as well.
Keep the credentials in base directory of backend as **credentials.json**

Perform backend related tasks in **base directory** and Frontend related tasks in **Frontend directory**.