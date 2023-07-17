
# Меню
def show_menu():
    print("\nВыбери пункт меню, введя соответствующую команду:\n"
          "1. Отобразить все заметки\n"
          "2. Найти заметку по ID\n"
          "3. Найти заметку по дате создания\n"
          "4. Добавить запись в заметку\n"
          "5. Удалить запись из заметки по ID\n"
          "6. Изменить данные записи в заметке\n"
          "7. Сохранить все заметки в текстовом формате\n"
          "8. Закончить работу")
    
    option = int(input())
    return option

# Парсинг
def parse_cvs(filename):
    columns= []
    rows = ["ID", "Название", "Тело заметки", "Дата создания" ]
    with open(filename, 'r', encoding='utf-8') as data:
        for line in data:
            record = dict(zip(rows, line.strip().split(',')))
            columns.append(record)
    return columns


#Все функции 
def notice_functions():
    option = show_menu()
    notice = parse_cvs('note.csv')

    while (option !=8):
            if option == 1:
                about_notice(notice)
            elif option == 2:
                about_notice(search_by_ID(notice))  


# 1. Отображение заметки
def about_notice(notice):
    for elem in notice:
        for key in elem:
            print(f'{key} : {elem[key]}')
        print() 

 # 2. Поиск по ID
def search_by_ID(notice):
    number = input('Введите номер ID: ')
    output = []
    for elem in notice:
        if elem['ID'] == number:
            output.append(elem)
    return output    