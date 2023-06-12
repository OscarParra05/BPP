import csv
import calendar
import locale
import matplotlib.pyplot as plt

def leer_csv(nombre_archivo):
    datos = []
    with open(nombre_archivo, 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter=';')
        next(lector_csv)
        for fila in lector_csv:
            datos.extend(fila)
    return datos

def obtener_mes_mas_gasto(datos):
    gastos = [float(valor) for valor in datos if es_valor_numerico(valor)]
    indice_mes_mas_gasto = gastos.index(max(gastos))
    mes_mas_gasto = calendar.month_name[indice_mes_mas_gasto % 12 + 1]
    return mes_mas_gasto

def obtener_mes_mas_ahorro(datos):
    ahorros = [float(valor) for valor in datos if es_valor_numerico(valor)]
    indice_mes_mas_ahorro = ahorros.index(min(ahorros))
    mes_mas_ahorro = calendar.month_name[indice_mes_mas_ahorro % 12 + 1]
    return mes_mas_ahorro

def calcular_media_gastos(datos):
    gastos = [float(valor) for valor in datos if es_valor_numerico(valor)]
    media_gastos = sum(gastos) / len(gastos)
    return media_gastos

def calcular_gasto_total(datos):
    gastos = [float(valor) for valor in datos if es_valor_numerico(valor)]
    gasto_total = sum(gastos)
    return gasto_total

def calcular_ingresos_totales(datos):
    ingresos = [float(valor) for valor in datos if es_valor_numerico(valor)]
    ingresos_totales = sum(ingresos)
    return ingresos_totales

def es_valor_numerico(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

nombre_archivo = 'Finanzas2020.csv'

#Leemos los datos del archivo CSV
datos = leer_csv(nombre_archivo)

#Comprobamos que el archivo tiene 12 columnas
if len(datos) != 12:
    print(f"El archivo {nombre_archivo} no tiene 12 columnas. Continuando con la ejecución...")

locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

try:
    #Obtenemos el mes con mayor gasto
    mes_gasto = obtener_mes_mas_gasto(datos)
    print("Mes con mayor gasto:", mes_gasto)

    #Obtenemos el mes con mayor ahorro
    mes_ahorro = obtener_mes_mas_ahorro(datos)
    print("Mes con mayor ahorro:", mes_ahorro)

    #Calculamos la media de gastos al año
    media_gastos = calcular_media_gastos(datos)
    print("Media de gastos al año:", media_gastos)

    #Calculamos el gasto total a lo largo del año
    gasto_total = calcular_gasto_total(datos)
    print("Gasto total a lo largo del año:", gasto_total)

    #Calculamos los ingresos totales a lo largo del año
    ingresos_totales = calcular_ingresos_totales(datos)
    print("Ingresos totales a lo largo del año:", ingresos_totales)

    months = [calendar.month_name[i] for i in range(1, 13)]

    income = [float(valor) if es_valor_numerico(valor) else 0 for valor in datos[:12]]

    #Obtenemos la gráfica de la evolución de los ingresos a lo largo del año
    plt.plot(months, income, marker='o')
    plt.title('Evolución de los ingresos a lo largo del año')
    plt.xlabel('Meses')
    plt.ylabel('Ingresos')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

except IndexError:
    print("No hay suficientes datos para calcular los resultados.")
except ValueError as e:
    print("Error al procesar los datos:", str(e))
except Exception as e:
    print("Se produjo un error:", str(e))
