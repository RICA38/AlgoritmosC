import csv
import random


with open("prueba.csv", "r", newline='') as f: 
    reader = csv.reader(f, delimiter=",")
    res = [[int(n) for n in line[-3:]] for line in reader] 
    
item=[50,78,20]
distancias=[]

for newlist in range(0,len(res)):
    for indice in range(0, len(res)):
        print(res[indice])
    
        for i in res[indice]:
            print(i)

        for j in item:
            print(j)
            
        aux=i-j
        raiz=0.5**aux
        distancias.append(raiz)
        
with open('DistanciasKnn.csv', 'w', newline='') as file:
   writer = csv.writer(file)
   nregistros=len(res)
   
   for i in range(0,len(distancias)):
       texto= [distancias[i], chr(random.randint(ord('A'), ord('Z'))) ]
       writer.writerow(texto)
       texto.sort()
       print(texto)
   
    