



import tkinter as tk
from leerArchivos.leer import seleccionar_archivo

#Crear la ventana inicial
root = tk.Tk()
root.title("Calcular media, mediana y moda de números"); 
root.geometry("400x300")
root.configure(bg="#f0f0f0")
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')

#Boton para cargar un archivo
label = tk.Label(root, text="Seleccione un archivo para calcular la media, mediana y moda:", bg="#f0f0f0", font=("Arial", 10))
label.pack(pady=20)
button = tk.Button(root, text="Cargar archivo", bg="#4CAF50", fg="white", font=("Arial", 12), padx=10, pady=5, command=seleccionar_archivo)
button.pack(pady=20)

root.mainloop()
