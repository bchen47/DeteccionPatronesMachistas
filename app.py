import streamlit as st
import pandas as pd
import requests

st.title("Predicción de patrones machistas")
st.markdown("Comparativa de modelos respecto a modelos que existen ya en el mercado vs modelo propio")
st.subheader("Seleccione el comentario")
df = pd.read_csv('test.csv', sep=";",names=["message","target","predict"])
option = st.selectbox(
    'Escoge frase',
    df)

if st.button('Hacer consulta'):
    url = "https://api.meaningcloud.com/sentiment-2.1"
    payload={
        'key': '5cee191a217c4d77587d45cd27f6152e',
        'txt': option,
        'lang': 'es',  # 2-letter code, like en es fr ...
    }

    response = requests.post(url, data=payload)

    print(df["target"][df["message"]==option].values)
    print(df["predict"][df["message"]==option].values)

    st.markdown("El comentario está etiquetado como :"+ ("False" if (df["target"][df["message"]==option].values[0] == 0) else "True"))
    st.markdown("El modelo propio ha predecido como :"+ ("False" if (df["predict"][df["message"]==option].values[0] == 0) else "True"))

    print('Status code:', response.status_code)
    st.subheader("La calificación proporcionada por MeaningCloud es")
    st.code(response.json()['score_tag'])
else:
    st.write('Goodbye')
