import pandas as pd
import matplotlib.pyplot as plt

archivo = r"Datos\\IngresoNacional.xlsx"

df = pd.read_excel(archivo, sheet_name="REGIONAL")
años = df[(df["Año"] >= 2020)]
print(años)