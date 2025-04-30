# Backend
## Preparation
1. Run the following command to create table to database and to enable changes.

    ```bash
    # In the host environment
    docker-compose run --rm django bash
    # In the container envrionment
    python manage.py makemigrations
    python manage.py migrate
    ```

1. Execute the following command to create superuser.

    ```bash
    # In the docker environment
    echo 'from django.contrib.auth.models import User; User.objects.create_superuser("'${DJANGO_SUPERUSER_NAME}'", "'${DJANGO_SUPERUSER_EMAIL}'", "'${DJANGO_SUPERUSER_PASSWORD}'")' | python manage.py shell
    ```

1. Type the following command to come back to the host environment.

    ```bash
    exit # or press Ctrl + D
    ```