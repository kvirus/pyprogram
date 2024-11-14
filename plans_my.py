import schedule
import time
import subprocess

# Функция для запуска внешней программы
def run_external_program():
    try:
        subprocess.Popen(["C:\Intel\showjpg\show_img.exe"])  # Укажите правильный путь к внешней программе
        print("Запуск внешней программы...")
    except Exception as e:
        print(f"Возникла ошибка при запуске внешней программы: {e}")

# Запланировать выполнение задачи в нужное время
#schedule.every().day.at("16:00").do(run_external_program)  # Например, запускать программу каждый день в 10:00
#schedule.every(2).minutes.do(run_external_program)
schedule.every().hour.at(":12").do(run_external_program)

# Добавить дополнительное планирование для выполнения каждые 2 минуты
schedule.every(1).minutes.do(run_external_program)


# Запуск планировщика в цикле
while True:
    schedule.run_pending()
    time.sleep(1)