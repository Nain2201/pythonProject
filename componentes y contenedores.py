import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        self.eventos = []

        self.frame_lista = ttk.Frame(self.root)
        self.frame_lista.pack(pady=10)

        self.treeview = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), selectmode="extended")
        self.treeview.heading("#0", text="ID")
        self.treeview.heading("Fecha", text="Fecha")
        self.treeview.heading("Hora", text="Hora")
        self.treeview.heading("Descripción", text="Descripción")
        self.treeview.pack()

        self.frame_datos = ttk.Frame(self.root)
        self.frame_datos.pack(pady=10)

        ttk.Label(self.frame_datos, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_fecha = ttk.Entry(self.frame_datos)
        self.entry_fecha.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.frame_datos, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_hora = ttk.Entry(self.frame_datos)
        self.entry_hora.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.frame_datos, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_descripcion = ttk.Entry(self.frame_datos)
        self.entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

        self.btn_agregar = ttk.Button(self.frame_datos, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.btn_eliminar = ttk.Button(self.root, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.btn_eliminar.pack(pady=10)

        self.btn_salir = ttk.Button(self.root, text="Salir", command=self.root.quit)
        self.btn_salir.pack(pady=10)

    def agregar_evento(self):
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        descripcion = self.entry_descripcion.get()

        if fecha and hora and descripcion:
            evento = (fecha, hora, descripcion)
            self.eventos.append(evento)
            self.actualizar_lista_eventos()
            self.limpiar_campos()
        else:
            messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos.")

    def actualizar_lista_eventos(self):
        self.treeview.delete(*self.treeview.get_children())
        for idx, evento in enumerate(self.eventos, start=1):
            self.treeview.insert("", "end", text=str(idx), values=evento)

    def limpiar_campos(self):
        self.entry_fecha.delete(0, tk.END)
        self.entry_hora.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)

    def eliminar_evento(self):
        seleccionados = self.treeview.selection()
        if seleccionados:
            confirmacion = messagebox.askyesno("Eliminar Evento", "¿Está seguro que desea eliminar el evento seleccionado?")
            if confirmacion:
                for seleccionado in seleccionados:
                    item = self.treeview.item(seleccionado)
                    idx = int(item["text"]) - 1
                    del self.eventos[idx]
                self.actualizar_lista_eventos()
        else:
            messagebox.showwarning("Sin selección", "Por favor seleccione un evento para eliminar.")

root = tk.Tk()
app = AgendaApp(root)
root.mainloop()