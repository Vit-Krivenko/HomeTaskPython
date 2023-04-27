import functions,interface



def main_prog():
    flag = True
    while flag:
        num_user = interface.begining()
        if num_user == '1':
            functions.add_contact(interface.get_contact())
        elif num_user == '2':
            functions.search_contact()
        elif num_user == '3':
            functions.print_all()
        elif num_user == '4':
            functions.change_contact()
        elif num_user == '5':
            functions.del_contact()
        else:
            flag = False



main_prog()