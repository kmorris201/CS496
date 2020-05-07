# This shell script does four things: formats the database, creates the 
# default admin user, creates the teachers and students group, and allows
# for writing to the various media directories

python3 manage.py makemigrations

python3 manage.py migrate

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@wku.edu', 'bigred2020')" | python3 manage.py shell

echo "from django.contrib.auth.models import Group; Group.objects.create(name='teachers'); Group.objects.create(name='students')" | python3 manage.py shell

chmod ugo=rwx /wku_sims/static/media/*
