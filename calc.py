import subprocess

j = 1

# Funkcja do zapisywania historii działań do pliku
def zapisz_do_histori(opis):
    with open("historia.txt", "a") as f:
        f.write(opis + "\n")

while j == 1:
    op = input('Podaj operację: ')

    if op == '+':
        a = []
        l = 0
        k = input('Liczba cyfr w dodawaniu: ')
        if not k.isdigit():
            print("Podaj liczbę całkowitą")
            continue
        for l in range(int(k)):
            a.append(int(input(str(l + 1) + ' liczba: ')))
            l = l + 1
        wynik = sum(a)
        print(wynik)

        # Zapisz do historii
        zapisz_do_histori(f'Dodawanie: {" + ".join(map(str, a))} = {wynik}')

    elif op == '-':
        a = []
        l = 0
        k = input('Liczba cyfr w odejmowaniu: ')
        if not k.isdigit():
            print("Podaj liczbę całkowitą")
            continue
        for l in range(int(k)):
            a.append(int(input(str(l + 1) + ' liczba: ')))
            l = l + 1
        wynik = a[0]
        b = 1
        k = len(a)
        for b in range(1, k):
            wynik -= a[b]
            b = b + 1
        print(wynik)

        # Zapisz do historii
        zapisz_do_histori(f'Odejmowanie: {" - ".join(map(str, a))} = {wynik}')

    elif op == '*':
        a = []
        l = 0
        k = input('Liczba cyfr w mnożeniu: ')
        if not k.isdigit():
            print("Podaj liczbę całkowitą")
            continue
        for l in range(int(k)):
            a.append(int(input(str(l + 1) + ' liczba: ')))
        wynik = a[0]
        b = 1
        k = len(a)
        for b in range(1, k):
            wynik = wynik * a[b]
        print(wynik)

        # Zapisz do historii
        zapisz_do_histori(f'Mnożenie: {" * ".join(map(str, a))} = {wynik}')

    elif op == '/':
        a = []
        l = 0
        k = input('Liczba cyfr w dzieleniu: ')
        if not k.isdigit():
            print("Podaj liczbę całkowitą")
            continue
        for l in range(int(k)):
            a.append(int(input(str(l + 1) + ' liczba: ')))
        wynik = a[0]
        b = 1
        k = len(a)
        for b in range(1, k):
            wynik = wynik / a[b]
        print(wynik)

        # Zapisz do historii
        zapisz_do_histori(f'Dzielenie: {" / ".join(map(str, a))} = {wynik}')

    elif op == '!':
        l = int(input('Podaj silnię: '))
        if not str(l).isdigit():
            print("Podaj liczbę całkowitą")
            continue
        a = list(range(1, l + 1))
        k = len(a)
        b = 1
        wynik = a[0]
        for b in range(1, k):
            wynik = wynik * a[b]
        print(wynik)

        # Zapisz do historii
        zapisz_do_histori(f'Silnia: {l}! = {wynik}')

    elif op == '^':
        l = 1
        k = int(input('Potęgowana liczba: '))
        if not str(k).isdigit():
            print("Podaj liczbę całkowitą")
            continue
        m = int(input('Do potęgi: '))
        if not str(m).isdigit():
            print("Podaj liczbę całkowitą")
            continue
        m -= 1
        wynik = k
        for l in range(int(m)):
            wynik = wynik * k
        print(wynik)

        # Zapisz do historii
        zapisz_do_histori(f'Potęgowanie: {k}^{m + 1} = {wynik}')

    elif op == 'q':
        j = 0

    else:
        print('Dostępne operacje: \n'
              '"+" - Dodawanie \n'
              '"-" - Odejmowanie \n'
              '"*" - Mnożenie \n'
              '"/" - Dzielenie \n'
              '"!" - Silnia \n'
              '"^" - Potęgowanie \n')

subprocess.run(["python", "Main.py"])
