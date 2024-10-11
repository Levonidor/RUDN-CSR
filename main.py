from services import *
from time import sleep
if __name__ == "__main__":
    startup_check()
    print('Добро пожаловать! Программа успешно запущена.\n')
    
    # printing_fix()

    registry = registry_read(registry_input())
    create_companies_sheet(registry,'template')
    print('Программа будет автоматически завершена через 10 секунд.\n')
    sleep(10)
    