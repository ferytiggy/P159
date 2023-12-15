from tkinter import *
from tkinter.messagebox import*
from PIL import ImageTk, Image

root=Tk()
root.title("Banderas de países")
root.geometry("600x400")
root.configure(background="lightblue")

get_input = Entry(root)
show_label = Label(root)

india_map = ImageTk.PhotoImage(Image.open ("India.jpg"))
america_map = ImageTk.PhotoImage(Image.open ("America.jpg"))
australia_map = ImageTk.PhotoImage(Image.open ("Australia.png"))
philippines_map = ImageTk.PhotoImage(Image.open ("Filipinas.png"))
japan_map = ImageTk.PhotoImage(Image.open ("Japon.jpg"))

maps_dictionary = { "India" : india_map , 
                    "America" : america_map ,
                    "Australia" : australia_map ,
                    "Filipinas" : philippines_map,
                    "Japon" : japan_map,}

def showMaps():
    map_name = get_input.get()
    # Añade un bloque try y except para manejar el error creado por la siguiente línea de código
    try:
        show_label['image'] = maps_dictionary[map_name]
    except:
        showinfo("Error", "No tenemos esa bandera en la base de datos")
        

btn = Button(root , text="Mostrar mapa", bg="green", command=showMaps)
get_input.place(relx=0.5, rely=0.1, anchor=CENTER)
btn.place(relx=0.5, rely=0.2, anchor=CENTER)
show_label.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()