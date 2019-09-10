## Ejemplo 04
## Pandas

Es una librería con estruturas de datos y análisis de los mismos. Se instala de la misma manera que las otras liberías, con Pip

```
pip install pandas
```

Puede obtener información desde:
* Bases de datos SQL, tablas estructuradas o archivos de Excel.
* Datos ordenados y desordenados con información en tiempo.
* Conjuntos de datos estadísticos y observacionales.

Sus datos se dividen en dos formas: Series y DataFrame.

`series_dataframe.py`

```python
In [1]: import numpy as np

In [2]: import pandas as pd

In [3]: s = pd.Series([1, 2, 4.5, np.nan, 6, 8, 20/11])

In [4]: s  # Series es para datos de una dimensión
Out[4]: 
0    1.000000
1    2.000000
2    4.500000
3         NaNd
4    6.000000
5    8.000000
6    1.818182
dtype: float64

In [6]: dates = pd.date_range('20130101', periods=6)

In [7]: dates
Out[7]: 
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')

In [8]: df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

In [9]: df
Out[9]: 
                   A         B         C         D
2013-01-01  0.126040  1.712168 -0.165948 -1.363206
2013-01-02  0.055530  0.913652  0.318734  0.211450
2013-01-03 -0.225969 -0.222985  0.840756  0.418775
2013-01-04 -1.128968 -0.989637  0.086524 -1.812489
2013-01-05 -0.040648  0.106741  1.976037  0.187990
2013-01-06 -1.330647 -1.076811 -0.354355 -0.526739

```

### Cargando datos

PAra cargar información en un DataFrame, se pueden utilizar archivos CSV, JSON, Excel, entre otros.

``
