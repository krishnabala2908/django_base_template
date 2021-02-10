<<<<<<< HEAD
=======
# django_base_template
dajngo base template with logging and debug toolbar modules for dev environment
>>>>>>> e70c5fcceec696b149da7ebef423dcdf4eb2dde6
#Django startup Template

##this project contains one app bythe name `core` which contains custom command `rename`.

```python
python manage.py rename someprojectname
```

the above command will rename the default project name with current project name in `manage.py`,`wsgi.py`,`settings.py` files and changes the folder name `src` to `someprojectname`

#default settings file is divided into 3 parts:

1. base.py
2. dev.py
3. prod.py

if you are using this project for development then edit manage.py file to point to settings as
`someprojectname.settings.dev`

##.env file is also added for the configuration

#TODO:
1.write docker and docker compose files with nginx,gunicorn and postgresdb
