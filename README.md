
---

# FindMe Mini Auth App

## Setup

1. Clone repo:

```bash
git clone git@github.com:drec0xy/findme.git
cd findme
```
2. Add the env variables to the ```.env``` file on the root of the repository
```bash
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
```
3. Start the database using docker compose:

```bash
docker-compose up --build
```
4. Install python packages
create and activate a virtual environment and run 
```bash
pip install -r requirements.txt
```

5. Run Migrations 
From the root of the repository, run migration by executing the following command

```bash
python manage.py migrate
```
6. Access app at by runnung 

```bash
python manage.py runserver
```
the app should be accesible here
 [http://localhost:8000](http://localhost:8000)

## Usage

* Signup at `/signup/`
* Login at `/login/`
* Logout at `/logout/`
* Home at `/`

## Run tests

```bash
python manage.py test user_auth.test_cases
```

---

