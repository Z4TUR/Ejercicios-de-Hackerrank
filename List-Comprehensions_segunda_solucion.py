'''  List Comprehensions

 Let's learn about list comprehensions! You are given three integers X, Y and Z representing the dimensions of a cuboid along with an
 integer N. You have to print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k  is not
 equal to N. Here, 0 <= i <= X; 0 <= j <= Y; 0 <= k <= Z 

Input Format
Four integers X, Y, Z and N each on four separate lines, respectively.

Constraints
Print the list in lexicographic increasing order.

Sample Input
1
1
1
2

Sample Output
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]'''

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())


lista = []
def arreglo (x, y, z, n):
    x, y, z = x+1, y+1, z+1
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if i+j+k != n:
                    lista.append([i, j, k])               
    return lista

arreglo(x, y, z, n)
print(lista)
