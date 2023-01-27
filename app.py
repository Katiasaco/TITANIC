#-----------------------------LIBRERIAS-----------------------------
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import plotly_express as px
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
import matplotlib.pyplot as plt
import requests
import os 
import streamlit.components.v1 as components
from unicodedata import name
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
from PIL import Image


#-----------------leer datos--------------------------
df = pd.read_csv (r'C:\Users\katia\.vscode\examplecode\MODULO_1\Modulo1\13-Trabajo_Modulo1\datos\titanic.csv')
df['Survived'] = pd.to_numeric(df['Survived'], errors='coerce').fillna(0)

st.set_page_config(page_title="ANALISIS COMPLETO DEL TITANIC" , page_icon="🛳️")


#------------------------SIDEBAR------------------------
with st.sidebar:

    st.image(('https://www.fcmtravel.com/sites/default/files/styles/large/public/analytics-large.png?itok=B0pCkaKw'),width=100,)
    st.write ('Selecciona el ambito que quieras analizar:')
    

#INTRODUCCION --------------

st.title(("EL TITANIC, ¿QUE PASÓ REALMENTE?"))

def load_lottieurl(url: str):
        r = requests.get (url)
        if r.status_code !=200:
            return None
        return r.json() 

lottie_url_barco = 'https://assets3.lottiefiles.com/packages/lf20_4iojwfsa.json'
lottie_barco = load_lottieurl(lottie_url_barco)
st_lottie(lottie_barco, key='barco')


user_name = st.text_input('Registrate con tu correo!')
button_press = st.button("Enviar")
if button_press: 
    print(st.header('Gracias por registrarte '+ user_name))


#----------------------DIVISION DE COLUMNAS ------------------------------------------
col1, col2 = st.columns(2)
with col1:
    st.title('¿Que pasó con el Titanic?')
    st.write ('El barco "insumergible" fue construido en dos años, navegó durante cuatro días y medio, y, tras chocar con un iceberg, se hundió en dos horas y 40 minutos llevándose consigo muchas vidas por delante.')
    st.video('https://www.youtube.com/watch?v=yRvojNAvlWY')
    st.write('Este video es de Qore')
with col2:
    st.title('Vamos a comprobarlo! ')
    def load_lottieurl(url: str):
        r = requests.get (url)
        if r.status_code !=200:
            return None
        return r.json() 

    lottie_url_lupa = 'https://assets1.lottiefiles.com/packages/lf20_wil3kuum.json'
    lottie_lupa = load_lottieurl(lottie_url_lupa)

    st_lottie(lottie_lupa, key='Lupa')




#-------------------------DATOS GLOBALES -----------------------
st.header("ANALISIS GLOBAL")
x=df.hist(figsize=(7,7) , color= "lightblue", edgecolor='maroon' , linewidth= 0.5) , plt.tight_layout()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()


#---------------------BOTONES DEL SIDEBAR-----------------------------

if st.sidebar.button('Análisis Geográfico'):
    st.title('TENEMOS UN TOTAL DE 980 PASAJEROS')

    col1, col2 = st.columns(2)
    with col1:
        
        st.write('Observamos que la mayorÍa de los supervivientes son de SOUTHMPTON')
        df_X=df.groupby(["Survived", "Embarked",]).count()["PassengerId"]  
        df_X.unstack(level=0).plot.bar()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
    with col2:
        st.write('AquÍ observamos la clase de billete que sale de cada puerto, viendo gráficamente la economía de cada lugar.')
        df_X=df.groupby(["Pclass", "Embarked"]).count()["PassengerId"]  
        df_X.unstack(level=0).plot.bar()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()


    col1, col2 = st.columns(2)
    with col1:
        df["Total_family"]= df["SibSp"] + df["Parch"]
        st.write('Observamos que la mayorÍa de los pasajeros salen desde Southmpton, coinciden con la clase 3, ya que a más familiares, menos clase.')
        df_X=df.groupby(["Total_family", "Embarked"]).count()["PassengerId"]  
        print(df_X)
        df_X.unstack(level=0).plot.bar()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
    with col2:
        st.write('Podemos ver la población que embarcó y la tarifa que escogieron.')
        sns.stripplot(x="Embarked", y="Fare", data=df)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    import plotly.graph_objects as go
   
    html = open("mapa.html", "r", encoding='utf-8').read()
    st.components.v1.html(html,height=500)


