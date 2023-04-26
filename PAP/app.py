import pandas as pd
import streamlit as st
import plotly.express as px

# page configstreamlit 

st.set_page_config(
    page_title='Pokemon App',
    page_icon='🐉',
    layout='wide'
)

st.sidebar.title('🐉 🦎 🐆 Pokemon App')
st.image('PAP/pokemon.jpg',use_column_width=True)
#load data 
def load_pokemon():
    data=pd.read_csv('PAP/pokemon.csv',index_col=0)
    return data
with st.spinner('Loading pokemon Data...'):
    pokemon=load_pokemon()
    st.sidebar.success("loading Pokemon Data...")

show_data=st.sidebar.checkbox('show the dataset')
if show_data: 
    st.subheader('pokemon Data') 
    st.dataframe(pokemon,use_container_width=True)
     
type1=st.sidebar.selectbox('select pokemon Type',pokemon['Type 1'].unique())

subset=pokemon[pokemon['Type 1']==type1]#filter

tabs=st.tabs(['Data','univeriable Analysis','Bivariate Analysis','trivariate'])
#Data tab

tabs[0].subheader(f'{type1}Pokemon')
tabs[0].dataframe(subset,use_container_width=True)

#univariate Analysis tab
#Attack
tabs[1].subheader(f'{type1}stats')
tabs[1].subheader('Atack')
ss=subset.sort_values(by='Attack')
fig1=px.histogram(ss,x='Attack',nbins=20)
fig2=px.bar(ss,x='Name',y='Attack',)
tabs[1].plotly_chart(fig1,use_container_width=True)
tabs[1].plotly_chart(fig2,use_container_width=True)

#Defence
ss=subset.sort_values(by='Defense')
fig1=px.histogram(ss,x='Defense',nbins=20)
fig2=px.bar(ss,x='Name',y='Defense')
tabs[1].subheader('Defense')
tabs[1].subheader(f'{type1}stats')
tabs[1].plotly_chart(fig1,use_container_width=True)
tabs[1].plotly_chart(fig2,use_container_width=True)

#do the same for HP, sp, Atk, sp. ,Def , speed

#Bivariate Analysis tab
x=tabs[2].selectbox('Select X',pokemon.select_dtypes('number').columns)
y=tabs[2].selectbox('Select Y',pokemon.select_dtypes('number').columns)
c=tabs[2].selectbox( 'Select Color',pokemon.select_dtypes(exclude='number').columns)
fig=px.scatter(subset,x=x,y=y,color=c,hover_data=['Name'],size=x,size_max=60)
tabs[2].subheader(f'{type1} : {x} vs{y} by{c}')
tabs[2].plotly_chart(fig,use_container_width=True)



#trivariate analysis
x=tabs[3].selectbox('select x',pokemon.select_dtypes('number').columns)
y=tabs[3].selectbox('select y',pokemon.select_dtypes('number').columns)
z=tabs[3].selectbox('select z',pokemon.select_dtype('number').columns)
c=tabs[3].selectbox( 'select color',pokemon.select_dtypes(exclude='number').columns)
fig=px.scatter_3d(subset,x=x,y=y,color=c,hover_data=['Name'],size=x,size_max=60)
tabs[3].subheader(f'{type1} : {x} vs{y} by{c}')
tabs[3].plotly_chart(fig,use_container_width=True)

 