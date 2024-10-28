from services import *
from time import sleep
if __name__ == "__main__":
    startup_check()
    print('Добро пожаловать! Программа успешно запущена.\n')
    
    # registry = registry_read(registry_input())
    # create_companies_sheet_gov(registry,'template')
    printing_fix()
    print('Программа будет автоматически завершена через 10 секунд.\n')
    sleep(10)
    