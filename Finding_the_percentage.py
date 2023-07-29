if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

datos = student_marks.get(query_name)

def marca (datos):
    puntaje = 0
    for punt in range(0, len(datos)):
        puntaje += datos[punt]
    
    return puntaje/3

print ("%.2f" % marca(datos))
