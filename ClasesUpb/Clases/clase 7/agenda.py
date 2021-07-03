import pandas as pd

def get_data(): 
    return pd.read_csv("agenda.csv")
    
def show_menu():
    print("\nOpciones\n1. Crear\n2. Listar\n3. Buscar\n4. Editar\n5. Eliminar\n7. Salir")
    option= input("Digite la opcion:\n")
    if option =="1":
        create()
    elif option =="2":
        list_contacts()
    elif option =="3":
        search()
    elif option =="4":
        update()
    elif option =="5":
        delete()
    elif option == "7":
        exit()

def create():
    name, phone, email = input("Nombre:\n"), input("Telefono:\n"), input("E-mail:\n") 
    filer = open('agenda.csv','a')
    filer.write(f"{name},{phone},{email}\n")
    filer.close()

def list_contacts():
    print(get_data())

def search():
    name = input("Digita el nombre que deseas buscar:\n")
    dataf = get_data()
    print(dataf[dataf['Nombre'].str.contains(name)])

def update():
    list_contacts()
    id = int(input("ID del contacto a modificar:\n"))
    option = input("¿Que desea editar?\n1. Nombre\n2. Telefono\n3. E-mail\n")
    dataf = get_data()
    if option == "1":
        dataf.loc[id, 'Nombre'] = input("Nombre:\n")
    elif option == "2":
        dataf.loc[id, 'Telefono'] = input("Telefono:\n")
    elif option =="3":
        dataf.loc[id, 'Email'] = input("E-mail:\n")
    dataf.to_csv('agenda.csv', index = False)


def delete():
    list_contacts()
    id = int(input("ID del contacto a eliminar:\n"))
    dataf = get_data()
    dataf.drop([id], inplace=True,axis=0)
    dataf.to_csv('agenda.csv', index = False)   

def run():
    show_menu()
    run()

if __name__ == "__main__":
    run()