# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import plotly.express as px
import pandas as pd




with st.sidebar:
    st.write("Esta es una barra lateral")
    option = st.selectbox(
        'How would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone'))
    st.write('You selected:', option)



def print_hi(name):
    st.header ("Hola")
    st.subheader("Buenas")
    st.write("Noches")
    st.write("FCA")

    df = px.data.gapminder()
    st.dataframe(df)
    listaPaises = df["country"].unique().tolist()
    #st.write(listaPaises)
    pais = "Canada"
    with st.sidebar:
        pais=st.selectbox("Paises",listaPaises)
        st.write(pais)
    datosPais = df.query("country == '"+ pais +"'")

    fig = px.bar(datosPais, x='year', y='pop')
    st.plotly_chart(fig, use_container_width=True)


    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(1):
        print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
