import tkinter as tk
from tkinter import messagebox

class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Lista de tareas
        self.tasks = []

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(pady=10)
        self.task_entry.bind('<Return>', self.add_task)  # Presionar Enter añade una tarea

        # Botones
        self.add_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(self.root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Listbox para mostrar tareas
        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Vincular doble clic en una tarea para marcarla como completada
        self.task_listbox.bind('<Double-Button-1>', self.complete_task)

    # Función para añadir una tarea
    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada Vacía", "Por favor ingresa una tarea.")

    # Función para marcar una tarea como completada
    def complete_task(self, event=None):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_index]
            self.tasks[selected_index] = f"{task} (Completada)"
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Selección Inválida", "Por favor selecciona una tarea para marcar como completada.")

    # Función para eliminar una tarea
    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Selección Inválida", "Por favor selecciona una tarea para eliminar.")

    # Actualizar la lista de tareas en el Listbox
    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)  # Limpia la lista
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

# Crear la ventana principal
root = tk.Tk()
app = TaskApp(root)
root.mainloop()
