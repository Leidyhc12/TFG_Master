# TFG_Master
Code created to replicate the methodology and verify the progress of the entire TFG process

# Modelo reproducible de cooperación educativa en Colombia — ODS 4

Este repositorio contiene el código y la base utilizados para reproducir el análisis de cooperación internacional no reembolsable asociada al ODS 4 en Colombia, para el periodo de registro 2015–2024. Se desarrolla como soporte metodológico del trabajo de grado sobre sostenibilidad financiera de programas de educación inclusiva.

## Archivos

| Archivo | Función |
|---|---|
| `Modelo_Tesis_APC.ipynb` | Notebook principal con el procedimiento y las explicaciones. |
| `Data Tesis.xlsx` | Base de entrada de APC-Colombia; debe conservar la hoja `Data` y los encabezados originales. |
| `ejecutar_modelo.py` | Ejecuta las celdas del notebook en orden y verifica los indicadores de referencia. |
| `requirements.txt` | Versiones de las librerías para reproducir el entorno. |
| `.github/workflows/ejecutar-modelo.yml` | Ejecución manual mediante GitHub Actions. |
| `Colab_VF (1).ipynb` | Versión anterior; se conserva como antecedente, no es el punto de entrada actualizado. |

## Ejecutar dentro de GitHub

1. Abrir la pestaña **Actions** del repositorio.
2. Seleccionar **Ejecutar modelo de tesis**.
3. Pulsar **Run workflow**, seleccionar `main` y confirmar.
4. Abrir la ejecución y esperar a que termine.
5. En **Artifacts**, descargar `resultados-tesis-apc`.

El flujo debe estar guardado en la rama predeterminada. Para iniciarlo se requiere acceso de escritura al repositorio y que GitHub Actions esté habilitado. Los visitantes pueden usar Colab. Los resultados se conservan como artefactos durante 30 días; no se incorporan automáticamente a la lista de archivos del repositorio. Una ejecución fallida requiere revisar el registro y la hoja `Reproducibilidad` del Excel, si llegó a generarse.

La pestaña Preview muestra el notebook, pero no ejecuta Python. GitHub Actions realiza el cálculo completo sin intervención en las celdas.

## Ejecutar en Google Colab

