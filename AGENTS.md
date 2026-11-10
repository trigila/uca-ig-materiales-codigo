# AGENTS.md — Material de apoyo de Informática General (IG)

## 1. Propósito y alcance

Estas instrucciones se aplican al trabajo de Codex en esta carpeta y sus subcarpetas. Aquí se mantienen fuentes HTML editables y documentos públicos que se exportan como PDF para estudiantes y docentes de Informática General (UCA, Facultad de Ingeniería y Ciencias Agrarias).

Antes de operar:

1. Leer `README.md` y las consignas o materiales proporcionados para la tarea.
2. Inspeccionar los HTML existentes. Reconocer los documentos públicos por el patrón `IG.A.NN_Titulo_del_documento_vX.Y.html` y localizar el documento pertinente por código, título y contenido; no depender de una lista fija de archivos ni de sus versiones.
3. Distinguir la plantilla técnica vigente `_IG.A.NN_Plantilla_Material_de_Apoyo_EDITABLE.html` por su finalidad, por las palabras `Plantilla` y `EDITABLE`, por su guion bajo inicial, por el marcador `NN` y porque no incluye un sufijo de versión publicada. Si no existe una única plantilla identificable, informarlo antes de crear un documento; no reutilizar un documento público como sustituto.
4. Tratar `IG.A.00` como documento público de presentación de la colección para estudiantes. Nunca es la plantilla técnica ni debe sobrescribirse para crear otro documento.

Las instrucciones explícitas del usuario tienen prioridad. No extrapolar criterios académicos de un documento a otro tema sin una indicación expresa.

## 2. Reglas no negociables

- No sobrescribir la plantilla técnica al crear documentos; duplicarla y editar la copia. Solo modificarla si el usuario lo solicita.
- Mantener la identidad visual IG/UCA: marca IG, logotipo UCA embebido, azul institucional, jerarquías de títulos, estilos de código, tablas y recuadros.
- Conservar el HTML autónomo: no depender de imágenes, CSS, tipografías ni scripts externos. Las figuras que se añadan deben incluir `alt` y epígrafe y, cuando sea necesario para distribución portátil, estar incrustadas.
- Preservar, salvo pedido explícito, `@media print`, `@page`, `@page :first`, márgenes A4, encabezados, pies y `counter(page) / counter(pages)`.
- No modificar, reinterpretar ni «mejorar» unilateralmente contenidos académicos, consignas o restricciones didácticas aprobadas. Si se detecta un error conceptual, informarlo y proponer la corrección por separado.
- No afirmar que un HTML o PDF fue probado si no se realizaron pruebas. No publicar ni reemplazar PDF oficiales sin autorización.

## 3. Crear un documento nuevo

1. Inspeccionar los documentos públicos existentes e identificar el próximo número disponible `NN`; no suponer un inventario ni una cantidad fija de publicaciones.
2. Localizar la plantilla técnica y copiarla a `IG.A.NN_Titulo_del_documento_vX.Y.html`. Si falta o es ambigua, detener esa creación e informar el problema.
3. Completar la portada y sustituir los marcadores entre corchetes por el contenido solicitado.
4. Conservar solo los componentes pertinentes: párrafos, `h2`, `h3`, listas, `.destacado-bloque`, `.ig-figure`, `.ig-table`, `.ig-two-col`, `pre` y referencias. No dejar ejemplos ni marcadores ficticios en un documento terminado.
5. Mantener una estructura didáctica clara: propósito, explicación, ejemplos cuando correspondan, síntesis y fuentes. Usar español claro y no agregar afirmaciones no respaldadas por los insumos.
6. Usar nombres estables: `IG.A.NN_Titulo_del_documento_vX.Y.html` y PDF con el mismo nombre base.

## 4. Sincronización obligatoria de metadatos

Antes de dar por terminado un documento, verificar:

| Ubicación | Datos a actualizar |
| --- | --- |
| `<title>` | Identificación del tema. |
| `<meta name="document-version">` | `X.Y` (sin `v`). |
| `<meta name="last-modified">` | Fecha y hora ISO 8601. |
| `.ig-document-heading .ig-doc-code` | `IG.A.NN`. |
| `.ig-document-heading .ig-eyebrow` | Tipo de material o categoría. |
| `.ig-document-heading h1`, `.ig-lead` | Título y subtítulo reales. |
| `.ig-metadata` | Versión y fecha/hora visibles. |
| `@page @top-right` | Identificación del documento. |
| `@page @bottom-center` | Código, versión y fecha/hora. |
| `<footer>` del HTML | Código, versión y fecha/hora para pantalla. |

Usar horario de Argentina (`America/Argentina/Buenos_Aires`, UTC−03:00) y obtener la hora real cuando esté disponible. No inventar marcas temporales ni sustituir automáticamente una fecha histórica cuando solo se audita. No incrementar una versión por ajustes de referencias externas salvo que corresponda según el protocolo o una instrucción.

## 5. Referencias, calidad académica y código

