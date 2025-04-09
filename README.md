# Reconocimiento de dígitos

El propósito es desarrollar un sistema de reconocimiento de dígitos basado en un modelo de red neuronal convolucional

[HERE IS A DEMO VIDEO](https://tajamar365-my.sharepoint.com/:v:/p/tsuenkit_lui/EeiO3d15F8FOnlQux01i8JoBB-kSni4WAOC1HJC6XqvGvA?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=RRYtAs)

Puedes pinchar en el link anterior para ver cómo funciona

## Estructura del proyecto

```
diigit-recognition/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── script.js
└── requirements.txt
```

**Contiene notebooks para ver paso a paso la creación del modelo de distintas maneras.** 

## Requisitos

Antes de ejecutar la aplicación, asegúrate de tener instalado:

- Python 3.7 o superior
- pip (el gestor de paquetes de Python)

## Despliegue

Este proyecto es una aplicación web simple construida con Flask. El archivo principal de la aplicación es `app.py`.

1. **Clona este repositorio:**

```bash
git clone https://github.com/TsuenKitTajamar/digit-recognition
cd digit-recognition
```

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

3. **Ejecutar la aplicación:**
```bash
python app.py
```

La aplicación se ejecutará por defecto en http://127.0.0.1:5000