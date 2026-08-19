# Prompt para Gemini — Diapositivas de apoyo

Usa este contenido como prompt completo en Gemini para que genere una presentacion de diapositivas de apoyo para un curso de Mineria 5.0.

## Instrucciones para Gemini

Genera una presentacion en espanol (Latinoamerica), con tono docente claro, profesional y cercano, pensada para un **supervisor de planta concentradora** que hoy trabaja principalmente con **Excel**, usa algo de **Power BI**, conoce algo de **SQL local**, y quiere evolucionar hacia una forma de trabajo de **Mineria 5.0**.

La presentacion debe cumplir estas reglas:

1. Debe estar pensada para un curso de **7 horas**, dividido en **2 sesiones** de aproximadamente **3.5 horas** cada una.
2. La audiencia **no tendra acceso en vivo a PI System** durante la clase. Para Supabase y Power BI se usara un enfoque de demo del repo:
   - Supabase: se crea/consulta la base con scripts y/o SQL (si hay credenciales; si no, se usa el fallback local)
   - Power BI: se importara **CSV** en Power BI Desktop (sin requerir Power BI Service en vivo)
   - Python: se ejecuta en **Google Colab** con los notebooks del curso
3. Aun asi, la teoria debe explicar el flujo completo: **sensores -> SCADA/DCS -> PI Historian -> nube/Supabase -> Python -> Power BI -> alerta de mantenimiento**.
4. El caso de estudio principal debe ser **PUMP101** en una **linea de molienda** de una planta concentradora.
5. El hilo narrativo debe ser progresivo:
   - primero explicar la realidad actual del supervisor,
   - luego mostrar la vision integrada de Mineria 5.0,
   - despues posicionar a Python como centro del pipeline,
   - y finalmente entrar a IA predictiva y priorizacion de alertas.
6. Cada diapositiva debe incluir exactamente estos bloques:
   - `Titulo`
   - `Bullets`
   - `Notas del orador`
   - `Referencia practica del curso`
7. Los `Bullets` deben ser cortos, visuales y listos para pasar a diapositiva. Evita parrafos largos.
8. Las `Notas del orador` deben servir para que el instructor explique la teoria antes de ir al codigo. Deben tener entre 2 y 5 frases.
9. No pongas codigo largo en las diapositivas. A lo mucho una linea de pseudocodigo o una analogia tipo Excel.
10. Usa analogias simples:
    - Python como la cocina o motor del pipeline
    - DataFrame como una hoja Excel en memoria
    - PI Historian como un Excel gigante con millones de filas
    - Random Forest como un comite de expertos que vota
11. Mantener una estetica industrial/minera:
    - colores sobrios
    - iconos de sensores, bombas, dashboards, nube, alertas
    - poco texto por slide
12. Incluir sugerencias de diagramas cuando ayuden:
    - viaje del dato
    - modelo Purdue simplificado
    - escalera de mantenimiento
    - pipeline de alertas
13. No vender humo con IA. Debe quedar claro que:
    - la IA apoya al supervisor, no lo reemplaza
    - todo depende de buena calidad de dato
    - primero se entiende el proceso, luego se modela
14. Donde se hable de Supabase/Power BI, aclarar que la practica del curso usa datos simulados del repo cuando no exista acceso a sistemas reales, y que el objetivo es dominar el flujo reproducible de tablas -> carga -> export -> dashboard.
15. El nivel tecnico de ML debe ser **moderado**: explicar Random Forest, matriz de confusion, ROC, Z-score, Isolation Forest y RUL con lenguaje simple y analogias de planta.

La salida debe ser una presentacion de **65 diapositivas** aproximadamente.

## Contexto del curso

- Nombre del curso: **Mineria 5.0 para supervisor de planta concentradora**
- Duracion: **7 horas**
- Formato: **2 sesiones de 3.5 horas**
- Enfoque principal: **IA predictiva de fallas**
- Soporte practico: **Google Colab + notebooks del proyecto**
- Contexto industrial: **planta concentradora**, especialmente **molienda**
- Caso central: **PUMP101**
- Meta pedagogica: primero ensenar teoria con diapositivas y luego abrir el notebook correspondiente para reforzar con codigo y graficos

## Material del curso que debes respetar

Usa como base conceptual estas referencias del curso:

- `GUIA_MAPA_CURSO_MINERIA50.md`
- `GLOSARIO_PLANTA_TECNOLOGIA.md`
- `00_python_para_ingenieros/00_01_bienvenida_y_entorno.ipynb`
- `00_python_para_ingenieros/00_02_variables_y_unidades.ipynb`
- `00_python_para_ingenieros/00_05_condicionales.ipynb`
- `00_python_para_ingenieros/00_08_intro_pandas_planta.ipynb`
- `01_PI_historiador_introduccion/clase_01_PI_historiador_introduccion.md`
- `04_ecosistema_datos/IV_01_flujo_datos_mineria50.ipynb`
- `05_ia_predictiva/IV_05_mantenimiento_predictivo.ipynb`
- `05_ia_predictiva/IV_06_ml_clasificacion_fallas.ipynb`
- `05_ia_predictiva/IV_07_anomalias_y_rul.ipynb`
- `05_ia_predictiva/IV_08_caso_integrado_alertas.ipynb`

## Estructura esperada

La presentacion debe dividirse asi:

- **Sesion 1:** de Excel a Mineria 5.0, flujo OT/IT, Python esencial y PI simulado
- **Sesion 2:** mantenimiento predictivo, machine learning, anomalias, RUL y pipeline de alertas

---

## Sesion 1 — De Excel a Mineria 5.0 + Python esencial

### Diapositiva 1
**Titulo**  
Mineria 5.0 para supervisores de planta concentradora

**Bullets**
- Del Excel aislado al pipeline integrado de datos
- Caso de estudio: PUMP101 en molienda
- Teoria primero, Colab despues

**Notas del orador**  
Abre explicando que la idea del curso no es volver programador al supervisor, sino darle una estructura moderna para usar mejor los datos de planta. La promesa es clara: entender de donde sale el dato, como viaja y como usarlo para anticipar fallas. Presenta a PUMP101 como el activo que conectara toda la historia del curso.

