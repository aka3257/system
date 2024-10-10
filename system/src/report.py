# module3.py

def generate_report(data):
    """Функция для генерации отчета."""
    print("Генерация отчета...")
    
    if not data:
        return "[ОШИБКА] Нет данных для генерации отчета."
    
    report = f"Отчет: {len(data)} элементов. Данные: {data}"
    print("[УСПЕШНО] Генерация отчёта")
    return report
