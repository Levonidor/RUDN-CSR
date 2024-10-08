from services import *
import os.path

if __name__ == "__main__":
    startup_check()
    print('Добро пожаловать! Программа успешно запущена.\n')
    
    registry = registry_read(registry_input())

    # print(len(registry))
    # print(registry[-1])
    create_companies_sheet(registry,'template')
    # print(registry[0])
    print('Программа будет завершена через 10 секунд.\n')
    sleep(10)