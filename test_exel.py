import openpyxl

# Создаем новый файл Excel
workbook = openpyxl.Workbook()
sheet = workbook.active

# Добавляем заголовки в первую строку
sheet['A1'] = 'Название'
sheet['B1'] = 'Цена'

# Добавляем данные в таблицу
for i in range(1, 6):
    name = f'Товар {i}'
    price = i * 100

    sheet[f'A{i + 1}'] = name
    sheet[f'B{i + 1}'] = price

workbook.save('c:\\products.xlsx')