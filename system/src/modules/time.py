import datetime

def command_time():
    """Команда 'time'."""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Текущее время: {current_time}")
    return True