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

Para cargar información en un DataFrame, se pueden utilizar archivos CSV, JSON, Excel, entre otros.

```python
In [1]: import pandas

In [2]: from pandas.io.excel import ExcelWriter 

In [3]: csv_file = pandas.read_csv("hoteles.csv")

In [4]: csv_file
Out[4]: 
                                               name   price  rating
0                                      Hotel Darcet  2160.0     4.5
1    Holiday Inn Express Paris-Canal de la Villette  2828.0     4.0
2                                    Atlantic Hôtel  3731.0     4.5
3                         Hôtel Odessa Montparnasse  2514.0     4.0
4                                     Hôtel Virgina  5204.0     4.0
..                                              ...     ...     ...
175                  Contact Hotel Alize Montmartre  3731.0     4.0
176                      Melia Paris Champs Elysees  5210.0     4.0
177    Hotel Etoile Saint-Ferdinand by HappyCulture  3692.0     4.0
178                                     Hotel Doisy  4399.0     4.5
179                                    Villa Brunel  3339.0     4.0

[180 rows x 3 columns]

In [5]: with ExcelWriter('hoteles.xlsx') as ew:  # Datos en Excel
   ...:     csv_file.to_excel(ew) 
   ...:   

In [6]: csv_file.to_json('hoteles.json')  # Datos a JSON
```

### Mostrando datos

Pandas puede mostrar datos con Matplotlib, de forma sencilla dada su integración con el mismo.

```python
In [10]: df = pandas.read_csv('hoteles.csv')

In [11]: df.sort_values(['rating', 'price'])                                                                                                                                                                           
Out[11]: 
                                 name    price  rating
25             BVJ Opera Youth Hostel    839.0     4.0
114                       Zazie Hotel   1591.0     4.0
32        Libertel Canal Saint-Martin   1750.0     4.0
12   Auberge de Jeunesse MIJE  Fourcy   1871.0     4.0
56                District République   1905.0     4.0
..                                ...      ...     ...
119           Mandarin Oriental Paris  22558.0     5.0
148               Hôtel Plaza Athénée  26413.0     5.0
145               The Peninsula Paris  26511.0     5.0
27        Four Seasons Hotel George V  27682.0     5.0
118                  Le Bristol Paris  29457.0     5.0

[180 rows x 3 columns]

In [12]: df.plot(title='Hoteles')  # Mostrando datos
Out[12]: <matplotlib.axes._subplots.AxesSubplot at 0x12c772310>

In [25]: plt.get_figure().savefig('hoteles.png')  # Guardando datos
```