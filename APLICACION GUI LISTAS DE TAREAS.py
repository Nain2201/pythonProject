import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        self.tasks = []

        # Crear la interfaz gráfica
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.grid(row=1, column=0, padx=10, pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=1, column=1, padx=5, pady=5)

        self.task_listbox = tk.Listbox(root, width=60)
        self.task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.task_entry.bind("<Return>", self.add_task_enter)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una tarea.")

    def add_task_enter(self, event):
        self.add_task()

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.task_listbox.itemconfig(task_index, {'bg': 'light green'})
        else:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para marcar como completada.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.task_listbox.delete(task_index)
            del self.tasks[task_index]
        else:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
