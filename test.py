import os

directory = R"C:\Intel\123"

# Проверяем существование каталога
if not os.path.exists(directory):
    # Если каталога нет, создаем его
    os.makedirs(directory)
    print("Каталог", directory, "создан")
else:
    print("Каталог", directory, "уже существует")