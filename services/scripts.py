import openpyxl
from .cfg import RegIndex,TempCell,Abbreviations,Abbreviations_Decryption
from math import floor
import datetime
import os.path
from time import sleep
from sys import exit

def startup_check():
        print('Запуск программы...')
        sleep(0.25)
        print('Проверка файлов...\n')
        sleep(0.25)
        if os.path.exists('./import_files/template.xlsx'):
            pass
        else:
            print('Ошибка! Не обнаружен файл шаблона. Проверьте наличие файла "template.xlsx" в папке "import_files". \n Программа будет завершена через 10 секунд.')
            sleep(12)
            exit()

def registry_input():
        while True:
            registry_filename = str(input('Введите название файла реестра (Пример: somename): '))
            if os.path.exists(f'./import_files/{registry_filename}.xlsx'):
                break
            else:
                print('\n Ошибка! Данный файл не найден. \n Проверьте название файла, уберите лишние пробелы и/или перезапустите программу. \n')
        print('')
        return registry_filename

# Считывание реестра-excel в список [[компания1],[компания2]]
def registry_read(filename: str) -> list:
    book = openpyxl.open(f'./import_files/{filename}.xlsx',read_only=True)
    registry = book.active
    reg_list = []
    for row in registry.iter_rows(min_row=2,max_row=registry.max_row,min_col=registry.min_column,max_col=registry.max_column+2):
        company = []
        for cell in row:
            if cell.value != None:
                company.append(cell.value)
            else:
                company.append('Нет Данных')
        reg_list.append(company)
    book.close()
    print(f'<><><><><>\nРеестр успешно прочтен \n Количество компаний: {len(reg_list)}\n<><><><><>\n')
    sleep(0.2)
    return reg_list


# Создает обложку для компании сответсвенно шаблону
def create_companies_sheet(companies: list, template_filename: str) -> None:
    print('<><><><><>\nНачало обработки файлов\n<><><><><>\n')
    book = openpyxl.open(f'./import_files/{template_filename}.xlsx')
    company_head_sheet = book.active
    companies_percent_count = floor(len(companies)/100)
    companies_count,percent_of_creating = 0,0
    time = datetime.datetime.now().replace(microsecond=0)
    for company in companies:
        company_name = (company[RegIndex.NAME.value].split())
        if company_name[0] in Abbreviations:
            company_head_sheet[TempCell.NAME.value] = Abbreviations_Decryption[(Abbreviations.index(company_name[0]))]+' '+''.join(company_name[1:])
        else:
            company_head_sheet[TempCell.NAME.value] = company[RegIndex.NAME.value]
        company_head_sheet[TempCell.LEGAL_ADDRESS.value] = company[RegIndex.ADDRESS.value]
        company_head_sheet[TempCell.POSTMAIL_ADDRESS.value] = company[RegIndex.ADDRESS.value]
        company_head_sheet[TempCell.ADMINISTRATOR.value] = f'{company[RegIndex.SURNAME.value]} {company[RegIndex.FIRSTNAME.value]} {company[RegIndex.PATRONYMIC.value]}'
        company_head_sheet[TempCell.YEAR.value] = '2024'
        company_head_sheet[TempCell.OWNERSHIP_FORM.value] = 'Частная собственность' 
        company_head_sheet[TempCell.OKPO.value] = company[RegIndex.OKPO.value]
        company_head_sheet[TempCell.OKVED_ACTIVITY_TYPE.value] = company[RegIndex.OKVED_ACTIVITY_TYPE.value]
        company_head_sheet[TempCell.OKATO_TERRITORY.value] = company[RegIndex.OKATO_TERRITORY.value]
        company_head_sheet[TempCell.INN.value] = company[RegIndex.INN.value]
        company_head_sheet[TempCell.KPP.value] = company[RegIndex.KPP.value]
        company_head_sheet[TempCell.OGRN.value] = company[RegIndex.OGRN.value]

        fixed_name_for_save = (str(company[RegIndex.NAME.value])).replace('"','').replace('/',' ').replace('\\',' ').replace('<',' ').replace('>',' ') +' '+str(company[RegIndex.INN.value])
        book.save('./export_files/'+f'{fixed_name_for_save}.xlsx')
        companies_count += 1
        if companies_count%companies_percent_count==0 and companies_count/companies_percent_count!=100 and companies_count/companies_percent_count!=0:
            percent_of_creating+=1
            print(f'Выполнение: {percent_of_creating}%  |   Оставшееся время: {(datetime.datetime.now().replace(microsecond=0) - time)*(100-percent_of_creating)}')
            time = datetime.datetime.now().replace(microsecond=0)
    book.close()
    print('<><><><><>\nВсе файлы успешно обработаны\nПроверьте папку export_files\n<><><><><>\n')

    