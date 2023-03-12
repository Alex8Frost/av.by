import environ

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, 'secretKey'),
    ALLOWED_HOSTS=(str, '*'),
    HOST=(str, '127.0.0.1'),

    POSTGRES_DB=(str, 'av_db'),
    POSTGRES_USER=(str, 'av_user'),
    POSTGRES_PASSWORD=(str, 'av_password'),
    POSTGRES_HOST=(str, 'db'),
    POSTGRES_PORT=(int, None),

)

