#Siempre buscar la mejor decicion
n = int(input('ingrese n ')) #pedimos los numeros por pantalla
k = int(input('ingrese k '))

arr = []
i = 0
contk = 0
while n > i:
    numero = int(input())
    if(numero >= -2147483648 and numero <= 2147483648): # en esta linea de codigo verificamos si la restriccion se cumple
        arr.append(numero)
        i = i + 1 
    else:
        break    
    
arr.sort()         
#El metodo sort() de python utiliza el algoritmo de ordenamiemto timsort el cual tiene como orden de complejidad O(nlog(n))   
for i in range(n - 1):
    if(arr[i + 1] - arr[i] == k ):  #comparamos todas las restas de los numeros ingresados posibles 
        contk = contk + 1   
    
     
       
print(contk)
# por lo tanto el codigo tiene un orden de complejidad de O(nlog(n))
""" 
Se generaron los siguientes ejemplos con chat GPT
ej:1

5 3
1 4 7 10 13
4

Ej2:
6 2
-5 -3 -1 1 3 5
5 

Ej3:
5 100
100 200 300 400 500
4
"""