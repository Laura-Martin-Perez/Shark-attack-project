import numpy as np


def delete_rows (df,col,s): 

#Elimina de un dataframe las filas que tengan un valor determinado en la columna determinada
#Parámetros: df: dataframe
#            col: columna
#            s: valor a buscar para eliminar la fila

#función para eliminar filas que tengan ciertos caracteres (s) en el valor de cierta columna (col) del dataframe (df)
# ~ es negacion
# isinstance para comprobar si es string o número (int, float)
# devuelve True si la comparacion es cierta y falso si no lo es
# al tener la negación, si se cumple y da True, se convierte en False y la elimina del dataframe

    return df[~df[col].apply(lambda value: True if (isinstance(value, str) and s in value) or (isinstance(value,(int,float)) and s == value) else False)]

def delete_rows_col (df, col, l_s):
# Devuelve un dataframe donde se elminan las filas que en las que la columna pasada por parámetro contengan los valores de la 
# lista pasada por parámetro. Llama a la función 'delete_rows'

#Parámetros: df: dataframe
#            col: columna
#            l_s: lista con los valore a buscar para eliminar la fila

    for s in l_s:
        df = delete_rows(df, col , s)
    return df

def clean_col(df,col,l_s):
    
# Devuelve una serie donde se reemplaza por los valores de la lista pasada por parametro, si este valor está
# en la columna pasada por parámetro
# Parámetros: df: dataframe
#            col: columna
#            l_s: lista de strings a buscar en cada valor de la columna para reemplazar por él mismo

    for s in l_s:
        df[col] = df[col].apply(lambda value: s if s in value else value)
        
    return df[col]


def replace_data(df,col,s,rs):

# Devuelve una serie donde se reemplaza el valor s pasado por parámetro por el valor rs pasado por parámetro
# Parámetros: df: dataframe
#            col: columna
#            s: dato a buscar para reemplazar, puede ser lista o string
#            rs : nuevo valor

    if isinstance(s,list):
        for v in s:
            df[col]=df[col].replace(v,rs)
    else:
        df[col] = df[col].replace(s,rs) 
        
    return df[col]


def col_groups (df, col, l_a, l_rg):
# Devuelve una serie donde se reasignan los valores de las lista pasada por parámetros de una columna determinada por los valores
# de otra lista pasada por parámetro
# Parámetros: df: dataframe
#             col: columna
#             l_a: lista de listas con los datos a buscar para reemplazar
#             l_rg : lista con los valores a reemplazar

    for i in range (len(l_rg)):
        for a in l_a[i]:
            df[col] = replace_data(df, col, a, l_rg[i])
            
    return df[col]

def other_injuries (df, col, l_rg, value):
    
# Devuelve una serie donde se reasignan los valores de una columna pasada por parámetro que no esten en la lista pasada por 
# parámetro por el valor 'value' pasado por parámetro
# Parámetros: df: dataframe
#             col: columna          
#             l_rg : lista con los valores donde buscar que no sean coincidentes
#             value : valor a asignar 
    
    for s in df[col].unique():
        if s not in l_rg:
            df[col] = replace_data(df,col,s,value)  
            
    return df[col]
           
          

def clean_age(df,col,l_s,pos):

# Devuelve una serie donde se reasignan los valores de una columna determinada dividiendo el string del valor por los datos 
# pasados por parámetro s y dejando los de la posición indicada por parámetro.
# Parámetros: df: dataframe
#             col: columna
#             s: datos a buscar para dividir el valor
#             pos: posición escogida
            
    for s in l_s:
        df[col] = [str(value).split(s)[pos].rstrip() if (value is not np.nan and s in value) else value for value in df[col]]
    return df[col]

def mean_vs_median_age_sex (df, col):
# Devuelve la media y la mediana de la columna 'age' del dataframe (pasados por parámetro) por sexo (valores de la columna 'sex') 
# Parámetros: df: dataframe
#            col: columna
    
# Media de edad de sex = 'M'
    mean_M = int(df[df.sex == 'M'].age.apply(int).mean())
# Media de edad de sex = 'F'
    mean_F = int(df[df.sex == 'F'].age.apply(int).mean())
    print ('Media: M', mean_M, 'F', mean_F)
# Mediana de edad de sex = 'M'
    median_M = int(df[df.sex == 'M'].age.apply(int).median())
# Mediana de edad de sex = 'F'
    median_F = int(df[df.sex == 'F'].age.apply(int).median())
    print ('Mediana: M', median_M, 'F', median_F)
    
    return (mean_M, mean_F, median_M, median_F)


def fill_null_col(df, col_f, col_s, s, r1, r2):
# Devuelve un dataframe con los nulos de la columna col_f pasada por parámetro rellenados con los valores r1 o r2 pasados por 
# parámetro en función de si el valor de la col_s es s

# Parámetros: df: dataframe
#             col_f : columna de valores a rellenar nulos
#             col_s: columna de valores a buscar para elegir con que rellenar nulos de la columna col_f
#             s: valor a buscar en la col_s para elegir con que reemplazar el nulo de col_f
#             r1: valor para rellenar los nulos de col_f donde el valor de col_s sea s
#             r2: valor para rellenar los nulos de col_f donde el valor de col_s no s


    for i in df[col_f].isnull().index:
        if (s in df.loc[i,col_s]) and (df.loc[i,col_f] is np.nan):
            df.loc[i,col_f] = r1
        elif df.loc[i,col_f] is np.nan:
            df.loc[i,col_f] = r2   
    return df

def replace_data_list(df,col,l_s,l_rs):

# Devuelve una serie donde se reemplaza los valores de la lista l_s pasada por parámetro por los valores de la lista l_rs pasada
# por parámetro en el mismo orden
# Parámetros: df: dataframe
#             col: columna
#             l_s: lista de datos a reemplazar
#             l_rs : lista de nuevos valores, en el mismo orden que l_s

    for i in range(len(l_s)):
         df[col]=df[col].replace(l_s[i],l_rs[i]) 
        
    return df[col]