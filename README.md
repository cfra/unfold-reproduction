# unfold-reproduction

This is a minimal repo to demonstrate an issue with django-unfold.

To set up and run, use:

```console
uv sync
uv run ./manage.py migrate
```

Migration fails because of a check introduced in commit:

```
commit f728bd6b89950b7fa64fcb1580137de9602ec260
Author: Lukas Vinclav <lukasvinclav@gmail.com>
Date:   Tue May 20 14:57:03 2025 +0200

    feat: allow django permissions in actions (#1230)
```

The check is run before migrations are run - it cannot expected the permissions
table to exist when we run migrate for the very first time.

In our deployements we also run the following prior to running migrate, for this
I also belive the check to be problematic if database has not been initialized yet:

```
./manage.py check --deploy --fail-level WARNING
```
