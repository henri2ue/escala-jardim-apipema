
import streamlit as st
import pandas as pd

# Carregar dados da escala (gerados previamente)
@st.cache_data
def carregar_escala():
    dados = '''Data,Thamires,Francine,Caique,Jéssica,Jamile,Stephanie,Jailson,Gil,Guilherme,Grazy,Joseane,Cauã
2025-06-16,7:00 - 17:00,7:00 - 16:00,10:00 - 18:20,14:40 - 23:00,14:40 - 23:00,7:00 - 15:20,7:00 - 16:00,7:00 - 15:20,13:00 - 23:00,7:00 - 17:00,10:00 - 18:20,14:40 - 23:00
2025-06-17,7:00 - 16:00,7:00 - 16:00,7:00 - 16:00,11:00 - 19:20,7:00 - 16:00,7:00 - 17:00,7:00 - 17:00,13:00 - 23:00,7:00 - 17:00,7:00 - 15:20,7:00 - 16:00,10:00 - 18:20
2025-06-18,14:40 - 23:00,10:00 - 18:20,7:00 - 16:00,7:00 - 15:20,13:00 - 23:00,7:00 - 17:00,11:00 - 19:20,11:00 - 19:20,7:00 - 17:00,7:00 - 17:00,7:00 - 17:00,10:00 - 18:20
2025-06-19,7:00 - 15:20,7:00 - 15:20,7:00 - 15:20,10:00 - 18:20,7:00 - 17:00,13:00 - 23:00,14:40 - 23:00,11:00 - 19:20,7:00 - 16:00,13:00 - 23:00,14:40 - 23:00,14:40 - 23:00
2025-06-20,7:00 - 15:20,14:40 - 23:00,7:00 - 15:20,11:00 - 19:20,7:00 - 16:00,13:00 - 23:00,14:40 - 23:00,13:00 - 23:00,10:00 - 18:20,7:00 - 17:00,13:00 - 23:00,13:00 - 23:00
2025-06-21,,,,,,,,,,,,
2025-06-22,,,,,,,,,,,,
2025-06-23,7:00 - 17:00,7:00 - 17:00,7:00 - 17:00,14:40 - 23:00,7:00 - 17:00,10:00 - 18:20,7:00 - 15:20,7:00 - 16:00,7:00 - 17:00,7:00 - 17:00,11:00 - 19:20,7:00 - 15:20
2025-06-24,7:00 - 15:20,7:00 - 16:00,14:40 - 23:00,7:00 - 17:00,7:00 - 17:00,10:00 - 18:20,7:00 - 16:00,13:00 - 23:00,14:40 - 23:00,7:00 - 16:00,10:00 - 18:20,14:40 - 23:00
2025-06-25,7:00 - 16:00,7:00 - 16:00,14:40 - 23:00,11:00 - 19:20,7:00 - 15:20,13:00 - 23:00,7:00 - 15:20,11:00 - 19:20,10:00 - 18:20,11:00 - 19:20,7:00 - 16:00,13:00 - 23:00
2025-06-26,11:00 - 19:20,11:00 - 19:20,7:00 - 17:00,7:00 - 15:20,7:00 - 17:00,11:00 - 19:20,7:00 - 17:00,7:00 - 17:00,10:00 - 18:20,10:00 - 18:20,11:00 - 19:20,7:00 - 17:00
2025-06-27,11:00 - 19:20,7:00 - 17:00,13:00 - 23:00,13:00 - 23:00,11:00 - 19:20,7:00 - 17:00,10:00 - 18:20,13:00 - 23:00,7:00 - 16:00,14:40 - 23:00,7:00 - 16:00,7:00 - 15:20
2025-06-28,,,,,,,,,,,,
2025-06-29,,,,,,,,,,,,
2025-06-30,7:00 - 15:20,7:00 - 16:00,10:00 - 18:20,7:00 - 16:00,7:00 - 15:20,14:40 - 23:00,7:00 - 15:20,13:00 - 23:00,7:00 - 16:00,13:00 - 23:00,7:00 - 15:20,7:00 - 17:00
'''
    from io import StringIO
    return pd.read_csv(StringIO(dados), parse_dates=["Data"])

df = carregar_escala()

st.set_page_config(page_title="Escala DBA 1497", layout="wide")
st.title("📋 Escala Operacional - DBA 1497 (Jardim Apipema)")
st.markdown("Visualize os turnos de trabalho entre 16 e 30 de junho de 2025.")

# Filtros
col1, col2 = st.columns(2)
with col1:
    colaborador = st.selectbox("Filtrar por colaborador", ["Todos"] + list(df.columns[1:]))
with col2:
    data = st.date_input("Filtrar por data", value=None, min_value=df["Data"].min(), max_value=df["Data"].max())

df_exibir = df.copy()
if colaborador != "Todos":
    df_exibir = df_exibir[["Data", colaborador]]
if data:
    df_exibir = df_exibir[df_exibir["Data"] == pd.to_datetime(data)]

st.dataframe(df_exibir, use_container_width=True)

# Botão para download
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("📥 Baixar escala completa (.csv)", data=csv, file_name="escala_1497.csv", mime='text/csv')
