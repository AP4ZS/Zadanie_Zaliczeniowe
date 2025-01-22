import subprocess

j=1

while j==1:
    op=input('Podaj operację:')
    if op=='+':
        a=[]
        l=0
        k=input('Liczba cyfr w dodawaniu: ')
        for l in range(int(k)):
            a.append(int(input(str(l+1)+' liczba: ')))
            l=l+1
        wynik=sum(a)
        print(wynik)

    elif op=='-':
        a = []
        l = 0
        k = input('Liczba cyfr w odejmowaniu: ')
        for l in range (int(k)):
            a.append(int(input(str(l+1) + ' liczba: ')))
            l = l + 1
        wynik = a[0]
        b=1
        k=len(a)
        for b in range (1, k):
            wynik -= a[b]
            b=b+1
        print(wynik)




    elif op=='*':
        a = []
        l = 0
        k = input('Liczba cyfr w mnożeniu: ')
        for l in range(int(k)):
            a.append(int(input(str(l+1) + ' liczba: ')))
        wynik = a[0]
        b = 1
        k=len(a)
        for b in range (1, k):
            wynik = wynik * a[b]
        print (wynik)
    elif op=='/':
        a = []
        l = 0
        k = input('Liczba cyfr w dzieleniu: ')
        for l in range(int(k)):
            a.append(int(input(str(l+1) + ' liczba: ')))
        wynik = a[0]
        b = 1
        k=len(a)
        for b in range (1, k):
            wynik = wynik / a[b]
        print (wynik)

    elif op=='!':
        l = int(input('Podaj silnię: '))
        a = list(range(1, l+1))
        k = len(a)
        b = 1
        wynik = a[0]
        for b in range (1, k):
            wynik = wynik * a[b]
        print (wynik)



    elif op=='^':
        l = 1
        k = int(input('Potęgowana liczba: '))
        m = int(input('Do potęgi: '))
        m -= 1
        wynik = k
        for l in range(int(m)):
            wynik = wynik * k
        print (wynik)

    elif op=='q':
        j=0

    else:
        print('Dostępne operacje: \n'
              '"+" - Dodawanie \n'
              '"-" - Odejmowanie \n'
              '"*" - Mnożenie \n'
              '"/" - Dzielenie \n'
              '"!" - Silnia \n'
              '"^" - Potęgowanie \n')

subprocess.run(["python", "Main.py"])
