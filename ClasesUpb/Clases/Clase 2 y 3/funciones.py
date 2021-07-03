'''
def calcular_tiempo_recorrido(numero_abordados:int, numero_desc:int):
    x = 180 + (numero_abordados*2)
    x = x + numero_desc
    print(f"el tiempo es {x} minutos")

numero_abordados = int(input("Cuantos pasajeros suben: "))
numero_desc = int(input("Cuantos pasajeros bajan: "))
calcular_tiempo_recorrido(numero_abordados,numero_desc)
'''

def calcular_tiempo_recorrido(v_por_hora:int,recorrido_total:int, numero_abordados:int, numero_desc:int):

    min_total = int((recorrido_total/v_por_hora)*60)
    min_total = min_total + (numero_abordados*2)
    min_total = min_total + numero_desc
    print(f"el tiempo es {min_total} minutos")

v_por_hora = int(input("Velocidad del bus (Km/h): "))
recorrido_total = int(input("reorrido total (Km): "))
numero_abordados = int(input("Cuantos pasajeros suben: "))
numero_desc = int(input("Cuantos pasajeros bajan: "))

calcular_tiempo_recorrido(v_por_hora,recorrido_total,numero_abordados,numero_desc)