#----------------------------------

if st.sidebar.button('Análisis Económico'):
    st.title('EL PRECIO MÁS ALTO DEL BILLETE ES: 512.3292 Y EL PRECIO MÁS BAJO ES:  0.0')
    col1, col2 = st.columns(2)
    with col1:
        st.write('Tabla de supervivientes según su sexo y clase.')
        html = open("tablita.html", "r", encoding='utf-8').read()
        st.components.v1.html(html,height=200)
    
    with col2: 
        st.write('Podemos observar que a mejor clase, mas supervivientes.')
        sns.lineplot(x="Pclass",y="Survived", data=df)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()        


    st.write('Podemos observar algunas de las tarifas que tenían en la entrada del barco.')
    col1, col2 = st.columns(2)
   
    with col1:
        df[['Fare']].value_counts().head(10).plot.pie()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    with col2:
        sns.displot(df.Fare)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()


    col1, col2 = st.columns(2)
    with col1:
        st.write('Podemos observar que la mayoría de los tripulantes eran de clase 3, es decir eran de clase media.')
        sns.displot(df.Pclass)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    with col2:
        df["Total_family"]= df["SibSp"] + df["Parch"]
        st.write('Tabla de supervivientes, clase y cantidad de familiares.')
        html = open("tablit.html", "r", encoding='utf-8').read()
        st.components.v1.html(html,height=800)


#---------------------------
if st.sidebar.button('Análisis Social'):


    #----------------------CONFIGURACION DE TABLAS------------------------------------
    tabs = st.tabs(["Rangos", "Sexo", "Supervivientes"])
#----------------------TABLA1------------------------------------
    tab_plots = tabs[0]
    with tab_plots:

        col1, col2 = st.columns(2)
        with col1:
            st.write('Mostramos el rango de edad del barco. La mayor parte de la tripulación rondaban los 30.')
            df.Age.plot.hist()
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()

        with col2:
            st.write('Mostramos el rango de edad segun los supervivientes.Podemos ver que la media de edad en este barco era de 29.70. Por eso, tanto la gran parte de muertos como supervivientes rondan en esta edad. ')
            df_X=df.groupby(["Survived", "Age"]).count()["PassengerId"]
            print(df_X)
            df_X.unstack(level=0).plot()
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()


    tab_plots = tabs[1]
    with tab_plots:
        col1, col2 = st.columns(2)
        with col1:
            st.write('Distribución sexual del barco')
            df[['Sex']].value_counts().plot.pie()
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
        with col2:
            st.write('La mayoría de las mujeres sobrevivieron y la mayoría de los hombres murieron')
            df_X=df.groupby(["Survived", "Sex"]).count()["PassengerId"]  
            print(df_X)
            df_X.unstack(level=0).plot.bar()
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()



    tab_plots = tabs[2]
    with tab_plots:
        st.write('Vamos a realizar un estudio de las personas que sobrevivieron en el titanic. Fueron un total de 342 personas y embarcaron 891.Es decir, murieron en el Titanic un total de 549 personas.')
        fig = plt.figure(figsize=(20,1))
        sns.countplot(y='Survived', data=df)
        print(df.Survived.value_counts())
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    
        df["Total_family"]= df["SibSp"] + df["Parch"]
        st.write('Aquí podemos ver los supervivientes que existen segun los grupos familiares. Vemos que los que mas murieron fueron,los que estaban solos sin cargas familiares, ya que un gran porcentaje de la tripulación eran trabajadores de este.')
        df_X=df.groupby(["Total_family","Survived"]).count()["PassengerId"]
        print(df_X)
        df_X.unstack(level=0).plot.bar()
        plt.show()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

#----------------------------------
    
if st.sidebar.button('Análisis final'):
    st.title('CONCLUSIÓN')
    foto1=Image.open('conclusion.png')
    st.image(foto1)

    def load_lottieurl(url: str):
        r = requests.get (url)
        if r.status_code !=200:
            return None
        return r.json() 

    lottie_url_gracias = 'https://assets4.lottiefiles.com/packages/lf20_sqpjokxl.json'
    lottie_gracias = load_lottieurl(lottie_url_gracias)
    st_lottie(lottie_gracias, key='Gracias')

with st.sidebar:
    audio1=open('song.mp3.mp3', "rb")
    st.audio(audio1)
