# App de un cajero bancario

Aplicación bancaria sencilla para gestionar operaciones básicas (ingresar, retirar dinero y ver el historial),
con interfaz gráfica en Tkinter y versión consola.

---

## Descripción

Esta aplicación simula un cajero automático que permite al usuario crear un cliente con un saldo inicial, y luego 
realizar depósitos, retiros y consultar el historial de movimientos, tanto desde la consola como desde una interfaz
gráfica.

---

## Características

- Crear cliente con datos personales y saldo inicial.
- Operaciones de ingreso y retiro de dinero.
- Visualización del saldo actualizado en tiempo real.
- Historial completo de movimientos con fecha y hora.
- Interfaz gráfica con Tkinter y versión de consola para uso alternativo.
- Manejo básico de errores y validaciones.

---

## Tecnologías usadas y requisitos

- Python 3.8 o superior
- Tkinter para la interfaz gráfica

---

## Estructura del proyecto

app-banco/
│
├── GUI/
│ └── interfaz.py # Interfaz gráfica con Tkinter
├── src/
│ ├── __init__.py
│ ├── clases.py # Modelo Cliente y lógica
│ ├── funciones.py # Funciones auxiliares y consola
│ └── main.py # Programa principal consola
├── tests/
│ ├── test_cliente.py # Tests unitarios para clase Cliente
│ └── test_funciones_auxiliares.py
├── README.md
├── LICENSE
└── .gitignore

---

## Configuración y ejecución

Para evitar problemas con importaciones y ejecución, sigue estos pasos:

1. Clona el repositorio y abre la carpeta raíz ('app-banco') como proyecto en tu IDE preferido.
2. Marca la carpeta 'app-banco' como **Source Root** (o equivalente en tu IDE)
3. Ejecuta desde la raíz del proyecto en consola:
    
   - Para ejecutar la versión en consola:
    
   ```bash
    python -m src.main
    ```
   - Para ejecutar la versión gráfica (Tkinter):
    
   ```bash
   python -m GUI.interfaz
   ```

---

## Uso de la aplicación

- En consola, sigue las indicaciones del menú para retirar, ingresar o ver el historial.
- En la interfaz gráfica, ingresa los datos del cliente, luego opera con los botones para ingresar o retirar dinero, y 
  consulta el historial en cualquier momento.

---

## Tests

Los tests unitarios están en la carpeta 'tests'. Puedes ejecutarlos con:

```bash
python -m unittest discover tests
```

---

## Autor

Alberto Barja Montes

