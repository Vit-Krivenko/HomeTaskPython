import interface

def add_contact(contact):
    data = open('file.txt','a')
    data.writelines(contact)
    data.write('\n')
    data.close()


def search_contact():
    contact_list = open('file.txt','r')
    search = input ('Введите фамилию для поиска: ')
    for i in contact_list:
        if search in i:
            print(i)
    contact_list.close()



def print_all():
    contact_list = open('file.txt','r')
    num = 1
    for i in contact_list:
        print(f'{num}. {i}')
        num +=1
    contact_list.close()



def del_contact():
    contact_list = open('file.txt','r')
    change_list = []
    changed_name = input ('Введите фамилию для удаления: ')
    for i in contact_list:
        if changed_name in i:
                continue
        change_list.append(i) 
    contact_list.close()

    contact_list = open('file.txt','w')
    for i in change_list:
        contact_list.writelines(i)
    contact_list.close()



def change_contact():
    contact_list = open('file.txt','r')
    change_list = []
    changed_name = input ('Введите фамилию которую нужно изменить: ')
    fill_to_change = input('Введите поле, которое нужно изменить("Фамилия", "Имя", "Отчество" или "Телефон"): ')
    new_value = input(f"Введите новое значение для поля {fill_to_change} ")

    for i in contact_list:
        if changed_name in i:
            fields = i.split()
            if fill_to_change == 'Фамилия':
                fields[0] = new_value
            elif fill_to_change == 'Имя':
                fields[1] = new_value
            elif fill_to_change == 'Отчество':
                fields[2] = new_value
            elif fill_to_change == 'Телефон':
                fields[3] = new_value
            changed_line = ' '.join(fields) + '\n'
            change_list.append(changed_line)
        else:
            change_list.append(i)
    contact_list.close()
    

    contact_list = open('file.txt','w')
    for i in change_list:
        contact_list.writelines(i)
    contact_list.close()


