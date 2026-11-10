# Código descargable — Informática General (IG)

Este repositorio público contiene únicamente archivos de código asociados a materiales de apoyo de Informática General de la UCA y las herramientas necesarias para administrarlos.

## Organización

- Cada directorio `IG.A.NN/` contiene código del documento indicado por ese código.
- Los archivos siguen `IG.A.NN_EXXX_TIPO.py`, donde `TIPO` es `ESPERADO`, `NO_ADMITIDO` o `ALTERNATIVA`.
- `manifest.json` es la fuente central de metadatos, rutas, clasificación, procedencia y enlaces publicados.
- `configuracion_publicacion.json` define los datos de publicación y las plantillas de enlaces, sin credenciales.
- `herramientas/` contiene utilidades genéricas para extracción, validación y actualización de enlaces.

No se crean directorios para documentos que no aportan código. Los nombres no incluyen la versión de un PDF: Git conserva el historial de cambios y los archivos permanecen en la misma ruta mientras estén publicados.

## Flujo local

1. Agregar o actualizar las entradas pertinentes de `manifest.json`.
2. Extraer los bloques desde el HTML académico con `herramientas/extraer_codigos.py`.
3. Validar nombres, UTF-8, tabulaciones, sintaxis y correspondencia con el HTML mediante `herramientas/validar_codigos.py`.
4. Incorporar los enlaces públicos al manifiesto solo después de publicar y comprobarlos.
5. Usar `herramientas/actualizar_enlaces_html.py` para generar una copia HTML con enlaces; nunca insertar URLs manualmente en documentos aprobados.
6. Ejecutar `herramientas/validar_enlaces.py` y luego generar el PDF desde esa copia con Chrome.
7. Antes de un commit autorizado, revisar el informe de `herramientas/preparar_publicacion.py`; la herramienta no crea commits ni publica.

Ejemplo de validación local, con rutas relativas al lugar donde se ejecuta:

```text
python herramientas/validar_codigos.py --manifest manifest.json --root . --html ../Material\ de\ apoyo\ IG/IG.A.02_Criterios_programacion_estructurada_v1.3.html
python herramientas/validar_enlaces.py --manifest manifest.json --config configuracion_publicacion.json --root .
```

## Publicación y mantenimiento

No publicar, eliminar ni renombrar archivos que puedan estar referenciados por un PDF sin autorización académica. Antes de un `git push`, revisar las validaciones, el manifiesto y el alcance del cambio. El repositorio no debe incluir evaluaciones, soluciones restringidas, información personal ni credenciales.

La estrategia de descarga de GitHub queda pendiente de una prueba real: una URL RAW puede mostrar el código en vez de descargarlo, según el navegador. No se configura un enlace de descarga hasta confirmar el nombre y los bytes obtenidos.
