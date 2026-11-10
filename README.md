# Material de apoyo — Informática General (IG)

Esta carpeta reúne las fuentes HTML editables de los materiales de apoyo de la cátedra Informática General, sus documentos públicos y la documentación para mantenerlos. Los HTML se distribuyen también como PDF cuando corresponde.

## Organización y descubrimiento de archivos

Los documentos públicos se identifican por el patrón `IG.A.NN_Titulo_del_documento_vX.Y.html`.

- `IG`: Informática General.
- `A`: material de apoyo.
- `NN`: código correlativo de dos dígitos, incluido `00`.
- `Titulo_del_documento`: descripción breve, sin espacios ni tildes en el nombre del archivo.
- `vX.Y`: versión académica publicada.

Para conocer los materiales disponibles, enumerar los archivos que coincidan con ese patrón y consultar el pertinente por su código, título y contenido. No mantener aquí un inventario de documentos ni depender de sus nombres completos o versiones para trabajar con ellos.

`IG.A.00` es un documento público de presentación de la colección, destinado a estudiantes. No es una plantilla técnica y nunca debe utilizarse como base para crear otro material.

La plantilla técnica vigente es `_IG.A.NN_Plantilla_Material_de_Apoyo_EDITABLE.html`. El guion bajo inicial y el marcador `NN` la distinguen de los documentos públicos; su ausencia de sufijo de versión publicada confirma su carácter técnico. Para localizarla, considerar además su finalidad y las palabras `Plantilla` y `EDITABLE`; si no hay exactamente una plantilla identificable, no se debe elegir un documento público como sustituto.

## Protocolo de construcción

1. Identificar los códigos públicos existentes y determinar el próximo `NN` disponible, sin suponer una cantidad fija de documentos.
2. Localizar la plantilla técnica y duplicarla; nunca sobrescribirla ni usar `IG.A.00` público como plantilla.
3. Nombrar el nuevo HTML como `IG.A.NN_Titulo_del_documento_vX.Y.html` y usar el mismo nombre base para el PDF distribuido.
4. Completar título, subtítulo, tipo de material y desarrollo académico. Conservar solo los componentes necesarios: secciones, subsecciones, figuras con epígrafe, tablas, bloques destacados, código y referencias.
5. Revisar precisión conceptual, redacción y ejemplos ejecutables. Distinguir claramente entre reglas específicas de IG y características generales de Python.
6. Sincronizar metadatos, encabezado visible, pie de pantalla y encabezados/pies de impresión CSS (`@page`).
7. Previsualizar en navegador y, cuando se solicite, generar un PDF A4. Publicarlo únicamente después de la revisión de la coordinación.

## Identificación, referencias y versiones

Cada documento debe mostrar su propio código, versión, fecha y hora de última modificación, especialmente en el pie de todas las páginas del PDF.

- `v1.0`: primera publicación oficial.
- `v1.1`, `v1.2`…: correcciones o ampliaciones menores.
- `v2.0`…: modificaciones importantes de contenido o estructura.
- La fecha y hora visibles usan `DD/MM/AAAA — HH:MM h`; los metadatos HTML usan ISO 8601 con zona horaria de Argentina (`-03:00`). No inventar marcas de tiempo.

Al mencionar otro material, usar su código y, si ayuda a la comprensión, una denominación estable. No incluir versiones, nombres de archivo ni referencias que obliguen a actualizar documentos ya publicados cuando aparezca una edición nueva. Las referencias académicas necesarias para comprender el contenido sí deben conservarse.

No incrementar una versión por un ajuste meramente técnico de referencias externas, salvo que la coordinación indique lo contrario. Mantener la correlación con el PDF publicado.

## Identidad visual e impresión

La plantilla técnica contiene la marca IG, el logotipo UCA embebido, el azul institucional y los estilos para títulos, código, tablas, imágenes y recuadros. Todo documento público debe ser autónomo: no depender de imágenes, CSS, tipografías ni scripts externos.

Preservar `@media print`, `@page`, `@page :first`, márgenes A4, encabezados, pies y numeración, salvo pedido explícito. Para imprimir desde Chrome o Edge: A4, escala 100 %, gráficos de fondo activados y encabezados/pies automáticos del navegador desactivados.

El PDF debe conservar una primera página con identificación institucional completa, cabecera compacta en las posteriores y un pie repetido con identidad de IG, código, versión, fecha/hora y numeración. Comprobar legibilidad, márgenes, saltos de página, tablas, figuras y código en todas las páginas.

## Trabajo con Codex

Antes de crear, corregir o exportar, Codex debe leer `AGENTS.md`, identificar los archivos existentes y abrir los documentos pertinentes a la tarea. Puede preparar cambios y revisiones técnicas, pero no debe cambiar contenidos ni criterios académicos aprobados sin una instrucción expresa.

En una auditoría, no modificar archivos salvo que se solicite la corrección. En una edición académica, limitarse a lo autorizado. En una edición visual, conservar el texto académico y evitar reformateos masivos innecesarios.

## Código descargable y repositorio único

Esta misma carpeta es la raíz prevista del único repositorio del proyecto. Los ejemplos descargables se organizan en `CODIGOS/IG.A.NN/`; cada archivo se identifica como `IG.A.NN_EXXX_TIPO.py`, sin incorporar la versión del documento. Los tipos son `NO_ADMITIDO`, `FORMA_ESPERADA` y, cuando corresponda, `ALTERNATIVA`.

El HTML académico es la fuente del contenido: los archivos `.py` se derivan de sus bloques `pre`, no los reinterpretan ni los sustituyen. `manifest.json` registra código documental, ejemplo, variante, ubicación, procedencia, hash y enlaces; `configuracion_publicacion.json` centraliza la configuración pública sin credenciales. Las utilidades de `herramientas/` permiten extraer, validar y preparar enlaces.

Para un documento que contenga ejemplos, verificar primero sin escribir:

```text
python herramientas/extraer_codigos.py --manifest manifest.json --root . --html IG.A.NN_Titulo_del_documento_vX.Y.html --document-code IG.A.NN
python herramientas/validar_codigos.py --manifest manifest.json --root . --html IG.A.NN_Titulo_del_documento_vX.Y.html --document-code IG.A.NN
python herramientas/validar_enlaces.py --manifest manifest.json --config configuracion_publicacion.json --root .
```

Solo después de una publicación autorizada y una descarga verificada se completan los enlaces del manifiesto. Para producir una copia con enlaces, usar `actualizar_enlaces_html.py`; no insertar URLs directamente en un HTML académico aprobado ni sobrescribir el original. La copia y su PDF son artefactos de prueba y no modifican la versión ni los metadatos del documento público.

Antes de cualquier commit o publicación, ejecutar `herramientas/preparar_publicacion.py` y revisar el alcance. No mover, eliminar ni renombrar un `.py` ya referenciado por un PDF sin autorización explícita. El historial Git es el mecanismo de seguimiento técnico; las rutas estables no dependen de futuras versiones de los PDF.

---

**Cátedra Informática General — Coordinación**
