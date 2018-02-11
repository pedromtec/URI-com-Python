# Problema -> Conversão de Tempo
segundos = int(input())
minutos = segundos//60
segundos%=60
horas = minutos//60
minutos%=60
print("{}:{}:{}".format(horas,minutos,segundos))