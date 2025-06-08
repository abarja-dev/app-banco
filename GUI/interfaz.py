"""
Módulo con Tkinter que crea una interfaz gráfica que simula un cajero
"""


import tkinter as tk
from tkinter import messagebox
from src.clases import Cliente


# Clase con la pantalla de inicio de "cajero" donde damos la bienvenida y pedimos sus datos al cliente
class PantallaInicio:
    def __init__(self, master):
        self.master = master
        self.master.title("Banco Plutón - Inicio")
        self.master.geometry("400x300")
        self.master.configure(bg='#f0f0f0')

        self.frame = tk.Frame(master, bg='#f0f0f0')
        self.frame.pack(expand=True)

        tk.Label(self.frame, text='Bienvenido a Banco Plutón', font=('Helvetica', 16), bg='#f0f0f0').pack(pady=10)

        tk.Label(self.frame, text='Nombre:', bg='#f0f0f0').pack()
        self.entry_nombre = tk.Entry(self.frame)
        self.entry_nombre.pack()

        tk.Label(self.frame, text='Apellido:', bg='#f0f0f0').pack()
        self.entry_apellido = tk.Entry(self.frame)
        self.entry_apellido.pack()

        tk.Label(self.frame, text='Número de cuenta:', bg='#f0f0f0').pack()
        self.entry_cuenta = tk.Entry(self.frame)
        self.entry_cuenta.pack()

        tk.Button(self.frame, text='Ingresar', command=self.crear_cliente).pack(pady=10)

    # Metodo para crear el cliente
    def crear_cliente(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        cuenta = self.entry_cuenta.get()

        if not nombre or not apellido or not cuenta:
            messagebox.showerror('Error', 'Por favor, completa todos los campos.')
            return

        # A efectos del ejercicio creamos al cliente con un saldo inicial de 5000
        cliente = Cliente(nombre, apellido, cuenta, 5000)
        self.master.withdraw()
        abrir_menu_principal(cliente)

# Clase con el menú principal, y los metodos que nos permitiran realizar las operaciones
class MenuPrincipal:
    def __init__(self, cliente):
        self.cliente = cliente
        self.root = tk.Toplevel()
        self.root.title('Banco Plutón - Cajero')
        self.root.geometry('400x350')
        self.root.configure(bg='#e6f2ff')

        tk.Label(self.root, text=f"Bienvenido, {cliente.nombre} {cliente.apellido}", font=("Helvetica", 14),
                 bg="#e6f2ff").pack(pady=20)
        tk.Label(self.root, text=f"Cuenta: {cliente.numero_cuenta}", bg="#e6f2ff").pack()
        self.label_saldo = tk.Label(self.root, text=f"Saldo actual: {cliente.balance:,.2f} €", bg="#e6f2ff")
        self.label_saldo.pack(pady=(0, 10))

        # Botones de las operaciones
        tk.Button(self.root, text='Ingresar dinero', width=25, command=self.ingresar).pack(pady=5)
        tk.Button(self.root, text="Retirar dinero", width=25, command=self.retirar).pack(pady=5)
        tk.Button(self.root, text="Ver historial", width=25, command=self.ver_historial).pack(pady=5)
        tk.Button(self.root, text="Salir", width=25, command=self.root.quit).pack(pady=20)


    def ingresar(self):
        pedir_monto(self.cliente, operacion='depositar', on_update=self.actualizar_saldo)

    def retirar(self):
        pedir_monto(self.cliente, operacion='retirar', on_update=self.actualizar_saldo)

    def ver_historial(self):
        historial = self.cliente.historial
        if not historial:
            messagebox.showinfo('Historial', 'No hay movimientos todavía')
            return

        ventana = tk.Toplevel(self.root)
        ventana.title('Historial de movimientos')

        for fecha, tipo, monto in historial:
            texto = f'{fecha.strftime("%d-%m-%Y %H:%M:%S")} - {tipo}: {monto} €'
            tk.Label(ventana, text=texto).pack(anchor='w')

    def actualizar_saldo(self):
        self.label_saldo.config(text=f"Saldo actual: {self.cliente.balance:,.2f} €")

# Función que abre una nueva ventana para solicitar un número float para las operaciones
def pedir_monto(cliente, operacion, on_update=None):
    def procesar():
        entrada = entry.get()
        try:
            cantidad = float(entrada)
            if cantidad <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror('Error', 'Por favor ingresa una cantidad válida y positiva.')
            return

        if operacion == 'depositar':
            cliente.depositar(cantidad)
            messagebox.showinfo('Éxito', 'Depósito realizado correctamente.')
        elif operacion == 'retirar':
            exito = cliente.retirar(cantidad)
            if exito:
                messagebox.showinfo('Éxito', 'Retiro realizado correctamente.')
            else:
                messagebox.showwarning('Error', 'Saldo insuficiente.')

        if on_update:
            on_update()

        ventana.destroy()

    ventana = tk.Toplevel()
    ventana.title(f'{operacion.capitalize()} dinero')

    tk.Label(ventana, text=f'¿Cuánto deseas {operacion}?').pack(pady=10)
    entry = tk.Entry(ventana)
    entry.pack()
    tk.Button(ventana, text='Aceptar', command=procesar).pack(pady=5)

# Metodo que abre el menú principal
def abrir_menu_principal(cliente):
    MenuPrincipal(cliente)

if __name__ == '__main__':
    root = tk.Tk()
    app = PantallaInicio(root)
    root.mainloop()

