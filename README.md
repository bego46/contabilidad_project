# 📊 Contabilidad Project

## 🔹 Descripción
Este proyecto es un **sistema de contabilidad personal** desarrollado en **Python y PyQt** con una arquitectura modular separada en **backend** y **frontend**. Permite el registro de ingresos y gastos, análisis de datos y generación de reportes.

## 🔹 Estructura del Proyecto
```
📂 contabilidad_project/
 ├── 📂 backend/        # Lógica y procesamiento de datos
 │    ├── db_manager.py      # Gestión de la base de datos SQLite
 │    ├── models.py          # Definición de las clases y estructuras de datos
 │    ├── calculations.py    # Funciones para cálculos financieros
 │    ├── report_generator.py # Generación de reportes en PDF/Excel
 │    ├── api.py             # Opcional: API para comunicar Frontend y Backend
 │    └── __init__.py        # Inicialización del módulo
 │
 ├── 📂 frontend/       # Interfaz gráfica con PyQt
 │    ├── main.py           # Punto de entrada de la aplicación
 │    ├── ui_main.py        # Diseño de la pantalla principal
 │    ├── ui_register.py    # Diseño de la pantalla de registro de transacciones
 │    ├── ui_history.py     # Diseño de la pantalla de historial con filtros
 │    ├── ui_reports.py     # Pantalla para generación de reportes
 │    ├── assets/           # Íconos y recursos visuales
 │    └── __init__.py       # Inicialización del módulo
 │
 ├── 📂 .venv/           # Entorno virtual
 ├── requirements.txt   # Librerías necesarias
 ├── README.md         # Documentación del proyecto
```

## 🔹 Características
✅ **Registro de transacciones** con ingreso y gasto.  
✅ **Historial detallado** con filtros por fecha y categoría.  
✅ **Gráficos financieros** interactivos con Matplotlib.  
✅ **Generación de reportes** en PDF y exportación a Excel.  
✅ **Base de datos SQLite** para almacenamiento eficiente.  

## 🔹 Instalación
### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tuusuario/contabilidad_project.git
cd contabilidad_project
```

### 2️⃣ Configurar el entorno virtual
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### 3️⃣ Ejecutar la aplicación
```bash
python frontend/main.py
```

## 🔹 Librerías utilizadas
- `PyQt6` → Interfaz gráfica.  
- `sqlite3` → Base de datos.  
- `pandas` → Manejo de datos.  
- `matplotlib` → Gráficos financieros.  
- `reportlab` → Generación de reportes en PDF.  

## 🔹 Autores
Desarrollado por **Developments Berlad (&lt;DB/&gt;)** 🚀  

## 🔹 Licencia
🔒 Este proyecto está protegido por derechos de autor. El código contenido aquí no puede ser copiado, modificado ni reutilizado sin autorización de **Developments Berlad (&lt;DB/&gt;)**.

## 🔹 Contacto
* 💼 LinkedIn: [https://www.linkedin.com/in/berladgonzalez/](https://www.linkedin.com/in/berladgonzalez/)
* 📧 Email: [berlad46@gmail.com](mailto:berlad46@gmail.com)
* 🌐 Sitio web: Próximamente



