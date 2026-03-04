# Flask app con Blueprints y Jinja

Estructura mínima creada:

- `app/` - paquete de la aplicación
  - `main` - blueprint principal (rutas de ejemplo)
  - `auth` - blueprint de autenticación (login de ejemplo)
  - `templates/` - plantillas Jinja
  - `static/` - archivos estáticos (CSS)

Arrancar localmente:

```powershell
python run.py
# o
set FLASK_APP=run.py
flask run
```
