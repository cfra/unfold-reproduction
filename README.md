# unfold-reproduction

This is a minimal repo to demonstrate an issue with django-unfold.

To set up and run, use:

```console
uv sync
uv run ./manage.py migrate
uv run ./manage.py createsuperuser
uv run ./manage.py runserver
```

Then navigate to <http://127.0.0.1:8000/admin/app/demomodel/add/>
