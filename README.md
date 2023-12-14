# django5test
Testing an old book project in django 5

# Steps
`mkdir pgdata_master`
`mkdir pgdata_slave`
`mkdir sqladmin_data`

`docker compose up`

`docker exec -it dj5test bash`
`django-admin startproject bookr`
`cd bookr`
`python manage.py runserver 0.0.0.0:8000`

`python manage.py startapp reviews`
`mkdir reviews/templates`

grant priviledges to sql_admin for the bookr database and all existing schemas and connect with sql

# Create a virtual environment for local IDE

# Be careful/purposeful with migrations
python manage.py showmigrations
python manage.py migrate --database=default

python manage.py makemigrations reviews
python manage.py migrate reviews --database=reviews
