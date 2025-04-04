GUÍA DE INSTALACIÓN Y EJECUCIÓN - ENTREGA 2
===========================================

REQUISITOS DEL SISTEMA
----------------------
• Python 3.8 o superior
• Git (opcional, solo para clonar)
• Sistemas compatibles:
  - Windows 10/11 (64-bit)
  - macOS 10.15+
  - Linux (Ubuntu 20.04+, Fedora 32+)

1. OBTENER EL CÓDIGO FUENTE
---------------------------
Opción recomendada (Git):
   git clone https://github.com/EForloni/SeminarioPython.git
   cd SeminarioPython

Opción alternativa (descarga manual):
   1. Visitar https://github.com/EForloni/SeminarioPython
   2. Hacer clic en "Code" → "Download ZIP"
   3. Extraer el archivo ZIP
   4. Abrir carpeta en terminal

2. CONFIGURACIÓN DEL ENTORNO
---------------------------
Windows:
   python -m venv venv
   .\venv\Scripts\activate

macOS/Linux:
   python3 -m venv venv
   source venv/bin/activate

3. INSTALACIÓN DE DEPENDENCIAS
-----------------------------
   pip install notebook

4. EJECUCIÓN DEL PROYECTO
-------------------------
Opción A (Jupyter Notebook - recomendada):
   jupyter notebook
   • Navegar a: notebooks/Entrega2.ipynb
   • En el menú superior: Kernel → Restart & Run All

Opción B (Ejecución directa):
   cd src
   python Entrega2.py
