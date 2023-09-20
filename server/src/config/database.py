def get_db_url(user, password, host, db_name) -> str:
    return f"postgres://{user}:{password}@{host}:5432/{db_name}"
