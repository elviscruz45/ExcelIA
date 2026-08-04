# Clase 02 — PI Asset Framework

## Contexto industrial

PI Asset Framework (AF) organiza activos en jerarquías: Planta → Área → Equipo → Componente. Cada sensor PI se asocia a un nodo del árbol de activos.

## Conceptos clave

- **Asset Path:** Ruta jerárquica del activo.
- **Template:** Modelo reutilizable de activo con atributos y tags.
- **Roll-up:** Agregación de KPIs por nivel de jerarquía.

## Objetivos de aprendizaje

1. Relacionar tags PI con componentes del activo.
2. Agrupar mediciones por componente.
3. Construir un dashboard multi-tag.

## Pasos del laboratorio

1. Regenerar datos con `script_generacion.py`.
2. Ejecutar el notebook completo.
3. Analizar el resumen por componente en `outputs/resultado_analisis.csv`.

## Preguntas de reflexión

- ¿Cómo estructurarías AF para una línea de 10 bombas idénticas?
- ¿Qué ventaja tiene el roll-up de vibración a nivel de área?
