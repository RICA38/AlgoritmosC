from django.shortcuts import render
from .models import Datosknn
import pandas as pd
import csv
import random
# Create your views here.



def  myKnn(request):
    
   
    # consulta = Datosknn.objects.all()
    # contexto= {'datos':consulta}

    # data = pd.read_csv('Knn/DistanciasKnn.csv')
    # for i in range(len(data)):
    #      info = Datosknn(
    #          data1= data['data1'][i],
    #          car1=data['car1'][i],
    #      )
    #      info.save()
    # print(contexto)
    return render (request,'Knn/Knn.html',{'algoritmknn':algoritmknn()})


def algoritmknn():
    with open("Knn/prueba.csv", "r", newline='') as f: 
        reader = csv.reader(f, delimiter=",")
        res = [[int(n) for n in line[-3:]] for line in reader] 
    
    item=[32,18,38]
    distancias=[]
    Ordenado=[]
    mostrarL=[]
    
    # for newlist in range(0,len(res)):
    for indice in range(0, len(res)):
            
    
        for i in res[indice]:
                i

        for j in item:
                j
                
            
        aux=i-j
        raiz=0.5**aux
        
        distancias.append(raiz)
        
    with open('Knn/DistanciasKnn.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        
        header= ["Distancia","Caracter"]
        writer.writerow(header)
        for i in range(0,len(distancias)):
            
            texto= [distancias[i], chr(random.randint(ord('A'), ord('Z'))) ]
            writer.writerow(texto)
            
    df=pd.read_csv('Knn/DistanciasKnn.csv') 
    order=df.sort_values(by=['Distancia'],ascending=[True])
    print(order.iloc[0][0]) 
    Ordenado.append(order)
    
    # obj = {'datos':Ordenado}
    contexto={'datos':Ordenado}
    
    
    return contexto
    

