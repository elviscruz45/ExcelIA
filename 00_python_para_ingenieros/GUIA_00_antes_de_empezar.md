# Guía 00 — Antes de empezar con Python (Colab e internet)

**Tiempo estimado:** 30 minutos, con apoyo de tu instructor.

Esta guía es para ingenieros de planta que usan Excel pero **nunca han programado** ni trabajado en la nube. Léela con tu instructor antes de abrir la lección `00_01_bienvenida_y_entorno.ipynb`.

---

## 1. Qué es internet (en la práctica)

Piensa en internet como el **bus de datos** entre tu computadora y los servidores de empresas como Google.

- Cuando abres una página web, tu navegador **pide** información a un servidor lejano y la **muestra** en pantalla.
- Cuando usas **Google Colab**, no instalas Python en tu PC: el código corre en un servidor de Google y tú ves el resultado en el navegador.
- Necesitas **conexión a internet estable** durante toda la sesión.

**Analogía de planta:** Es como consultar el historiador PI desde la oficina de mantenimiento. Los datos están en otro lugar; tú los ves en tu pantalla a través de la red.

---

## 2. Lo mínimo que debes saber del navegador

| Acción | Cómo hacerlo |
|--------|--------------|
| Abrir una página | Escribe la dirección (URL) en la barra superior o haz clic en un enlace |
| Nueva pestaña | `Ctrl + T` (Windows) o `Cmd + T` (Mac) |
| Copiar texto | Selecciona → clic derecho → Copiar (o `Ctrl/Cmd + C`) |
| Pegar texto | Clic donde quieras pegar → clic derecho → Pegar (o `Ctrl/Cmd + V`) |
| Subir un archivo | Botón **Subir** o **Elegir archivo** en la página |

**Navegadores recomendados:** Google Chrome o Microsoft Edge (versiones recientes).

---

## 3. Cuenta de Google

Colab requiere una **cuenta de Google** (Gmail).

1. Si ya tienes Gmail, úsala para iniciar sesión en [Google Colab](https://colab.research.google.com/).
2. Si no tienes cuenta, pide ayuda a tu instructor para crearla (nombre, contraseña, verificación).
3. No compartas tu contraseña. Solo necesitas acceso a Colab y, opcionalmente, Google Drive para guardar notebooks.

---

## 4. Abrir tu primera lección en Colab

### Paso a paso

1. Abre [https://colab.research.google.com/](https://colab.research.google.com/) e inicia sesión.
2. Menú **Archivo → Subir notebook**.
3. Elige el archivo `00_01_bienvenida_y_entorno.ipynb` (tu instructor te lo enviará o estará en la carpeta del curso).
4. Verás el notebook abierto: bloques de **texto explicativo** (Markdown) y bloques de **código** (fondo gris).

### Ejecutar una celda de código

1. Haz clic dentro de una celda de código.
2. Presiona **Shift + Enter**.
3. El resultado aparece **debajo** de la celda (texto, números o gráficos).

**Importante:** El código no corre solo. Debes ejecutar cada celda manualmente, de arriba hacia abajo.

---

## 5. Archivos y carpetas del curso

| Elemento | Qué es | Analogía con Excel |
|----------|--------|---------------------|
| `.ipynb` | Notebook de la lección (texto + código) | Como un libro de Excel con varias hojas y macros |
| `data/` | Carpeta con datos de ejemplo (CSV) | Como una carpeta con archivos `.xlsx` de lecturas |
| `outputs/` | Carpeta donde se guardan gráficos generados | Como una carpeta de reportes exportados |
| `.csv` | Archivo de datos en texto (columnas separadas por comas) | Como guardar una hoja como "CSV delimitado por comas" |

En Colab, el panel de archivos (icono de carpeta a la izquierda) muestra las carpetas del entorno. Si generas un gráfico, puedes **descargarlo** con clic derecho sobre el archivo en ese panel.

---

## 6. Jupyter vs Excel (mapa mental)

| En Excel | En Jupyter / Colab |
|----------|-------------------|
| Celda (A1, B2…) | Celda de código o texto |
| Fórmula `=SUMA(A1:A10)` | Línea de código Python |
| Ver resultado en la celda | Ver resultado debajo de la celda (`print`) |
| Guardar `.xlsx` | Guardar notebook o descargar outputs |

Si vienes de Excel, busca en cada lección las cajas **"Si vienes de Excel…"** — traducen conceptos que ya conoces.

---

## 7. Checklist antes de la lección 00_01

Marca cada ítem con tu instructor:

- [ ] Tengo internet estable y un navegador actualizado.
- [ ] Puedo iniciar sesión en Google (cuenta Gmail).
- [ ] Sé abrir Colab y subir un archivo `.ipynb`.
- [ ] Ejecuté al menos una celda con **Shift + Enter** y vi el resultado.
- [ ] Entiendo que debo leer el texto de cada sección antes de ejecutar el código.

Si los cinco ítems están marcados, estás listo para **Lección 00_01**.

---

## 8. Problemas frecuentes

| Problema | Qué hacer |
|----------|-----------|
| Colab pide iniciar sesión | Usa tu cuenta Google; verifica que no esté bloqueada |
| No aparece resultado al ejecutar | Asegúrate de haber hecho clic en la celda de **código** (no solo en texto) |
| "Sesión desconectada" | Vuelve a conectar (Colab → Conectar). Re-ejecuta celdas desde el inicio |
| No encuentro el archivo `.ipynb` | Pide al instructor el enlace o la carpeta del módulo 0 |
| Quiero guardar mi trabajo | **Archivo → Guardar una copia en Drive** o descarga el notebook |

---

## 9. Siguiente paso

1. Lee el mapa general del curso: [`GUIA_MAPA_CURSO_MINERIA50.md`](../GUIA_MAPA_CURSO_MINERIA50.md)
2. Abre la lección: `00_01_bienvenida_y_entorno.ipynb`
3. Consulta términos nuevos en: [`GLOSARIO_PLANTA_TECNOLOGIA.md`](../GLOSARIO_PLANTA_TECNOLOGIA.md)