**Referencia practica del curso**  
`GUIA_MAPA_CURSO_MINERIA50.md`

### Diapositiva 2
**Titulo**  
Como trabaja hoy un supervisor de concentradora

**Bullets**
- Excel para reportes y consolidaciones
- Power BI para ver indicadores
- SQL local para algunas consultas
- Mucho trabajo manual y poca trazabilidad

**Notas del orador**  
Reconoce la realidad actual de la audiencia para generar confianza. Explica que estas herramientas no estan mal; el problema es que suelen estar desconectadas. La consecuencia es que los datos llegan tarde, se duplican y cuesta convertirlos en decisiones oportunas.

**Referencia practica del curso**  
`GUIA_MAPA_CURSO_MINERIA50.md`

### Diapositiva 3
**Titulo**  
Limitaciones del enfoque actual

**Bullets**
- Datos repartidos en varios archivos
- Analisis posterior a la falla
- Reportes no siempre repetibles
- Escala limitada cuando crecen los sensores

**Notas del orador**  
Conecta esta diapositiva con dolores reales: cierres de turno, reportes manuales, perdida de version de archivos y dificultad para cruzar variables. Haz ver que Excel sirve muy bien para ciertas tareas, pero no para sostener un sistema de analitica operativa a escala.

**Referencia practica del curso**  
`04_ecosistema_datos/IV_01_flujo_datos_mineria50.ipynb`

### Diapositiva 4
**Titulo**  
La vision integrada de Mineria 5.0

**Bullets**
- Integrar OT e IT
- Conectar sensores, datos, analitica y decision
- Automatizar limpieza, consulta y alertas
- Pasar de reaccionar a anticipar

**Notas del orador**  
Define Mineria 5.0 en lenguaje simple: conectar lo que ocurre en planta con herramientas digitales que permitan actuar mejor y antes. No la presentes como una moda, sino como una forma de trabajo basada en datos y criterio operacional.

**Referencia practica del curso**  
`GUIA_MAPA_CURSO_MINERIA50.md`

### Diapositiva 5
**Titulo**  
Caso de estudio del curso: PUMP101

**Bullets**
- Bomba de alimentacion en linea de molienda
- Variables: temperatura, vibracion, presion y corriente
- Equipo ideal para explicar degradacion

**Notas del orador**  
Introduce el activo sobre el que girara la teoria y la practica. Recalca que una bomba es un buen ejemplo porque combina fenomenos mecanicos y de proceso, y porque los supervisores reconocen facilmente el valor de monitorear tendencia y condicion.

**Referencia practica del curso**  
`05_ia_predictiva/IV_05_mantenimiento_predictivo.ipynb`

### Diapositiva 6
**Titulo**  
El viaje del dato en planta

**Bullets**
- Sensor -> PLC -> PI Historian
- Python limpia y transforma
- Supabase centraliza historial
- Power BI visualiza
- Mantenimiento decide

**Notas del orador**  
Esta es una de las diapositivas centrales del curso. Explica el flujo completo como una cadena de valor del dato, desde la medicion hasta la accion. Aclara que en clase se recorrera toda la cadena en teoria, pero en vivo se demostrara principalmente la parte de Python y analitica con datos simulados.

**Referencia practica del curso**  
`04_ecosistema_datos/IV_01_flujo_datos_mineria50.ipynb`

### Diapositiva 7
**Titulo**  
Campo: donde nace el dato

**Bullets**
- Sensores de temperatura, vibracion y presion
- Señales 4-20 mA y redes como Profibus
- La calidad de dato empieza en el campo

**Notas del orador**  
Explica que la analitica no compensa un mal instrumento o un sensor mal calibrado. Si el dato nace mal, todo lo demas se contamina. Aprovecha para introducir que cada variable cumple un rol distinto: unas hablan del proceso y otras de la salud del activo.

**Referencia practica del curso**  
`04_ecosistema_datos/IV_01_flujo_datos_mineria50.ipynb`

### Diapositiva 8
**Titulo**  
SCADA y DCS: ver y controlar no es lo mismo que analizar

**Bullets**
- SCADA/HMI: supervision y operacion
- DCS: control del proceso
- No son el repositorio historico principal

**Notas del orador**  
Aclara un error frecuente: creer que porque algo se ve en pantalla ya esta listo para analitica historica. SCADA y DCS sirven para operar y controlar; el historiador y las capas IT sirven para conservar, consultar y analizar a escala.

**Referencia practica del curso**  
`GLOSARIO_PLANTA_TECNOLOGIA.md`

### Diapositiva 9
**Titulo**  
PI Historian: el Excel gigante de la planta

**Bullets**
- Guarda millones de registros con fecha y hora
- Trabaja con tags de proceso
- Permite ver tendencia y contexto historico

**Notas del orador**  
Usa la analogia del Excel gigante porque conecta rapido con la audiencia. Explica que la gran diferencia es la escala, la continuidad temporal y la estructura de tags. Introduce que despues esos datos pueden exportarse a CSV para ser procesados por Python.

**Referencia practica del curso**  
`01_PI_historiador_introduccion/clase_01_PI_historiador_introduccion.md`

### Diapositiva 10
**Titulo**  
Tag, timestamp y quality

**Bullets**
- Tag: nombre unico del punto de medicion
- Timestamp: cuando ocurrio el valor
- Quality: GOOD, BAD o QUESTIONABLE

**Notas del orador**  
Define estos tres conceptos porque luego son claves para comprender limpieza y confiabilidad del analisis. Aterriza con ejemplos como `PUMP101.BEARING_TEMP` y explica por que filtrar `BAD` es una decision operativa, no solo tecnica.

**Referencia practica del curso**  
`01_PI_historiador_introduccion/clase_01_PI_historiador_introduccion.md`

### Diapositiva 11
**Titulo**  
OT vs IT en una concentradora

**Bullets**
- OT opera el proceso en tiempo real
- IT almacena, consulta y analiza
- Mineria 5.0 une ambos mundos

