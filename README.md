# 📦 Sistema Simple de Inventario

## 📖 Descripción

Este proyecto consiste en un programa en **Python** que permite registrar un producto dentro de un inventario simple.
El usuario puede ingresar el **nombre del producto, el precio y la cantidad disponible**, y el sistema calculará automáticamente el **costo total**.

Además, el programa incluye **validación de datos** para evitar errores en la entrada del usuario.

---

## ⚙️ Funcionalidades

* Solicita el **nombre del producto**.
* Solicita el **precio del producto**.
* Solicita la **cantidad disponible**.
* Valida que:

  * El precio sea un número válido.
  * El precio no sea negativo.
  * La cantidad sea un número entero.
  * La cantidad no sea negativa.
* Calcula el **costo total del producto**.
* Muestra un **resumen final con los datos ingresados**.

---

## 🧮 Fórmula utilizada

```
Costo Total = Precio × Cantidad
```

---

## 🖥️ Tecnologías utilizadas

* Python 3
* Estructuras utilizadas:

  * `while`
  * `try / except`
  * `input()`
  * `float()` y `int()`
  * `f-strings`

---

## ▶️ Cómo ejecutar el proyecto

1. Clona este repositorio o descarga el archivo.
2. Asegúrate de tener **Python 3** instalado.
3. Ejecuta el archivo desde la terminal:

```bash
python inventario.py
```

4. Ingresa los datos solicitados por el sistema.

---

## 💡 Ejemplo de ejecución

```
=== Sistema simple de inventario ===

Ingrese el nombre del producto: Laptop
Ingrese el precio del producto: 2500
Ingrese la cantidad: 3

=== Resultado ===
Producto: Laptop | Precio: 2500.0 | Cantidad: 3 | Total: 7500.0
```

---

## 🛡️ Validaciones del sistema

El programa evita errores como:

* Ingresar texto en lugar de números.
* Ingresar precios negativos.
* Ingresar cantidades negativas.

En estos casos, el sistema solicitará nuevamente el dato correcto.

---

## 🚀 Posibles mejoras

Algunas mejoras futuras para el proyecto podrían ser:

* Permitir registrar **múltiples productos**.
* Guardar productos en **listas o diccionarios**.
* Calcular el **valor total del inventario**.
* Guardar los datos en **archivos o bases de datos**.
* Crear un **menú interactivo para el inventario**.
