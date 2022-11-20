from django.shortcuts import render
from .models import Datos 
import pandas as pd

# Create your views here.



def  muestra_datos(request):
    consulta = Datos.objects.all()
    lista=calculaSuma(consulta)

    contexto= {'datos':lista}

    #print(lista)
    # data = pd.read_csv('prueba1/prueba.csv')
    # for i in range(len(data)):
    #      info = Datos(
    #          dato1= data['dato1'][i],
    #          c1=data['c1'][i],
    #          dato2 = data['dato2'][i],
    #          dato3 = data['dato3'][i],
    #      )
    #      info.save()
    
    return render (request,'prueba1/index.html', contexto)

def calculaSuma(l):
    lista=[]
    for i in l:
        r=i.dato1 + i.dato2 + i.dato3
        obj = {'dato1':i.dato1, 'dato2':i.dato2, 'dato3':i.dato3, 'suma':r, 'c1':i.c1}
        
        lista.append(obj)
        
    return lista