**Notas del orador**  
Explica la diferencia entre tecnologia operacional y tecnologia de informacion. Resalta que unir OT e IT no significa mezclar todo sin orden, sino construir puentes controlados para usar mejor el dato en mantenimiento, produccion y gestion.

**Referencia practica del curso**  
`04_ecosistema_datos/IV_01_flujo_datos_mineria50.ipynb`

### Diapositiva 12
**Titulo**  
Modelo Purdue simplificado

**Bullets**
- Nivel 0: sensores
- Nivel 1: PLC
- Nivel 2: SCADA
- Nivel 3: PI y MES
- Nivel 4: Python ETL y Supabase
- Nivel 5: Power BI y ERP

**Notas del orador**  
No hace falta profundizar academicamente en Purdue; basta con que el supervisor vea que existen capas con roles distintos. La idea es ordenar mentalmente donde vive cada tecnologia y por que la nube y los dashboards estan varios niveles por encima del control.

**Referencia practica del curso**  
`04_ecosistema_datos/IV_01_flujo_datos_mineria50.ipynb`

### Diapositiva 13
**Titulo**  
Excel, Power BI, SQL y Python no compiten

**Bullets**
- Excel modela y calcula rapido
- Power BI comunica indicadores
- SQL consulta historial centralizado
- Python conecta, limpia y automatiza

**Notas del orador**  
Evita la sensacion de reemplazo. El mensaje debe ser que cada herramienta tiene su lugar y que Python sirve como articulador entre varias capas. Esto baja resistencia y facilita la adopcion.

**Referencia practica del curso**  
`04_ecosistema_datos/IV_01_flujo_datos_mineria50.ipynb`

### Diapositiva 14
**Titulo**  
Por que SQL en la nube (Supabase) para dashboards y trazabilidad

**Bullets**
- Tablas mínimas: `equipos`, `lecturas_pi`, `eventos_mantenimiento`
- Esquema en `04_ecosistema_datos/sql/schema_supabase.sql`
- Historial centralizado con `timestamp` + `quality`
- Base única para dashboards, trazabilidad y decisiones

**Notas del orador**  
Presenta a Supabase como un “historiador operativo” para analítica en la nube: mismo modelo de datos para operaciones, mantenimiento y jefatura. En clase se trabaja con datos simulados y scripts del repo; en planta real el objetivo mental sigue siendo: crear tablas, cargar datos y visualizar con trazabilidad.

**Referencia practica del curso**  
`04_ecosistema_datos/sql/schema_supabase.sql`

### Diapositiva 15
**Titulo**  
Python como centro del pipeline

**Bullets**
- Extrae export PI (CSV/API) y estandariza estructura
- Limpia datos y filtra `quality` (GOOD)
- Carga en Supabase (IV_04 + script de seed)
- Exporta datasets para Power BI (CSV listo para importar)

**Notas del orador**  
Usa la analogía de la cocina: los sensores entregan ingredientes, pero Python cocina, organiza y entrega platos útiles a Supabase (SQL) y a Power BI (CSV/datos). Esta es la diferencia entre “hacer un gráfico” y construir un pipeline repetible para decisiones.

**Referencia practica del curso**  
`04_ecosistema_datos/IV_04_pipeline_python_datos.ipynb`

### Diapositiva 16
**Titulo**  
Por que Python y no VBA, R o SQL

**Bullets**
- Mas facil de leer y mantener
- Fuerte en datos industriales tabulares
- Integra ETL, graficos y machine learning
- Gran comunidad y librerias

**Notas del orador**  
No des una guerra de lenguajes. Explica simplemente que VBA vive muy pegado a Excel, SQL consulta pero no modela todo el flujo y R es fuerte en analitica, pero Python ofrece una combinacion muy equilibrada para automatizar y escalar en entornos mixtos.

**Referencia practica del curso**  
`00_python_para_ingenieros/00_01_bienvenida_y_entorno.ipynb`

### Diapositiva 17
**Titulo**  
Colab: el punto de entrada practico

**Bullets**
- Python en el navegador
- Sin instalar entorno local
- Ejecutar celda a celda
- Ideal para practica guiada

**Notas del orador**  
Explica que Colab elimina la friccion inicial para alguien que aun no domina instalaciones ni entornos. Conecta con la mecanica del curso: primero teoria en diapositiva, luego se abre un notebook y se ejecutan celdas en orden.

**Referencia practica del curso**  
`00_python_para_ingenieros/00_01_bienvenida_y_entorno.ipynb`

### Diapositiva 18
**Titulo**  
Que es una variable para un ingeniero

**Bullets**
- Un nombre que guarda un valor
- Puede representar temperatura, caudal o horas
- Conviene nombrar con unidad

**Notas del orador**  
Parte desde algo familiar: una celda de Excel con nombre o una variable de proceso. Explica que en Python conviene hacer explicito el significado con nombres como `temp_rodamiento_c` o `presion_descarga_bar`.

**Referencia practica del curso**  
`00_python_para_ingenieros/00_02_variables_y_unidades.ipynb`

### Diapositiva 19
**Titulo**  
Variables y tags: el puente mental correcto

**Bullets**
- Un tag PI identifica una medicion
- Una variable Python almacena un valor
- Juntos permiten pasar del dato al analisis

**Notas del orador**  
Ayuda a la audiencia a no ver Python como algo abstracto. Un tag como `PUMP101.BEARING_TEMP` existe en la planta; una variable Python permite usar ese dato en calculos, reglas y graficos. Este es el primer puente entre mundo OT y analitica.

**Referencia practica del curso**  
`00_python_para_ingenieros/00_02_variables_y_unidades.ipynb`

### Diapositiva 20
**Titulo**  
Condicionales: la logica detras de una alarma

**Bullets**
- Si vibracion > umbral -> alerta
- Si temp y vibracion suben -> prioridad mayor
- Es la misma idea de la funcion SI() de Excel

**Notas del orador**  
Esta diapositiva le da confianza al alumno porque muestra que la logica no es nueva. Lo nuevo es la escala y la capacidad de aplicar esa logica a miles de registros, no solo a unas cuantas filas de una hoja.

**Referencia practica del curso**  
`00_python_para_ingenieros/00_05_condicionales.ipynb`

