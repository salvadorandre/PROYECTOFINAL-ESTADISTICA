import re
import pdfplumber
from docx import Document
from tkinter import filedialog, messagebox
import statistics
import math
import matplotlib.pyplot as plt
def extraer_numeros(texto):
    return re.findall(r'\d+\.?\d*', texto)

def leer_pdf(ruta):
    texto = ""
    # Lógica para leer archivos PDF
    with pdfplumber.open(ruta) as pdf: 
        for pagina in pdf.pages:
            texto += pagina.extract_text() + "\n"
    return texto

def leer_word(ruta): 
    doc = Document(ruta)
    texto = ""; 
    for p in doc.paragraphs: 
        texto += p.text + "\n"
    return texto

def leer_txt(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()
    return texto

def leer_archivo(ruta): 
    if(ruta.endswith('.pdf')):
        return leer_pdf(ruta)
    elif(ruta.endswith('.txt')):
        return leer_txt(ruta)
    elif(ruta.endswith('.docx')):
        return leer_word(ruta)
    else:
        return ""

def seleccionar_archivo():
    ruta = filedialog.askopenfilename(title="seleccionar el archivo", filetypes=[
        ("Documentos", "*.pdf *.txt *.docx *.xlsx *.xls"),
        ("Todos los archivos", "*.*")
    ]);
    if ruta:
        texto = leer_archivo(ruta)
        numeros = extraer_numeros(texto); 
        if not numeros: 
            messagebox.showwarning("Advertencia", "No se encontraron números en el archivo.")
            return
    
    #calculos estadisticos 
    media = statistics.mean(map(float, numeros))
    mediana = statistics.median(map(float, numeros))
    try: 
        moda = statistics.mode(map(float, numeros))
    except statistics.StatisticsError:
        moda = "No hay moda única"
    varianza = statistics.variance(map(float, numeros)) if len(numeros) > 1 else 0
    desviacion = statistics.stdev(map(float, numeros)) if len(numeros) > 1 else 0
    n = len(numeros)
    rango = max(map(float, numeros)) - min(map(float, numeros))
    intervalos = round(1 + 3.322 * math.log10(n))

    amplitud = math.ceil(rango / intervalos)

    intervalos_tabla = []
    limite_inferior = min(map(float, numeros))

    for i in range(intervalos): 
        limite_superior = limite_inferior + amplitud
        intervalos_tabla.append((limite_inferior, limite_superior))
        limite_inferior = limite_superior
    
    frecuencias = []
    for li, ls in intervalos_tabla: 
        count = sum(1 for x in numeros if li <= float(x) < ls)
        frecuencias.append(count)

    #histograma
    plt.hist(numeros, bins=intervalos, color="blue", edgecolor="skyblue")
    plt.title('Histograma de Números')
    plt.xlabel('rangos')
    plt.ylabel('Frecuencia')
    plt.show()
    resultados = f"Resultados:\n\nMedia: {media}\nMediana: {mediana}\nModa: {moda}\nVarianza: {varianza}\nDesviación estándar: {desviacion}\n Número de intervalos: {intervalos}\nAmplitud de los intervalos: {amplitud}\n"
    messagebox.showinfo("Resultados", resultados)
