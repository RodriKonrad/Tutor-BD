# Tutor-BD
Este proyecto contiene una implementación la Inteligencia Artificial de Google utilizando el nuevo SDK de segunda generación (`google-genai`) para un tutor de bases de datos.

## 🛠️ Requisitos Previos

Antes de comenzar, asegúrate de tener:
* Instalado **Python 3.10 o superior**
* Una **API Key** de Google AI Studio. Puedes obtenerla en [aistudio.google.com](https://aistudio.google.com/).

## 🚀 Configuración del Entorno

Sigue estos pasos para ejecutar el código en tu máquina local:

### 1. Clonar el repositorio
### 2. Abrir una terminal (en VS Code: ctrl + ñ)
### 3. Crear y activar un entorno virtual
En Windows:

```bash
python -m venv venv
```
```bash
.\venv\Scripts\activate
```
En macOS/Linux:
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```
### 5. Configurar variables de entorno
Crea un archivo llamado .env en la raíz del proyecto y añade tu API Key Google AI Studio de la siguiente manera:
```bash
GEMINI_API_KEY=tu_clave_secreta_aqui
```
## 💻 Uso
Para ejecutar el script principal de conexión:

```bash
python run.py
```
## 🗒️ Anotaciones EXTRA
*  **Para crear o actualizar el `requirements.txt`:** Ejecuta este comando en tu terminal (con el entorno activado) para que el archivo de texto se genere automáticamente:
    ```bash
    pip freeze > requirements.txt
    ```
## ✅ Ejemplo de ejecución
<img width="1302" height="701" alt="imagen" src="https://github.com/user-attachments/assets/32b3779b-a3be-4382-875c-3564273bcc66" />
