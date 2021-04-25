import pandas as pd 
import numpy as np


url = 'Casos_positivos_de_COVID-19_en_Colombia.csv'

df = pd.read_csv(url)

df.shape

df.columns

df.size

df.count()


df['Código ISO del país'].value_counts

df.drop('Código ISO del país',axis=1,inplace=True)

df.drop(['Pertenencia étnica',
       'Nombre del grupo étnico','Nombre del país','Tipo de recuperación'],axis=1,inplace=True)

df.loc[df['Ubicación del caso'] == 'CASA','Ubicación del caso'] = 'Casa'

df.loc[df['Ubicación del caso'] == 'casa','Ubicación del caso'] = 'Casa'


# Número de casos de Contagiados en el País.
numCasosColombia = len(df['ID de caso'])

# Número de Municipios Afectados
numMunicipiosAfectados = len(df.groupby('Nombre municipio'))

## Listado de municipios afectados sin repetir

listMunicipios = df.groupby('Nombre municipio').size().sort_values(ascending=True)

## Número de personas que se encuentran en atención en casa

cantidadCasa = len(df.loc[df['Ubicación del caso'] == 'Casa']) + len(df.loc[df['Ubicación del caso'] == 'CASA'])

# Número de personas que se encuentran recuperados

cantidadRecuperados = len(df.loc[df['Recuperado'] == 'Recuperado'])

# Número de personas que ha fallecido

cantidadFallecidos = len(df.loc[df['Ubicación del caso'] == 'fallecido']) + len(df.loc[df['Ubicación del caso'] == 'Fallecido'])

# Número de departamentos afectados
numDepartamentosAfectados = len(df.groupby('Nombre departamento'))

## Liste los departamentos afectados(sin repetirlos)

listDepartamentos = df.groupby('Nombre departamento').size().sort_values(ascending=False)

# Liste de mayor a menor los 10 departamentos con mas casos de contagiados

topDepartamentos = listDepartamentos[:10]

# Liste de mayor a menor los 10 departamentos con mas casos de fallecidos

topFallecidosDepartamentos = df[df['Ubicación del caso'] == 'Fallecido'].groupby('Nombre departamento').size().sort_values(ascending=False)[:10]

# Liste de mayor a menor los 10 departamentos con mas casos de recuperados

topRecuperadosDepartamentos = df[df['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size().sort_values(ascending=False)[:10]

#Liste de mayor a menor los 10 municipios con mas casos de contagiados

topContagiadosDepartamentos = df[df['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size().sort_values(ascending=False)[:10]


#Liste de mayor a menor los 10 municipios con mas casos defallecidos

topFallecidosMunicipio = df[df['Ubicación del caso'] == 'Fallecido'].groupby('Nombre municipio').size().sort_values(ascending=False)[:10]


# Liste de mayor a menor los 10 municipio con mas casos de recuperados

topRecuperadoMunicipio = df[df['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size().sort_values(ascending=False)[:10]

# Liste agrupado por departamento y en orden de Mayor a menor las ciudades con mas casos de contagiados

df.groupby(['Nombre departamento']).size().sort_values(by=['Nombre municipio'],ascending=False)
##bar = df[df['Nombre municipio'] == 'BARRANQUILLA']

##bar.loc[df['Estado'] == 'leve','Estado'] = 'Leve'

##bar.groupby(['Sexo','Estado']).size()
##bar.groupby(['Sexo','Edad']).size()
##bar.groupby('Fecha de diagnóstico').size().sort_values(ascending=True)