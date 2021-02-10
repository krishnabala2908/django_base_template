from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = "Renames a django Project"

    def add_arguments(self, parser):
        parser.add_argument("new_project_name", type=str, help="new project name")
        # parser.add_argument('-p','--prefix')

    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']

        files_to_rename = ['src/settings/base.py', 'src/wsgi.py', 'manage.py']
        folder_to_rename = 'src'

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace('src', new_project_name)

            with open(f, 'w') as file:
                file.write(filedata)

        os.rename(folder_to_rename, new_project_name)
        self.stdout.write(self.style.SUCCESS("project renamed as %s", new_project_name))
