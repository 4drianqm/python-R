import mysql.connector
import pandas as pd
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from ttkthemes import ThemedStyle
from rpy2.robjects import r

def mostrar_grafica():
    # Establecer la conexión a la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="adrian12",
        database="purchases"
    )

    # Realizar una consulta SQL
    query = "SELECT country, SUM(purchase_amount) as Total FROM purchase INNER JOIN country ON country_id = country.idcountry GROUP BY country_id ORDER BY Total DESC LIMIT 5;"

    cursor = conexion.cursor()
    cursor.execute(query)

    # Obtener los resultados de la consulta y convertirlos en un DataFrame de Pandas
    resultados = cursor.fetchall()
    result_dataset = pd.DataFrame(resultados, columns=["country", "Total"])

    df = result_dataset.sort_values(by="Total", ascending=False).head(5)

    pandas2ri.activate()
    result_dataset_r = pandas2ri.py2rpy(df)

    # Crear la ventana de la interfaz gráfica
    ventana = tk.Tk()
    ventana.title("Gráfico de Top 5 Países")

    # Crear el contenedor del gráfico
    contenedor_grafico = ttk.Frame(ventana)
    contenedor_grafico.pack(padx=10, pady=10)

    # Enviar los datos al entorno R
    r.assign("df", result_dataset_r)

    # Ejecutar el código R para crear el gráfico
    r('''
    barplot(df$Total, names.arg = df$country, col = "blue",
            main = "Top 5 países", xlab = "País", ylab = "Total")
    ''')

    # Botón para cerrar la ventana
    boton_cerrar = ttk.Button(ventana, text="Cerrar", command=ventana.destroy)
    boton_cerrar.pack(pady=10)

    # Iniciar el bucle principal de la interfaz gráfica
    ventana.mainloop()

def mostrar_grafica_genero():
    # Establecer la conexión a la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="adrian12",
        database="purchases"
    )

    # Realizar la segunda consulta SQL
    query = "SELECT gender, SUM(purchase_amount) as Total FROM purchase INNER JOIN gender ON gender_id = gender.idgender GROUP BY gender_id ORDER BY Total DESC LIMIT 5;"

    cursor = conexion.cursor()
    cursor.execute(query)

    # Obtener los resultados de la consulta y convertirlos en un DataFrame de Pandas
    resultados = cursor.fetchall()
    result_dataset = pd.DataFrame(resultados, columns=["gender", "Total"])

    df = result_dataset.sort_values(by="Total", ascending=False).head(5)

    pandas2ri.activate()
    result_dataset_r = pandas2ri.py2rpy(df)

    # Crear la ventana de la interfaz gráfica
    ventana = tk.Tk()
    ventana.title("Gráfico de Top 5 Géneros")

    # Crear el contenedor del gráfico
    contenedor_grafico = ttk.Frame(ventana)
    contenedor_grafico.pack(padx=10, pady=10)

    # Enviar los datos al entorno R
    r.assign("df_genero", result_dataset_r)

    # Ejecutar el código R para crear el gráfico
    r('''
    barplot(df_genero$Total, names.arg = df_genero$gender, col = "red",
            main = "Top 5 géneros", xlab = "Género", ylab = "Total")
    ''')

    # Botón para cerrar la ventana
    boton_cerrar = ttk.Button(ventana, text="Cerrar", command=ventana.destroy)
    boton_cerrar.pack(pady=10)

    # Iniciar el bucle principal de la interfaz gráfica
    ventana.mainloop()

def mostrar_grafica_payment():
    # Establecer la conexión a la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="adrian12",
        database="purchases"
    )

    # Realizar la segunda consulta SQL
    query = "SELECT payment_method, SUM(purchase_amount) as Total FROM purchase INNER JOIN payment_method ON payment_method_id = payment_method.idpayment_method GROUP BY payment_method ORDER BY Total DESC LIMIT 5;"

    cursor = conexion.cursor()
    cursor.execute(query)

    # Obtener los resultados de la consulta y convertirlos en un DataFrame de Pandas
    resultados = cursor.fetchall()
    result_dataset = pd.DataFrame(resultados, columns=["payment_method", "Total"])

    df = result_dataset.sort_values(by="Total", ascending=False).head(5)

    pandas2ri.activate()
    result_dataset_r = pandas2ri.py2rpy(df)

    # Crear la ventana de la interfaz gráfica
    ventana = tk.Tk()
    ventana.title("Gráfico de Top 5 Géneros")

    # Crear el contenedor del gráfico
    contenedor_grafico = ttk.Frame(ventana)
    contenedor_grafico.pack(padx=10, pady=10)

    # Enviar los datos al entorno R
    r.assign("df_payment", result_dataset_r)

    # Ejecutar el código R para crear el gráfico
    r('''
    barplot(df_payment$Total, names.arg = df_payment$payment_method, col = "red",
            main = "Top 5 Metodos de Pago", xlab = "payment_method", ylab = "Total")
    ''')

    # Botón para cerrar la ventana
    boton_cerrar = ttk.Button(ventana, text="Cerrar", command=ventana.destroy)
    boton_cerrar.pack(pady=10)

    # Iniciar el bucle principal de la interfaz gráfica
    ventana.mainloop()
# Crear la ventana principal
root = tk.Tk()
root.title("Visualizador de Gráficos")

# Aplicar estilo a la ventana principal
style = ThemedStyle(root)
style.set_theme("arc")  # Puedes probar diferentes temas como "aquativo", "blue", "elegance", etc.

# Aplicar estilo a los botones
style.configure("TButton", padding=(10, 5, 10, 5), font=('Arial', 12))

# Botón para mostrar la gráfica
boton_mostrar_grafica = ttk.Button(root, text="Mostrar Gráfica", command=mostrar_grafica)
boton_mostrar_grafica.pack(pady=20)

# Botón para mostrar la gráfica de géneros
boton_grafica_genero = ttk.Button(root, text="Gráfico de Géneros", command=mostrar_grafica_genero)
boton_grafica_genero.pack(pady=10)
# Botón para mostrar la gráfica de metodos de pago
boton_grafica_payment = ttk.Button(root, text="Gráfico de Metodos de pago", command=mostrar_grafica_payment)
boton_grafica_payment.pack(pady=10)
# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
