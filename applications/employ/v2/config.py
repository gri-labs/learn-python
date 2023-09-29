def config_database():
    config = {
        'SQLALCHEMY_DATABASE_URI': 'mysql+mysqlconnector://root:root@:3308/'
    }

    return config