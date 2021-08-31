# Proyecto2
El historico de medallas olímpicas desde 1896

En este proyecto me he decargado un DataSet del histórico de medallas olímpicas por países desde el año 1896.
He limpiado este DataFrame con las técnicas aprendidas en clase.
Además he complementado esta información "escrapeando" dos páginas webs distintas ya que el DataFrame inicial solo contaba con datos hasta el año 2012. Es por eso que he escrapeado para tener los datos del año 2016 (Río) y el año 2021 (Tokyo).
Por último, he realizado la visualización con gráficos para obtener el total de medallas de España desde el inicio de las olimpiadas y otro gráfico que nos muestra el ránking de países con más medallas (>500) a lo largo de todos los tiempos.

Para realizar este proyecto he importado algunas librerías:

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import seaborn as sns
import matplotlib.pyplot as plt

