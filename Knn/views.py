from django.shortcuts import render
from .models import Datosknn
from prueba1.models import Datos
import pandas as pd
import math
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
    return render (request,'Knn/Knn.html',algoritmknn(request))


def algoritmknn(request):
    datos = Datos.objects.all()
    # with open("Knn/prueba.csv", "r", newline='') as f: 
    #     reader = csv.reader(f, delimiter=",")
    #       res = [[int(n) for n in line[-3:]] for line in reader] 
    

    print(request.POST['prod1'])
    print(request.POST['prod2'])
    print(request.POST['prod3'])

    item=[32,18,38]
    distancias=[]
    Ordenado=[]
    mostrarL=[]
    print(len(datos))
    # for newlist in range(0,len(res)):
    for i in range(len(datos)):
        distancias.append(math.sqrt(((datos[i].dato1 - item[0])**2)) + ((datos[i].dato2 - item[1])**2) + ((datos[i].dato3 - item[2])**2))


    # print(len(distancias))
        # aux=i-j
        # raiz=0.5**aux
        
        # distancias.append(raiz)
        
    # with open('Knn/DistanciasKnn.csv', 'w', newline='') as file:
    #     writer = csv.writer(file)
        
    #     header= ["Distancia","Caracter"]
    #     writer.writerow(header)
    #     for i in range(0,len(distancias)):    
    #         texto= [distancias[i], chr(random.randint(ord('A'), ord('Z'))) ]
    #         writer.writerow(texto)
            
    # df=pd.read_csv('Knn/DistanciasKnn.csv') 
    # order=df.sort_values(by=['Distancia'],ascending=[True])
    # print(df.iloc[0])
    # Ordenado.append(order)
    
    
    # obj = {'datos':Ordenado}

    # new list = {letra: datos[i].c1, distancia: distancia[i] }



    contexto={'datos': datos, 'distancias': distancias}
    
    
    return contexto
    