### Diapositiva 21
**Titulo**  
Pandas: una hoja Excel en memoria

**Bullets**
- Lee CSV de planta
- Filtra, agrupa y resume
- Maneja miles de filas rapidamente

**Notas del orador**  
Presenta a pandas como la herramienta que vuelve practico el trabajo con datos tabulares. La audiencia no necesita dominar toda la libreria; basta con entender que un DataFrame permite cargar, explorar y filtrar datos mucho mas rapido que hacerlo manualmente.

**Referencia practica del curso**  
`00_python_para_ingenieros/00_08_intro_pandas_planta.ipynb`

### Diapositiva 22
**Titulo**  
Filtrar calidad GOOD antes de decidir

**Bullets**
- No todo dato medido es util
- Filtrar BAD mejora confiabilidad
- Calidad de dato impacta alertas y KPIs

**Notas del orador**  
Conecta esta idea con la experiencia diaria del supervisor: sensores ruidosos, mantenimiento deficiente del instrumento, señales intermitentes. Explica que limpiar el dato no es cosmetica; es una condicion para confiar en el analisis y no disparar falsas alarmas.

**Referencia practica del curso**  
`00_python_para_ingenieros/00_08_intro_pandas_planta.ipynb`

### Diapositiva 23
**Titulo**  
La tendencia vale mas que una foto aislada

**Bullets**
- Un punto no explica degradacion
- La curva muestra direccion y velocidad
- Tendencia + contexto = mejor decision

**Notas del orador**  
Explica por que el analisis de condicion no debe quedarse en un valor instantaneo. Una vibracion de 4.2 mm/s puede parecer aceptable sola, pero si lleva dias subiendo cambia completamente la interpretacion. Aqui preparas el terreno para mantenimiento predictivo.

**Referencia practica del curso**  
`00_python_para_ingenieros/00_08_intro_pandas_planta.ipynb`

### Diapositiva 24
**Titulo**  
PI real vs PI simulado en este curso

**Bullets**
- La planta usa PI, pero no habra acceso en clase
- Trabajaremos con exportaciones y datos simulados
- Los conceptos son los mismos

**Notas del orador**  
Aclara esta limitacion desde el inicio para alinear expectativas. El objetivo de la clase no es navegar PI en vivo, sino entender sus conceptos y procesar datos equivalentes con Python. Eso permite mantener el valor pedagógico aun sin conectividad a sistemas reales.

**Referencia practica del curso**  
`01_PI_historiador_introduccion/clase_01_PI_historiador_introduccion.md`

### Diapositiva 25
**Titulo**  
Resumen de la sesion 1

**Bullets**
- Ya entendemos el viaje del dato
- Python es el centro operativo del pipeline
- La calidad y la tendencia importan
- En la siguiente sesion veremos como anticipar fallas

**Notas del orador**  
Cierra la primera sesion uniendo los conceptos. Repite que el curso no abandona Excel ni Power BI, sino que los conecta mejor mediante Python y una arquitectura mas ordenada. Deja sembrada la idea de que ahora viene la parte de mayor valor: decidir antes de la falla.

**Referencia practica del curso**  
`GUIA_MAPA_CURSO_MINERIA50.md`

---

## Sesion 2 — IA predictiva + practica en Colab

### Diapositiva 26
**Titulo**  
Donde entra la IA en el pipeline

**Bullets**
- Despues de limpiar y estructurar datos
- Antes de priorizar la accion
- No reemplaza el criterio del supervisor

**Notas del orador**  
Abre la sesion 2 dejando claro que la IA no es magia ni punto de partida. Primero se necesita el dato ordenado, entendible y confiable. Solo entonces tiene sentido aplicar modelos para apoyar la toma de decisiones.

**Referencia practica del curso**  
`05_ia_predictiva/IV_08_caso_integrado_alertas.ipynb`

### Diapositiva 27
**Titulo**  
De reactivo a prescriptivo

**Bullets**
- Reactivo: reparar tras la falla
- Preventivo: intervenir por tiempo
- Predictivo: actuar por condicion
- Prescriptivo: priorizar recomendacion optima

**Notas del orador**  
Usa la escalera de mantenimiento del notebook para mostrar madurez. Pregunta mentalmente a la audiencia en que nivel siente que esta hoy su planta. La idea no es juzgar, sino mostrar una ruta de evolucion realista.

**Referencia practica del curso**  
`05_ia_predictiva/IV_05_mantenimiento_predictivo.ipynb`

### Diapositiva 28
**Titulo**  
Que gana una concentradora con predictivo

**Bullets**
- Menos fallas funcionales inesperadas
- Mejor uso de ventanas de parada
- Mayor trazabilidad de la decision
- Prioridad segun riesgo y no solo intuicion

**Notas del orador**  
Habla en terminos de negocio y operacion, no solo de tecnologia. El supervisor debe ver que esto impacta disponibilidad, costo de falla, coordinacion con mantenimiento y calidad de la planificacion.

**Referencia practica del curso**  
`05_ia_predictiva/IV_05_mantenimiento_predictivo.ipynb`

### Diapositiva 29
**Titulo**  
Variables de condicion en PUMP101

**Bullets**
- Temperatura de rodamiento
- Vibracion RMS
- Presion de descarga
- Corriente del motor

**Notas del orador**  
Explica que un modelo no trabaja con intuiciones, sino con variables medibles. Algunas reflejan el estado mecanico y otras el contexto de proceso. Juntas cuentan una historia mas completa del equipo.

**Referencia practica del curso**  
`05_ia_predictiva/IV_05_mantenimiento_predictivo.ipynb`

### Diapositiva 30
**Titulo**  
Feature engineering: convertir datos en señales utiles

**Bullets**
- Media movil de vibracion
- Pendiente de temperatura
- Porcentaje de presion
- Tendencia por ventana de tiempo

**Notas del orador**  
Aclara que un solo dato bruto muchas veces no basta. Las features derivadas resumen comportamiento, tendencia y contexto. Esta es una de las grandes diferencias entre mirar una planilla y construir una analitica predictiva.

