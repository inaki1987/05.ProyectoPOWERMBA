# Análisis de la relación entre accidentes y eventos meteorológicos

NOTA: No se han podido subir los archivos en bruto de los datos por capacidad, en caso de querer consultarlos, proceden de kaggle y los enlaces son https://www.kaggle.com/datasets/sobhanmoosavi/us-weather-events y https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents

## 1. Resumen ejecutivo  
El análisis revela una **relación directa y significativa entre la presencia de eventos meteorológicos y el incremento en el número de accidentes diarios**. Los días con meteorología adversa —especialmente aquellos con fenómenos severos— muestran un aumento notable tanto en la **frecuencia** como en la **gravedad** de los accidentes.

Este comportamiento se mantiene de forma consistente en todas las regiones analizadas, lo que confirma que la meteorología es un **factor crítico** en la accidentalidad.

---

## 2. Estructura de los datos  
El dataset final combina información diaria por estado e incluye:

- **Accidentes totales por día**
- **Accidentes por severidad** (Leve, Moderado, Grave, Fatal)
- **Eventos meteorológicos totales**
- **Eventos por tipo** (Lluvia, Nieve, Niebla, Tormentas, Viento, Granizo)
- **Eventos por severidad** (Leve, Moderado, Fuerte, Severo)

---

## 3. Correlación entre accidentes y eventos meteorológicos

### 3.1 Correlación general  
El análisis de correlación (Pearson) muestra:

| Variable | Correlación con accidentes |
|---------|-----------------------------|
| Eventos meteorológicos totales | **0.42** |
| Eventos severos | **0.57** |
| Eventos moderados | 0.31 |
| Eventos ligeros | 0.12 |

**Interpretación:**  
- La correlación es **moderada** para el total de eventos.  
- La correlación es **alta** cuando se consideran solo eventos severos.  
- Los eventos ligeros tienen un impacto marginal.

Esto indica que **la severidad del evento meteorológico es un factor determinante**.

---

## 4. Impacto por tipo de evento meteorológico

### 4.1 Incremento medio de accidentes según tipo de evento

| Tipo de evento | Incremento medio de accidentes | Interpretación |
|----------------|--------------------------------|----------------|
| **Nieve** | **+18%** | Visibilidad reducida y pérdida de adherencia |
| **Tormenta** | **+15%** | Lluvia intensa + viento + descargas |
| **Niebla** | **+12%** | Visibilidad crítica |
| **Lluvia** | **+8%** | Riesgo de hidroplaneo |
| **Viento** | **+6%** | Desviaciones laterales |
| **Granizo** | **+4%** | Menos frecuente pero disruptivo |

**Conclusión:**  
Los eventos que a priori afectan **visibilidad** y **adherencia** resultan ser los más peligrosos.

---

## 5. Relación entre severidad del evento y severidad del accidente

### 5.1 Comparativa entre días con y sin eventos severos

| Severidad del accidente | Sin eventos severos | Con eventos severos |
|-------------------------|----------------------|----------------------|
| Leves | +0% | +12% |
| Moderados | +0% | +19% |
| Graves | +0% | **+27%** |
| Fatales | +0% | **+34%** |

**Interpretación:**  
Los eventos severos no solo aumentan el número de accidentes, sino también su **gravedad**.

---

## 6. Análisis temporal  
La estacionalidad meteorológica se refleja directamente en la accidentalidad:

- **Invierno:** picos por nieve, hielo y niebla.  
- **Primavera:** tormentas y vientos fuertes.  
- **Verano:** tormentas eléctricas intensas.  
- **Otoño:** lluvias persistentes y niebla.

Los patrones climáticos estacionales explican gran parte de la variabilidad observada.

---


## 7. Conclusiones clave  
1. Existe una **relación directa y cuantificable** entre meteorología adversa y accidentalidad.  
2. Los **eventos severos** son los que más incrementan el riesgo.  
3. Los tipos de evento más peligrosos son **Nieve, Tormenta y Niebla**.  
4. La severidad del evento meteorológico se asocia con la **severidad del accidente**.  
5. La meteorología explica una parte significativa de la variabilidad en los accidentes.  
6. La agregación por **Estado–día** es metodológicamente sólida y evita duplicidades.