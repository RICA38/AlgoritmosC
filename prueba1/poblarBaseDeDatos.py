import csv
from models import Datos


fields = ["x1", "x2", "x3"]

for row in csv.reader(open('C:\Users\grill\Downloads\ALG\clasificacion\prueba.csv')):
    Datos.objects.create(**dict(zip(fields, row)))