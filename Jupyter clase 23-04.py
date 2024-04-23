#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install pandas


# In[1]:


import pandas as pd


# In[3]:


#Crear una serie: arreglo unidimencional de datos.
miSerie = pd.Series([43, 76, 78, 23, 34])
miSerie


# In[5]:


# Diccionario en Python

miDiccionario = {
    "Nombre":"Casa_1",
    "Area":120,
    "Baños":3,
    "Propietarios": [
        "Paulo", "Diana", "Sonia"
    ],
    "Barrio" : {
        "Nombre": "Gran Britalia",
        "Localidad":"Bosa"
    }
}
miDiccionario


# Data frame: Estructura de datos en formato tabla
# La forma mas "simple" de crear un dataframe es apartir de un diccionario, otra forma puede ser desde hojas de calculo, dede archivos JSON o desde archivos CSV (Valores separados por comas)

# In[8]:


miDataframe = pd.DataFrame({"Si": [10,15], "No":[50, 68]})
miDataframe


# In[ ]:




