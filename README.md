# SousPoker

## Setup
1. Install Docker
1. Add a `.env` file in the root with the following keys:
    ``` 
    DATABASE_NAME 
    DATABASE_USER 
    DATABASE_PASS
    ```
1. Add a `.env` file in `src/sous_poker`
    ```
    DJANGO_SECRET_KEY
    DEBUG
    DATABASE_NAME
    DATABASE_USER
    DATABASE_PASS
    DATABASE_HOST
    DJANGO_SETTINGS_MODULE
    ```
1. From root run `docker-compose up --build`
1. third