**Referencia practica del curso**  
`05_ia_predictiva/IV_05_mantenimiento_predictivo.ipynb`

### Diapositiva 31
**Titulo**  
Pensar en tendencias y no solo en umbrales

**Bullets**
- Un valor instantaneo puede engañar
- La media movil da estabilidad
- La pendiente revela degradacion

**Notas del orador**  
Relaciona esta idea con el mundo real: muchas veces el equipo aun no cruza el limite critico, pero claramente viene degradandose. El predictivo sirve para capturar esa pelicula, no solo una fotografia.

**Referencia practica del curso**  
`05_ia_predictiva/IV_05_mantenimiento_predictivo.ipynb`

### Diapositiva 32
**Titulo**  
Que es machine learning para un supervisor

**Bullets**
- Aprender patrones desde datos historicos
- Estimar riesgo con varias variables a la vez
- Apoyar decisiones repetibles

**Notas del orador**  
Evita definiciones academicas largas. Di simplemente que el modelo aprende de ejemplos historicos donde hubo comportamientos normales y cercanos a falla. Luego aplica ese aprendizaje a nuevos datos para apoyar la decision humana.

**Referencia practica del curso**  
`05_ia_predictiva/IV_06_ml_clasificacion_fallas.ipynb`

### Diapositiva 33
**Titulo**  
Clasificacion binaria: normal vs falla inminente

**Bullets**
- `falla = 0` significa operacion normal
- `falla = 1` significa condicion de riesgo
- La pregunta es: que tan cerca estamos de fallar

**Notas del orador**  
Explica que el problema del notebook no intenta adivinar cualquier cosa, sino responder una pregunta operacional concreta. Esto ayuda a la audiencia a entender por que el objetivo del modelo debe ser muy claro desde el principio.

**Referencia practica del curso**  
`05_ia_predictiva/IV_06_ml_clasificacion_fallas.ipynb`

### Diapositiva 34
**Titulo**  
Random Forest como comite de expertos

**Bullets**
- Muchos arboles opinan
- Cada uno mira patrones distintos
- La decision final sale de la votacion

**Notas del orador**  
Usa la analogia del comite de expertos porque se entiende muy bien en mantenimiento. Un arbol puede fijarse mas en vibracion, otro en temperatura y otro en la combinacion de ambas. El conjunto suele ser mas robusto que una sola regla fija.

**Referencia practica del curso**  
`05_ia_predictiva/IV_06_ml_clasificacion_fallas.ipynb`

### Diapositiva 35
**Titulo**  
Costo industrial de equivocarse

**Bullets**
- Falso positivo: parada innecesaria
- Falso negativo: falla no detectada
- El mejor modelo depende del costo operacional

**Notas del orador**  
Esta es la diapositiva que aterriza el modelo a negocio. No basta con decir que un algoritmo acierta mucho; importa como se equivoca. En mantenimiento, una falla no detectada puede costar mucho mas que una revision adicional.

**Referencia practica del curso**  
`05_ia_predictiva/IV_06_ml_clasificacion_fallas.ipynb`

### Diapositiva 36
**Titulo**  
Matriz de confusion sin asustarse

**Bullets**
- Aciertos normales
- Aciertos de falla
- Falsas alarmas
- Fallas que se escaparon

**Notas del orador**  
Explica la matriz como un conteo ordenado de decisiones correctas e incorrectas. No hace falta entrar en algebra; lo importante es que el supervisor entienda cuantas alarmas sirven, cuantas sobran y cuantas fallas podrian escaparse.

**Referencia practica del curso**  
`05_ia_predictiva/IV_06_ml_clasificacion_fallas.ipynb`

### Diapositiva 37
**Titulo**  
Recall, precision y criterio de operacion

**Bullets**
- Recall: cuantas fallas logras captar
- Precision: cuantas alertas realmente importan
- Hay que balancear seguridad y productividad

**Notas del orador**  
Presenta estas metricas con lenguaje operativo. Si subes recall, tal vez detectes mas fallas pero tambien generes mas alertas. Si exiges mucha precision, podrias dejar escapar eventos relevantes. El punto es discutir criterio, no memorizar formulas.

**Referencia practica del curso**  
`05_ia_predictiva/IV_06_ml_clasificacion_fallas.ipynb`

### Diapositiva 38
**Titulo**  
Curva ROC como termometro del discriminador

**Bullets**
- Mide capacidad de separar normal y falla
- Mejor cuanto mas se aleja de la diagonal
- Sirve para comparar modelos

**Notas del orador**  
Presenta la ROC de forma conceptual. No la conviertas en una clase estadistica. Basta con que la audiencia entienda que resume que tan bien el modelo distingue entre comportamientos normales y condiciones cercanas a falla.

**Referencia practica del curso**  
`05_ia_predictiva/IV_06_ml_clasificacion_fallas.ipynb`

### Diapositiva 39
**Titulo**  
Anomalias: cuando el comportamiento se sale de patron

**Bullets**
- No todo se detecta con umbrales fijos
- Lo raro puede ser mas importante que lo alto
- El contexto multivariable importa

**Notas del orador**  
Explica que algunas fallas emergen como combinaciones extrañas, no solo como un valor muy grande. Esa es la puerta de entrada a metodos de deteccion de anomalias que miran relaciones entre variables.

**Referencia practica del curso**  
`05_ia_predictiva/IV_07_anomalias_y_rul.ipynb`

### Diapositiva 40
**Titulo**  
Z-score: una forma simple de detectar rareza

**Bullets**
- Compara el valor con su promedio
- Considera la dispersion natural
- Alerta si se aleja demasiado

**Notas del orador**  
Presenta el Z-score como una regla estadistica sencilla. Si el valor actual esta muy lejos de lo normalmente esperado, algo merece revision. Sirve para introducir pensamiento estadistico sin complicar demasiado la clase.

**Referencia practica del curso**  
`05_ia_predictiva/IV_07_anomalias_y_rul.ipynb`

### Diapositiva 41
**Titulo**  
Isolation Forest: detectar combinaciones extrañas

**Bullets**
- Mira varias variables juntas
- Detecta patrones poco comunes
- Ayuda cuando una sola señal no basta

