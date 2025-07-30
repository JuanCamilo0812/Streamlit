import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

#
st.set_page_config(layout = 'centered',page_title='Talento Tech', page_icon='::smaile')
#Titulo de la pagina
t1, t2 =st.columns([0.3,0.7])
t1.image('TalentoTech.jpg', width= 200)
t2.title('Mi primera Tablero')
t2.markdown('**tel:** 123| **email:** juan.cardona50@udea.edu.co') 

#Secciones
Steps= st.tabs(['Pestaña', 'Pestaña 2','Pestaña $\sqrt{9}$'],)



with Steps[0]:

    camp_df=pd.read_csv('Campanhas.csv', encoding='latin-1',sep=';')
    camp = st.selectbox('Escoge un id de campaña',
                        camp_df['ID_Campana'],
                         help = 'Muestra las campañas existentes')
    met_df = pd.read_csv('Metricas.csv', encoding='latin-1',sep=';')

    m1,m2,m3 = st.columns ([1,1,1])

    id1 = met_df[(met_df['ID_Campana'] == camp)|(met_df['ID_Campana'] == 1)]
    id2 = met_df[met_df['ID_Campana'] == camp]
    m1.write('Metricas.csv')
    m2.metric(label = 'Metrica 1',value = sum(id1['Conversiones']),
    delta=str(sum(id1['Rebotes']))+ 'Numero de Rebotes', 
    delta_color='inverse')

    m2.metric(label = 'Metrica 2',value = np.mean(id1['Conversiones']),
    delta=str(np.mean(id1['Rebotes']))+ 'Promedios', 
    delta_color='inverse')

with Steps[1]:
    df=pd.read_csv("https://raw.githubusercontent.com/diplomado-bigdata-machinelearning-udea/Curso1/master/s03/dataVentas2009.csv")
    df.Fecha = pd.to_datetime(df.Fecha, format ='%d/%m/%Y')
    df.set_index('Fecha',inplace= True)
    
    varx=st.selectbox('Escoge la variable',df.columns)
    fig, ax = plt.subplots()
    ax =sns.histplot(data=df, x=varx)
    st.pyplot(fig)








