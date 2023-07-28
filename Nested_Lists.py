"""
Given the names and grades for each student in a class of
students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example
The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:
alpha
beta
"""

lista = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista.append([name, score])

def orden (lista):
    n_lista=sorted(lista, key=lambda lista: (lista[1], lista[0]))
    for pers in range(0, len(n_lista)):
        enc = []
        if n_lista[pers][1] != n_lista[pers + 1][1]:
            x = pers + 1
            for exc in range (x, len(n_lista)):
                if n_lista[exc][1] == n_lista[x][1]:
                    enc.append(n_lista[exc])

            for orden in range(len(enc)):
                print(enc[orden][0])

            break
        else:
            enc.clear()
        
orden(lista)
