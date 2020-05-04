python3 manage.py makemigrations

python3 manage.py migrate

echo "from django.contrib.auth import get_user_model: User = get_user_model(); User.objects.create_superuser(username='admin3', email='admin@wku.edu', passward='bigred2020')" | python3 manage.py shell

echo "from django.contrib.auth.models import Group; Group.objects.create(name='teachers'); Group.objects.create(name='students')" | python3 manage.py
