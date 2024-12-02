from django.core.management import call_command
from django.db import connection

def load_data_if_needed():
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM your_app_name_yourmodelname;")
        if cursor.fetchone()[0] == 0:  # Replace with a check for your use case
            call_command("loaddata", "data.json")
