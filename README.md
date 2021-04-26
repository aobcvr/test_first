# Test for Python Junior Developer

[Documentation](https://github.com/mazer9/test_first/blob/master/docs/test_first.md)

Requirements:

- [Docker >= 20.10.3](https://docs.docker.com/engine/install/)
- [Docker Compose >= 1.28.2](https://docs.docker.com/compose/install/)

### Installation

#### 1. Download or clone (`git clone https://github.com/mazer9/test_first`) the repository

#### 2. Change directory

```cd test_first```

#### 3. Create local environment files

- .envs/.local/db.env

```env
DATABASE_URL=psql://dev_user:dev_password@postrgesql:5432/test_first
```

- .envs/.local/django.env

```env
DJANGO_DEBUG=True
DJANGO_SETTINGS_MODULE=config.settings.local
DJANGO_SECRET_KEY=!!!SET DJANGO_SECRET_KEY!!!
DJANGO_ADMINS=Full Name <email-with-name@example.com>,anotheremailwithoutname@example.com
DJANGO_STAFF=Full Name <email-with-name@example.com>,anotheremailwithoutname@example.com
DJANGO_ALLOWED_HOSTS=0.0.0.0,127.0.0.1,localhost
```

#### 4. Start the containers

```docker-compose -f docker-compose-dev.yml up -d```

#### 5. Visit http://127.0.0.1:8000
