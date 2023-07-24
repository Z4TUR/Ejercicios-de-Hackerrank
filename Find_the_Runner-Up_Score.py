Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given

scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains
. The second line contains an array of integers each separated by a space. 

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

def arreglo(arr):
    li = []
    for m in arr:
        if m not in li:
            li.append(m)
    li.sort(reverse=True)
    
    return li[1]
        
print(arreglo(arr)
