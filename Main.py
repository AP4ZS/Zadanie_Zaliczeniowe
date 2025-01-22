import subprocess
i=1
while i==1:
    cmd=(input('Command: '))
    if cmd=='quit':
        i=0

    elif cmd=='calc':
        subprocess.run(["python", "calc.py"])
        i=0

    elif cmd=='files':
        subprocess.run(["python", "files.py"])
        i=0

    else:
        print('Podana komenda nie istnieje. Dostępne komendy:\n'
              'quit - wyjdź z programu\n'
              'calc - kalkulator\n'
              'files - obsługa plików\n')
