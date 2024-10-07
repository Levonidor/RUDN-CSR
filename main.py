from services import *
import os.path

if __name__ == "__main__":
    Startup_Check()
    print('Добро пожаловать! Программа успешно запущена.\n')
    
    registry = Registry_Read(Registry_Input())

    # print(len(registry))
    # print(registry[-1])
    Create_Companies_Sheet(registry,'template')
    # print(registry[0])
    print('Программа будет завершена через 10 секунд.\n')
    sleep(10)