**Notas del orador**  
Usa una explicacion intuitiva: un punto anomalo es facil de aislar del resto porque se comporta diferente. Lo importante aqui no es el detalle matematico, sino la idea de detectar eventos raros en escenarios multivariables.

**Referencia practica del curso**  
`05_ia_predictiva/IV_07_anomalias_y_rul.ipynb`

### Diapositiva 42
**Titulo**  
RUL: vida util remanente

**Bullets**
- Cuanto tiempo queda antes de intervenir
- Traduce sensores en ventana de accion
- Facilita planificacion de mantenimiento

**Notas del orador**  
Esta es una de las ideas mas poderosas para un supervisor porque traduce una señal tecnica a tiempo de decision. No se trata solo de decir que hay riesgo, sino de estimar si se puede esperar, inspeccionar pronto o parar en la siguiente ventana.

**Referencia practica del curso**  
`05_ia_predictiva/IV_07_anomalias_y_rul.ipynb`

### Diapositiva 43
**Titulo**  
RUL bajo: que haria un supervisor

**Bullets**
- Menos de 72 h: planificar inspeccion
- Validar con vibracion y contexto operativo
- Cruzar con ventana de parada

**Notas del orador**  
Convierte la prediccion en accion concreta. El alumno debe salir viendo que un numero de RUL es una ayuda para decidir prioridades, coordinar recursos y reducir improvisacion, no un oraculo perfecto.

**Referencia practica del curso**  
`05_ia_predictiva/IV_07_anomalias_y_rul.ipynb`

### Diapositiva 44
**Titulo**  
Pipeline integrado de alertas

**Bullets**
- Datos -> features -> modelo
- Modelo -> probabilidad de falla
- Probabilidad + RUL -> riesgo
- Riesgo -> priorizacion

**Notas del orador**  
Vuelve a unir todas las piezas. La fortaleza del enfoque no es solo tener un algoritmo, sino convertir datos historicos en un flujo operativo repetible que termina en una lista priorizada de acciones.

**Referencia practica del curso**  
`05_ia_predictiva/IV_08_caso_integrado_alertas.ipynb`

### Diapositiva 45
**Titulo**  
Pareto: no todas las alertas son iguales

**Bullets**
- Ordenar por riesgo
- Enfocarse primero en el mayor impacto
- Priorizar top 20 por ciento

**Notas del orador**  
Explica que en la vida real no se atiende todo a la vez. Pareto ayuda a enfocar tiempo y recursos donde el riesgo acumulado es mayor. Esto es muy comprensible para roles de supervision y planificacion.

**Referencia practica del curso**  
`05_ia_predictiva/IV_08_caso_integrado_alertas.ipynb`

### Diapositiva 46
**Titulo**  
PUMP101: del dato a la accion

**Bullets**
- Export de PI o datos simulados
- Limpieza y features en Python
- Score de riesgo y RUL
- Lista priorizada para mantenimiento

**Notas del orador**  
Haz un resumen ejecutivo del caso integrado para que el alumno vea la pelicula completa. Esta diapositiva muestra el valor del curso: entender y reproducir mentalmente el paso desde dato bruto hasta accion sugerida.

**Referencia practica del curso**  
`05_ia_predictiva/IV_08_caso_integrado_alertas.ipynb`

### Diapositiva 47
**Titulo**  
Limites y buenas practicas

**Bullets**
- Basura entra, basura sale
- Validar con expertos de planta
- No confiar en una sola variable
- La IA complementa, no reemplaza

**Notas del orador**  
Esta diapositiva es clave para no sobredimensionar la tecnologia. Un buen curso de analitica debe incluir criterio, validacion y humildad tecnica. El mejor resultado es un supervisor que pregunta mejor y decide mejor, no uno que confia ciegamente en un modelo.

**Referencia practica del curso**  
`05_ia_predictiva/IV_08_caso_integrado_alertas.ipynb`

### Diapositiva 48
**Titulo**  
Como se trabajara en Colab

**Bullets**
- Abrir notebook correspondiente
- Ejecutar celdas en orden
- Revisar graficos y tablas
- Relacionar salida con la teoria

**Notas del orador**  
Usa esta diapositiva como puente practico. Explica que cada notebook fue pensado para reforzar la teoria: primero se ve el concepto en slides y luego se observa en datos, tablas, graficos y outputs reales del curso.

**Referencia practica del curso**  
`00_python_para_ingenieros/00_01_bienvenida_y_entorno.ipynb`

### Diapositiva 49
**Titulo**  
Ruta practica sugerida para la sesion 2

**Bullets**
- IV_05: escalera y features
- IV_06: clasificacion y metricas
- IV_07: anomalias y RUL
- IV_08: scoring y Pareto
- IV_03/IV_04: SQL y pipeline hacia dataset BI
- `script_seed_supabase.py` + export CSV para Power BI

**Notas del orador**  
Esta diapositiva ayuda a conducir el laboratorio y a que el alumno vea la logica del orden. Cada notebook prepara al siguiente. No conviene saltar directamente al pipeline final sin haber construido antes el lenguaje comun de features, riesgo y deterioro.

**Referencia practica del curso**  
`05_ia_predictiva/README_modulo_ia.md`

### Diapositiva 50
**Titulo**  
Transición: de IA a Power BI + Supabase (práctico)

**Bullets**
- Ya puedes generar riesgo predictivo con IA
- Ahora lo conectamos a un dashboard para jefatura
- Creas tablas en Supabase, cargas datos y exportas CSV para Power BI
- Luego interpretas el riesgo con contexto operativo (PUMP101)

**Notas del orador**  
Esta diapositiva funciona como “puente operativo”. Hasta aquí el foco fue entender y predecir; a partir de ahora el foco es el ecosistema que permite que esa información viva en un dashboard para supervisión.

**Referencia practica del curso**  
`04_ecosistema_datos/powerbi/instrucciones_dashboard.md`

### Diapositiva 51
**Titulo**  
Bloque Supabase + Power BI: del dato central al dashboard

