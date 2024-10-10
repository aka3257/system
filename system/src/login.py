# login.py
def authenticate(username, password):
    """Функция для аутентификации пользователя."""
    # Здесь можно добавить реальную проверку с базой данных, например
    # Для примера проверим простые строки
    if username == "admin" and password == "password":
        return True
    else:
        return False