with open('fileName', 'a') as data:
    data.writelines('')
print('') 

 # Вывод инфрмации
        
def show_data():
    phoneNumberBook = readData('C:/Users/Пользователь/Desktop/Python_DZ/fileName')
    for i in phoneNumberBook:
        print(i)
        
def readData(fileName):
    with open(fileName) as f:
         phoneNumberBook=[]
         for line in f:
             phoneNumberBook.append(line.split(','))
    return phoneNumberBook   

        # Запись  новых данных
        
def records_data(filename):
    with open(filename, 'r', encoding="utf-8") as data:
        tel_file = data.read()
    num = len(tel_file.split('\n'))
    with open(filename, 'a', encoding="utf-8") as data:  
        surName = str(input('Enter surName:')) 
        firstName = str(input('Enter firstName:'))
        midleName = str(input('Enter midleName:'))
        phoneNumberNumber = str(input('phoneNumberNumber:'))
        data.write(f'{num}. {surName }  {firstName}  {midleName} - { phoneNumberNumber }\n')
        print(f'Новая запись: {num}, {surName }, {firstName}, {midleName}, { phoneNumberNumber }')

         #  Удаление данных
               
def delete_data(filename):
    print(f'num surName  firstName midleName  phoneNumberNumber ')
    with open(filename, "r", encoding="utf-8") as data:
        tel_file = data.read()
        print(tel_file)
    print("")
    index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
    tel_file_lines = tel_file.split("\n")
    del_tel_file_lines = tel_file_lines[index_delete_data]
    tel_file_lines.pop(index_delete_data)
    print(f"Удалено: {del_tel_file_lines}\n")
    with open(filename, "w", encoding='utf-8') as data:
        data.write("\n".join(tel_file_lines)) 
        
     # Изменяет информацию из файла (Фамилия+Телефон)
     
def edit_data(filename):
    print(f'num surName  firstName midleName  phoneNumberNumber ')
    with open(filename, "r", encoding='utf-8') as data:
        tel_file = data.read()
    print(tel_file)
    print("")
    index_delete_data = int(input("Введите номер строки для редактирования: ")) - 1
    tel_file_lines = tel_file.split("\n")
    edit_tel_file_lines = tel_file_lines[index_delete_data]
    elements = edit_tel_file_lines.split(" | ")
    surName = str(input('Enter surName:')) 
    # firstName = str(input('Enter firstName:')) 
    # midleName = str(input('Enter midleName:'))
    phoneNumber = str(input('phoneNumberNumber:'))
    num = elements[0]
    if len(surName) == 0:
        surName = elements[1]
    if len(phoneNumber) == 0:
        phoneNumber = elements[2]
    edited_line = f'{num} =>> {surName} {phoneNumber}'
    tel_file_lines[index_delete_data] = edited_line
    print(f'Запись - {edit_tel_file_lines}, изменена на - {edited_line}\n')
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(tel_file_lines))    
        

print('''HELLO User:/n 
      [1] -- Вывод информации
      [2] -- Запись данных
      [3]-- Изменение данных
      [4] -- Удаление данных
      [5] -- Выход из программы ''')
action = int(input("Действие: "))
if action == 1:
    show_data()
elif action == 2:
       records_data('filename')
elif action == 3:
    edit_data('filename')
elif action == 4:
         delete_data('filename')
else:
     action == 0
     print()
     print('WHAT DO you WANT to DO?')    
print()   