**Bullets**
- Objetivo: exportar datos listos para jefatura
- Paso a paso: schema -> seed -> export CSV -> Power BI
- Puente: lo que ves en BI también ayuda a interpretar IA

**Notas del orador**  
En esta parte hacemos visible el “circuito operativo” que normalmente queda escondido detrás de dashboards. Verás qué tablas existen, cómo se cargan y cómo Python deja un CSV para Power BI. Ese mismo flujo sostiene la trazabilidad.

**Referencia practica del curso**  
`04_ecosistema_datos/README_modulo_ecosistema.md`

### Diapositiva 52
**Titulo**  
Tablas mínimas en Supabase (qué guarda cada una)

**Bullets**
- `equipos`: equipos, área y tipo
- `lecturas_pi`: timestamp, tag, valor, unidad, quality
- `eventos_mantenimiento`: inicio/fin, modo_falla, MTTR

**Notas del orador**  
El modelo de datos es intencional: lecturas (series) separadas de eventos (mantenimiento) y conectadas por el equipo. Esto evita inconsistencias cuando calculas KPIs y luego interpretas alertas.

**Referencia practica del curso**  
`04_ecosistema_datos/sql/schema_supabase.sql`

### Diapositiva 53
**Titulo**  
Cómo crear el esquema en Supabase (DDL + RLS)

**Bullets**
- Abre Supabase -> SQL Editor
- Ejecuta `schema_supabase.sql`
- Verifica tablas + índices + políticas RLS del curso

**Notas del orador**  
No es necesario memorizar SQL: lo importante es que exista un “contrato” de estructura para que el pipeline sea repetible. En producción, RLS y permisos controlan quién puede leer/escribir.

**Referencia practica del curso**  
`04_ecosistema_datos/sql/schema_supabase.sql`

### Diapositiva 54
**Titulo**  
Poblar Supabase con datos simulados (seed)

**Bullets**
- Configura `04_ecosistema_datos/.env` (URL/KEY)
- Ejecuta `script_seed_supabase.py`
- Inserta: equipos -> lecturas_pi -> eventos_mantenimiento

**Notas del orador**  
Esta etapa reemplaza el “estar conectado a PI en vivo” durante el curso. Pedagogicamente, el objetivo es que entiendas el flujo técnico completo y puedas repetirlo sin depender de un historiador real.

**Referencia practica del curso**  
`04_ecosistema_datos/script_seed_supabase.py`

### Diapositiva 55
**Titulo**  
Validación rápida con SQL: mínimos para confiar

**Bullets**
- COUNT de lecturas con `quality = 'GOOD'`
- Top tags por volumen/periodo
- JOIN de equipos con eventos (si aplica)

**Notas del orador**  
Evita el error típico: construir un dashboard sobre datos incompletos o con calidad deficiente. El supervisor debe confiar por evidencia, no por intuición.

**Referencia practica del curso**  
`04_ecosistema_datos/IV_03_sql_supabase.ipynb`

### Diapositiva 56
**Titulo**  
Export para Power BI desde Supabase

**Bullets**
- CSV listo para importar: `dashboard_fuente_supabase.csv`
- Export diario con mean (coherente con el dataset del curso)
- Equipo derivado del prefijo de `tag` (PUMP101.*, MILL201.*)

**Notas del orador**  
En esta clase el camino práctico es: SQL -> export CSV -> Power BI. En arquitectura productiva podrías conectar Power BI directo a Supabase, pero el CSV mantiene reproducibilidad y simplicidad.

**Referencia practica del curso**  
`04_ecosistema_datos/export_supabase_to_powerbi.py`

### Diapositiva 57
**Titulo**  
Ejecutar el export (ejemplo)

**Bullets**
- `uv run python 04_ecosistema_datos/export_supabase_to_powerbi.py --days 30`
- Ajusta `--page-size` si hay volumen alto
- Verifica el CSV: `Timestamp,Tag,Valor,Equipo`

**Notas del orador**  
La meta es que el alumno (o su equipo) pueda regenerar el dataset y no dependa de alguien que “ya lo dejó listo”.

**Referencia practica del curso**  
`04_ecosistema_datos/export_supabase_to_powerbi.py`

### Diapositiva 58
**Titulo**  
Importar a Power BI Desktop (tendencia + KPI)

**Bullets**
- Importar CSV `dashboard_fuente_supabase.csv`
- Convertir `Timestamp` a tipo Fecha
- Visual 1: tendencia temporal
- Visual 2: tarjeta KPI

**Notas del orador**  
Usa `instrucciones_dashboard.md` como checklist. La meta aquí no es aprender DAX, sino construir visuals útiles para supervisión.

**Referencia practica del curso**  
`04_ecosistema_datos/powerbi/instrucciones_dashboard.md`

### Diapositiva 59
**Titulo**  
Visuales mínimos recomendados para jefatura

**Bullets**
- Tendencia por `Tag`/`Equipo`
- Filtros: equipo y periodo
- Tarjeta KPI: vibración/temperatura (según tag)

**Notas del orador**  
Un dashboard útil responde preguntas rápidas: “¿sube/baja?”, “¿en qué equipo?” y “¿desde cuándo?”. Lo demás es secundario para supervisión.

**Referencia practica del curso**  
`04_ecosistema_datos/powerbi/instrucciones_dashboard.md`

### Diapositiva 60
**Titulo**  
KPIs que conectan BI con mantenimiento

**Bullets**
- Calidad de dato (GOOD/BAD) -> confiabilidad
- Promedio/pico -> condición del activo
- Eventos de mantenimiento -> contexto operativo

**Notas del orador**  
El supervisor interpreta una desviación como degradación real o como ruido considerando la calidad y el contexto de eventos. Esa combinación es lo que vuelve la decisión robusta.

**Referencia practica del curso**  
`04_ecosistema_datos/IV_02_excel_y_powerbi.ipynb`

### Diapositiva 61
**Titulo**  
Demo local vs arquitectura productiva (cambia el origen)

**Bullets**
- Demo: `script_seed_local.py` genera CSV + SQLite -> `dashboard_fuente.csv` -> Power BI (import CSV)
- Productivo: PI -> Python ETL -> Supabase -> dataset/dashboard
- Fuente única para trazabilidad y reporting

