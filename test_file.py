from openpyxl import Workbook

# Создаем новый рабочий файл
wb = Workbook()

# Создаем активный лист
ws = wb.active

# Заполняем лист данными
ws['A1'] = 'Hello, World!'

# Указываем путь к папке, где вы хотите сохранить файл
folder_path = './export_files/'
file_name = 'example.xlsx'
full_path = folder_path + file_name

# Сохраняем файл
wb.save(folder_path+file_name)

print(f"Файл сохранен в {full_path}")
