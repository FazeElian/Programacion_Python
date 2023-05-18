import tkinter as tk
from tkinter import ttk

#Importación de menú
import menu as menu

#Creación ventana principal
indexTodos_los_comps = tk.Tk()
indexTodos_los_comps.title("Tienda Online | Todos los computadores") #Titulo de ventana
# indexTodos_los_comps.geometry("1580x720") #Tamaño de ventana
indexTodos_los_comps.attributes('-fullscreen',True) #Ventana en pantalla completa
indexTodos_los_comps.configure(bg="gray") #Color de fondo de ventana

#Contenido de ventana principal
#Texto presentación Página Principal
encuentre_aqui = tk.Label(indexTodos_los_comps, text="Encuentra aquí tu nuevo computador!")
encuentre_aqui.configure(bg="gray")
encuentre_aqui.grid(row=0, column=1, pady=40, padx=10)