**Notas del orador**  
Deja claro el “pattern” mental. En el curso trabajas con datos simulados; en planta, el mismo patrón opera con datos reales provenientes del proceso/PI.

**Referencia practica del curso**  
`04_ecosistema_datos/IV_04_pipeline_python_datos.ipynb`

### Diapositiva 62
**Titulo**  
Calidad de datos: el filtro antes de alarmas

**Bullets**
- Filtrar `quality = GOOD`
- Documentar reglas de limpieza
- Validar interpretaciones con mantenimiento

**Notas del orador**  
Si la calidad está mal, el dashboard puede “verse correcto” y aun así conducir a mala decisión. La calidad es una condición de negocio, no solo técnica.

**Referencia practica del curso**  
`00_python_para_ingenieros/00_08_intro_pandas_planta.ipynb`

### Diapositiva 63
**Titulo**  
Puente hacia IA: BI muestra contexto, IA estima riesgo

**Bullets**
- IA necesita datos confiables y consistentes
- En el curso: IA usa dataset predictivo generado (IV_05-08)
- En planta: features se construyen desde lecturas almacenadas en Supabase

**Notas del orador**  
No prometas que la IA “sale directo del dashboard”. BI ayuda a ver tendencia y contexto; la IA y el modelado crean priorización. Ambos descansan en una base de datos consistente.

**Referencia practica del curso**  
`05_ia_predictiva/IV_05_mantenimiento_predictivo.ipynb`

### Diapositiva 64
**Titulo**  
De dashboard a decisión operativa

**Bullets**
- Dashboard: detectar tendencia y equipos críticos
- IA: estimar riesgo y apoyo a priorización (RUL/alertas)
- Acción: programar inspección y ventana de parada

**Notas del orador**  
El flujo final es humano. El modelo ayuda, pero la validación y ejecución corresponden a mantenimiento y operación con criterio.

**Referencia practica del curso**  
`05_ia_predictiva/IV_08_caso_integrado_alertas.ipynb`

### Diapositiva 65
**Titulo**  
Cierre del curso (7h): end-to-end listo para supervisión

**Bullets**
- Explicar el viaje del dato: sensores -> decisión
- Crear tablas y cargar Supabase con scripts
- Exportar CSV e importar a Power BI
- Usar IA predictiva para priorizar alertas (PUMP101)

**Notas del orador**  
Cierra alineando los logros esperados a una ruta real: arquitectura, datos centralizados, visualización y priorización. Deja como siguiente nivel profundizar integración productiva con PI/API y refresh automatizado.

**Referencia practica del curso**  
`GUIA_MAPA_CURSO_MINERIA50.md`

---

## Anexos para enriquecer la presentacion

### Diagrama sugerido 1 — Viaje del dato

Usa un diagrama horizontal con esta secuencia:

`Sensor -> PLC -> SCADA/DCS -> PI Historian -> Python ETL -> Supabase -> Power BI -> Alerta -> Decision de mantenimiento`

### Diagrama sugerido 2 — Escalera de mantenimiento

Usa cuatro niveles ascendentes:

- Reactivo
- Preventivo
- Predictivo
- Prescriptivo

Con un ejemplo de PUMP101 en cada nivel.

### Diagrama sugerido 3 — Pipeline predictivo

Usa esta secuencia:

`Datos crudos -> limpieza -> features -> modelo ML -> probabilidad de falla -> RUL -> Pareto -> accion`

## Tabla de mapeo entre teoria y notebooks

| Bloque teorico | Notebook de apoyo |
|---|---|
| Vision general y flujo OT/IT | `04_ecosistema_datos/IV_01_flujo_datos_mineria50.ipynb` |
| Introduccion a Python y Colab | `00_python_para_ingenieros/00_01_bienvenida_y_entorno.ipynb` |
| Variables y unidades | `00_python_para_ingenieros/00_02_variables_y_unidades.ipynb` |
| Logica de alarmas | `00_python_para_ingenieros/00_05_condicionales.ipynb` |
| CSV, calidad y tendencia | `00_python_para_ingenieros/00_08_intro_pandas_planta.ipynb` |
| PI Historian, tags y quality | `01_PI_historiador_introduccion/clase_01_PI_historiador_introduccion.md` |
| Escalera de mantenimiento | `05_ia_predictiva/IV_05_mantenimiento_predictivo.ipynb` |
| Random Forest y metricas | `05_ia_predictiva/IV_06_ml_clasificacion_fallas.ipynb` |
| Anomalias y RUL | `05_ia_predictiva/IV_07_anomalias_y_rul.ipynb` |
| Pipeline de alertas | `05_ia_predictiva/IV_08_caso_integrado_alertas.ipynb` |

## Guion corto de transicion a Colab

Despues de explicar la teoria de cada bloque, usa transiciones como estas:

- "Ahora abrimos Colab para ver este concepto en datos reales simulados."
- "Lo que acabamos de ver como idea, ahora lo veremos en una tabla y un grafico."
- "Primero entiendan la logica; luego miraremos como Python la ejecuta."
- "No se trata de programar por programar, sino de entender como el dato se convierte en decision."

## Temas que puedes mencionar como continuidad, pero no desarrollar mucho en esta presentacion

- PI Asset Framework
- MTBF / MTTR a detalle
- Supabase en vivo
- Power BI en vivo
- Weibull
- Vibracion avanzada ISO 10816
- Machine learning multivariable mas profundo

## Prompt final corto para pegar en Gemini

Genera una presentacion en espanol de 65 diapositivas basada exactamente en el contenido anterior. La audiencia es un supervisor de planta concentradora con base en Excel y Power BI basico. Mantiene un tono docente, industrial y claro. Respeta la estructura de cada slide con titulo, bullets, notas del orador y referencia practica del curso. No uses demasiado texto por slide. Mantiene a Python como el centro del pipeline de Mineria 5.0 y desarrolla con claridad el flujo completo desde sensores hasta alertas predictivas, usando a PUMP101 como caso central e incluyendo el flujo practico de Supabase (tablas + carga) y export hacia Power BI.
