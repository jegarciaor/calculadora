# Librerías externas.
from cx_Freeze import setup, Executable

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

# Archivos a incluir.
include_files = ['img/']

# Paquetes a incluir.
packages = [
    'calculadora', 'calculadora.python', 'calculadora.python.front_calculadora',
    'calculadora.python.metadata']

setup(
    name='Proyecto Calculadora',
    version='1.0.0',
    author='Jefferson Andrés García Ortiz',
    author_email='jefferson.garciaor@gmail.com',
    url='https://github.com/jegarciaor/proyecto_calculadora.git',
    options={'build_exe': {
        'packages': packages,
        'include_files': include_files}
    },
    executables=[Executable('run.py',
                            base="Win32GUI",
                            icon='img/calculator_icon.ico')],
)