- Las referencias entre materiales deben usar códigos o denominaciones estables, sin versiones ni nombres de archivo. No crear dependencias de mantenimiento por futuras publicaciones.
- Conservar las referencias académicas necesarias para comprender el contenido.
- Distinguir criterios didácticos de IG de reglas generales de Python; no presentar una restricción de la materia como prohibición universal del lenguaje.
- En ejemplos de Python, comprobar sintaxis, indentación, entrada/salida y resultado cuando se pueda ejecutar; documentar ejemplos deliberadamente no admitidos.
- Escapar en HTML los caracteres de código que lo requieran: `&lt;`, `&gt;`, `&amp;`. Verificar espacios e indentación en `pre`.
- Usar `h1` una sola vez, seguido de `h2` y `h3`; usar tablas con encabezados comprensibles y no eliminar fuentes o atribuciones provistas.

### Código descargable

- Esta carpeta es la única raíz de trabajo y repositorio del proyecto. Los archivos descargables viven en `CODIGOS/IG.A.NN/`; descubrir documentos, ejemplos y enlaces a partir de `manifest.json`, no de un inventario fijo en estas instrucciones.
- Mantener `IG.A.NN_EXXX_TIPO.py`, con `TIPO` igual a `NO_ADMITIDO`, `FORMA_ESPERADA` o `ALTERNATIVA`. No incluir versiones de PDF en esos nombres, no reutilizar identificadores retirados y no mover archivos publicados sin revisar las referencias.
- Los `.py` conservan el bloque `pre` del HTML académico y pueden agregar solo el contexto mínimo necesario para funcionar como programas completos. Mantener UTF-8, cuatro espacios por nivel y ausencia de tabulaciones. No corregir silenciosamente ni convertir un ejemplo `NO_ADMITIDO` en una `FORMA_ESPERADA`.
- Todo código Python ofrecido para descarga debe ser autónomo, ejecutable y estar validado mediante una ejecución real. Los fragmentos académicos deben completarse con el contexto mínimo necesario, sin alterar el concepto que ilustran.
- Registrar en el manifiesto la procedencia, dependencias, hash, clasificación y comprobación de ejecución de cada descarga. No inventar datos ajenos al concepto académico para volver autónomo a un fragmento.
- `configuracion_publicacion.json` no contiene credenciales. Completar enlaces reales únicamente después de publicación autorizada y verificación del archivo descargado. Para enlaces en documentos, generar una copia HTML mediante `herramientas/actualizar_enlaces_html.py`; no modificar un HTML académico aprobado solo para insertar una URL.

## 6. Verificación antes de entregar

### HTML

- Archivo UTF-8 válido y autónomo; apertura local sin recursos rotos.
- Logo institucional, encabezado completo y hoja de estilos presentes.
- Sin marcadores de plantilla en documentos terminados.
- Código, versión y fecha/hora coherentes dentro de cada documento, sin alterar metadatos existentes en una auditoría que no requiera ese cambio.
- Sin etiquetas mal anidadas, tablas incompletas ni código recortado.

### PDF

Cuando se solicite o sea posible generarlo, renderizar con Chromium, Chrome o Edge compatible con CSS paginado: A4, escala 100 %, fondos activados y encabezados/pies automáticos del navegador desactivados. Revisar todas las páginas: cabeceras, pie con código/versión/fecha/hora y `PÁG. X / Y`, márgenes, legibilidad, saltos, tablas, figuras y código. Si el motor no admite las cajas de margen de `@page`, reportarlo expresamente.

### Código y enlaces

- Ejecutar `herramientas/extraer_codigos.py` sin `--write` para detectar diferencias antes de sincronizar un `.py` con su HTML.
- Ejecutar `herramientas/validar_codigos.py --run` para comprobar nombres, UTF-8, ausencia de tabulaciones, sintaxis Python, hash, conservación del bloque `pre` y ejecución real con salida esperada.
- Ejecutar `herramientas/validar_enlaces.py` para comprobar enlaces configurados; usar `--check-downloads` solo cuando exista una publicación autorizada que pueda descargarse.
- Antes de un commit o una publicación, ejecutar `herramientas/preparar_publicacion.py`. No crear commits ni hacer `push` sin instrucción expresa del usuario; antes de un `push`, informar remoto, rama y commits concretos.

## 7. Modo de trabajo y respuesta final

- **Nuevo documento:** duplicar la plantilla técnica, completar contenido, sincronizar identificación y validar HTML; generar PDF solo si se solicita o forma parte del encargo.
- **Edición académica:** señalar cambios propuestos y editar solo lo autorizado.
- **Edición visual:** modificar CSS o componentes visuales sin alterar texto académico; evitar reformateos masivos, especialmente del logo Base64.
- **Corrección de impresión:** actuar sobre `@media print` y `@page`, validar mediante renderizado real y preservar la pantalla.
- **Auditoría:** revisar y enumerar hallazgos; no alterar archivos salvo que se solicite la corrección.

Al finalizar, informar brevemente los archivos modificados, el código/versión/fecha aplicada cuando corresponda, las pruebas realmente ejecutadas y las cuestiones pendientes de aprobación académica.
