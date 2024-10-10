from login import authenticate
from modules.hello import command_hello
from modules.time import command_time

def command_exit():
    """Команда 'exit'."""
    print("Выход из системы.")
    return False

def command_status():
    """Команда 'status'."""
    print("Система работает в штатном режиме.")
    return True

def run_command(command):
    """Функция для выполнения команд."""
    commands = {
        "hello": command_hello,
        "exit": command_exit,
        "time": command_time,
        "status": command_status,
    }
    
    if command in commands:
        result = commands[command]()
        if result is False:
            return False
        return True
    else:
        print(f"Неизвестная команда: {command}")
        return True

def main():
    print("Welcome to the system!")  # Сообщение при запуске

    attempts = 3
    while attempts > 0:
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        if authenticate(username, password):
            print("Аутентификация успешна. Добро пожаловать!")
            break
        else:
            attempts -= 1
            print(f"Неверные данные. Осталось попыток: {attempts}")
    
    if attempts == 0:
        print("Превышено количество попыток. Доступ запрещен.")
        return

    while True:
        command = input("user@system $ ")
        if not run_command(command):
            break

if __name__ == "__main__":
    main()
