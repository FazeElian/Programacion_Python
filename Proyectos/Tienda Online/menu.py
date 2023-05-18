import tkinter as tk
from tkinter import ttk

#Creación ventana principal
index = tk.Tk()
index.title("Tienda Online | Inicio") #Titulo de ventana
# index.geometry("1580x720") #Tamaño de ventana
index.attributes('-fullscreen',True) #Ventana en pantalla completa
index.configure(bg="gray") #Color de fondo de ventana

#Contenido de ventana principal
#Texto presentación Página Principal
presentacion = tk.Label(index, text="Bienvenido a nuestra Tienda Online, aquí encontrarás variedad de productos de tecnología para tu hogar!")
presentacion.configure(bg="gray")
presentacion.grid(row=0, column=1, pady=40, padx=10)

#Imagen Banner de empresa


#Creación menú superior
menu = tk.Menu()  #Tkinter de ventana de menu

#Opciones de menu
menu_inicio = tk.Menu(menu, tearoff=0)
menu_categorias = tk.Menu(menu, tearoff=0)
menu_productos = tk.Menu(menu, tearoff=0)
menu_carrito = tk.Menu(menu, tearoff=0)

#Agregar las opciones de menu
menu.add_cascade(label="Inicio", menu=menu_inicio)
menu.add_cascade(label="Categorías", menu=menu_categorias)
menu.add_cascade(label="Productos", menu=menu_productos)
menu.add_cascade(label="Carrito de Compras", menu=menu_carrito)

#Creación subopciones de Categorias
menu_categorias.add_command(label="Tecnología")

menu_categorias.add_command(label="Electrodomésticos")
menu_categorias.add_command(label="Computadores")
menu_categorias.add_command(label="Celulares")
menu_categorias.add_command(label="Periféricos")
menu_categorias.add_command(label="Monitores")
menu_categorias.add_command(label="Memorias USB")
menu_categorias.add_command(label="Tarjetas SD")

#Creación subopciones de Productos
menu_productos.add_command(label="Mis productos")
menu_productos.add_command(label="Mis Compras")
menu_productos.add_command(label="Mis Favoritos")

#Creación subopciones de Inicio
menu_inicio.add_command(label="Mi Cuenta")
menu_inicio.add_command(label="Ajustes")
menu_inicio.add_command(label="Cerrar Sesión")

#Creación subopciones de Carrito
menu_carrito.add_command(label="Añadir productos")
menu_carrito.add_command(label="Ir a carrito de compras")
menu_carrito.add_command(label="Continuar Compra")
