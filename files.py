import os
import subprocess
j = 1

os.chdir("C:\\")
while j == 1:
    i = input('Command_Files: ')

    if i == 'q':
        j = 0

    elif i == 'ls':
        print(os.getcwd())
        print(os.listdir())

    elif i.startswith('cd'):
        if i == 'cd':
            print('Brak argumentu')
        else:
            os.chdir(i[3:])
            print(os.getcwd())

    elif i.startswith('head'):
        if i == 'head':
            print('Brak argumentu')
        else:
            try:
                with open(i[5:],'r') as file:
                    k = file.read(512)
                    print(k)
            except FileNotFoundError:
                print('Nie odnaleziono pliku')
            except PermissionError:
                print('Brak dostępu')

    elif i == 'pwd':
        print(os.getcwd())

    else:
        print('Komenda nie istnieje. Dostępne komendy: \n'
              'q - wyjście \n'
              'ls - wyświetl listę plików w bieżącym katalogu \n'
              'cd $1 - przejdź do katalogu \n'
              'pwd - wyświetla bieżącą ścieżkę \n'
              'head $1 - wyświetla pierwsze 512 bajtów pliku')

subprocess.run(["python", "Main.py"])