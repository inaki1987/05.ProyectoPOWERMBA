# Análisis de Accidentes de tráfico y Eventos Meteorológicos en Estados Unidos (2022)

## 1. Objetivo del proyecto
Explorar si existe relación entre los accidentes de tráfico y los eventos meteorológicos en Estados Unidos durante el año 2022, evaluando tanto la frecuencia como la severidad de ambos fenómenos.

---

## 2. Datasets utilizados

Los datos provienen de fuentes públicas y cubren información de accidentes y eventos meteorológicos en EE.UU.:

- **United States - Region Codes.csv**  
  Códigos y regiones administrativas de EE.UU.

- **US_Accidents_March23.csv**  
  Dataset de accidentes de tráfico en EE.UU. (Kaggle).

- **WeatherEvents_Jan2016-Dec2022.csv**  
  Dataset de eventos meteorológicos (Kaggle).

NOTA: No se han podido subir los archivos en bruto de los datos por capacidad, en caso de querer consultarlos, los enlaces son https://www.kaggle.com/datasets/sobhanmoosavi/us-weather-events y https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents

Tras el análisis preliminar, filtrado para el año 2022 y la limpieza, se generaron datasets combinados en:

- `Acc_met.csv`  
- `Acc_met_clean.csv`  


El dataset final combina información diaria por estado e incluye:

- **Accidentes totales por día**
- **Accidentes por severidad** (Leve, Moderado, Grave, Fatal)
- **Eventos meteorológicos totales**
- **Eventos por tipo** (Lluvia, Nieve, Niebla, Tormentas, Viento, Granizo)
- **Eventos por severidad** (Leve, Moderado, Fuerte, Severo)

---

## 3. Variables clave del análisis

### Accidentes
- `ACC_EVENTS`
- `ACC_SEV_LIGHT`
- `ACC_SEV_MODERATE`
- `ACC_SEV_HEAVY`
- `ACC_SEV_SEVERE`

### Clima
- `WEATHER_EVENTS`
- `WEA_SEV_LIGHT`
- `WEA_SEV_MODERATE`
- `WEA_SEV_HEAVY`
- `WEA_SEV_SEVERE`

### Tipos de evento meteorológico
- `TYP_COLD`
- `TYP_FOG`
- `TYP_HAIL`
- `TYP_PRECIPITATION`
- `TYP_RAIN`
- `TYP_SNOW`
- `TYP_STORM`

---

## 4.Gráficos incluidos en el análisis

Se incluyen todos los gráficos que aportan información real:

### Correlaciones
- Matriz de correlación  
- Dispersión ACC_EVENTS vs WEATHER_EVENTS  
- Correlación por severidad  
- Correlación por tipo de evento meteorológico  

### Impacto porcentual
- Incremento % por tipo de evento  
- Incremento % por severidad del accidente  

### Series temporales
- Accidentes vs eventos meteorológicos por mes   

### Otros
- Comparación de severidad de accidentes en días con y sin clima severo  
  

---

## 5.Metodología

1. **Carga y exploración inicial (EDA_Preliminar)** 
2. **Unión de datasets**   
    - Creación de columnas de recuento
    - Filtrado por año 2022  
3. **Limpieza de datos**  
    - Normalización tipos de datos 
    - Conversión de fechas  
4. **Análisis (EDA) y Visualización** 
  

---

## 6.Conclusiones principales

- La correlación diaria entre accidentes y clima es baja, pese a lo que la intución nos podría hacer pensar.  
- Sin embargo, las tendencias mensuales muestran patrones similares.  
- La niebla y el frío incrementan los accidentes más del 150%, siendo los eventos meteorológicos con mayor impacto relativo.  Sorprende el dato que los días con eventos de nieve, el numero de accidentes se reduce.
- La severidad del clima no determina la severidad del accidente,  aunque si produce un aumento porcentual significativo en todos los tipos de accidentes. Los eventos severos son raros, pero cuando ocurren incrementan el riesgo general.


---

# Próximos pasos

- Analizar impacto por estado o región.  
- Añadir datos de tráfico real.  
- Crear un dashboard interactivo incluyendo el estad o región

---