[Abrir el modelo en Google Colab](https://colab.research.google.com/github/Leidyhc12/TFG_Master/blob/main/Modelo_Tesis_APC.ipynb)

1. Abrir el enlace y conectar el entorno.
2. Para usar las versiones declaradas, ejecutar en una celda inicial: `%pip install numpy==2.3.5 pandas==2.2.3 matplotlib==3.10.8 openpyxl==3.1.5`. Si Colab solicita reiniciar la sesión, hacerlo antes de continuar.
3. Ejecutar todas las celdas del notebook en orden.
4. La base se descarga automáticamente del repositorio público si no existe en el directorio de trabajo.
5. Revisar la tabla de reproducibilidad: todos los indicadores deben figurar como `OK`.
6. Al finalizar se ofrece la descarga de `Modelo_Tesis_APC_Resultados.zip`.

## Ejecutar en un equipo local

Requiere Python 3.11. Desde la carpeta del repositorio:

```bash
python -m pip install -r requirements.txt
python ejecutar_modelo.py
```

El modelo usa primero el archivo local `Data Tesis.xlsx`. Si no existe, intenta descargarlo de la rama `main`. Si se desea reproducir una versión histórica, descargar el código y la base del mismo commit y ejecutarlos juntos; la descarga desde `main` podría corresponder a una versión posterior.

## Fuente y trazabilidad

Fuente: Agencia Presidencial de Cooperación Internacional de Colombia (APC-Colombia). El archivo utilizado es `Data Tesis.xlsx`, hoja `Data`.

- Enlace exacto de origen o mecanismo de obtención de la base: https://www.datos.gov.co/Funci-n-p-blica/RECURSOS-DE-COOPERACI-N-INTERNACIONAL-NO-REEMBOLSA/2d3i-f9wd/explore/query/SELECT%0A%20%20%60codigo_intervencion%60%2C%0A%20%20%60fecha_registro_intervencion%60%2C%0A%20%20%60nombre_intervencion%60%2C%0A%20%20%60objetivo_general%60%2C%0A%20%20%60fecha_inicial%60%2C%0A%20%20%60fecha_final%60%2C%0A%20%20%60estado_intervencion%60%2C%0A%20%20%60modalidad_cooperacion%60%2C%0A%20%20%60plan_nacional_desarrollo%60%2C%0A%20%20%60hoja_ruta%60%2C%0A%20%20%60ods%60%2C%0A%20%20%60sectores_gobierno%60%2C%0A%20%20%60nombre_del_actor%60%2C%0A%20%20%60tipo_de_actor%60%2C%0A%20%20%60pais_del_actor%60%2C%0A%20%20%60rol_del_actor%60%2C%0A%20%20%60tipo_de_asistencia%60%2C%0A%20%20%60monto_aporte_en_usd%60%2C%0A%20%20%60es_adicion%60%2C%0A%20%20%60total_territorios%60/page/filter
- Fecha de descarga o recepción de la base: Julio 2026

La fecha de carga a GitHub no sustituye la fecha de obtención de la fuente. El periodo 2015–2024 corresponde al filtro analítico; la base original incluye registros fuera de ese periodo.

## Procedimiento metodológico

1. Validar las columnas de la base original.
2. Filtrar por fecha de registro entre 2015 y 2024 y por ODS 4.
3. Conservar cada código de intervención distinto como una unidad independiente.
4. Identificar aportes únicos por código, actor, rol, tipo de asistencia, monto y condición de adición.
5. Confirmar montos positivos asociados a donantes internacionales explícitos.
6. Calcular concentración por intervención y grupo de donante: Gini, HHI, Top 3, Top 5 y participación de intervenciones de al menos USD 500.000.
7. Construir la serie anual por año de registro y escenarios de reducción de aportes del Top 3.
8. Preseleccionar el núcleo de educación inclusiva mediante reglas textuales y exportar la matriz para revisión humana.

## Valores de referencia

| Indicador | Referencia aproximada |
|---|---:|
| Registros originales | 43.105 |
| Registros 2015–2024 | 36.864 |
| Filas ODS 4 | 1.186 |
| Intervenciones ODS 4 | 274 |
| Intervenciones con monto confirmado | 269 |
| Aportes internacionales únicos | 354 |
| Valor confirmado | USD 111.251.610,67 |
| Gini financiero | 0,778411 |
| HHI por grupo de donante | 0,151190 |
| Participación Top 3 | 58,2372 % |
| Participación Top 5 | 72,5465 % |
| Intervenciones de al menos USD 500.000 | 30 |
| Participación de estas intervenciones | 75,4500 % |

Los valores esperados se utilizan únicamente para contrastar el resultado calculado. El modelo calcula los indicadores desde el Excel; no reemplaza los resultados por estas referencias.

## Productos generados

En `resultados_tesis_apc/`:

- `Resultados_Modelo_Tesis_APC.xlsx`: resumen, embudo, intervenciones, aportes, donantes, serie anual, ranking, pruebas de estrés, núcleo preliminar y verificación de reproducibilidad.
- `Revision_Manual_Nucleo_Inclusivo.csv`: matriz de revisión humana.
- `Indicadores_Principales.json`: indicadores principales.
- `graficas/`: curva de Lorenz, principales donantes, pruebas de estrés y serie anual.

## Alcance y limitaciones

- La serie anual representa valores asociados a registros administrativos; no debe interpretarse como desembolsos efectivos o flujos de caja anuales.
- Las cinco intervenciones sin monto atribuible permanecen en el universo temático y no se tratan como intervenciones de valor cero para calcular el Gini.
- La preselección de educación inclusiva requiere validación humana; no constituye una clasificación definitiva. El notebook exporta la matriz, pero no incorpora automáticamente las decisiones manuales posteriores.
- Las pruebas de estrés son escenarios hipotéticos de exposición, no pronósticos ni estimaciones causales del cierre de USAID.
- La verificación de reproducibilidad confirma coincidencia con la base y los indicadores de referencia; no sustituye la revisión metodológica de los criterios.

## Autoría y referencia

Responsable del repositorio: Leidy Dayana Hernández Cruz.

Repositorio: https://github.com/Leidyhc12/TFG_Master

Para referenciar una versión, registrar el título del modelo, autora, año, URL y el commit o versión utilizado.
