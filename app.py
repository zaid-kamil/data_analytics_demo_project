import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

@st.cache
def load_data():
    return pd.read_csv('data/ASIANPAINT.csv',parse_dates=['Date'],dayfirst=True, index_col='Date')

st.set_page_config(layout="wide")
df = load_data()

st.title("this is an example")

st.sidebar.subheader("change over time (Univariate analysis)")
cols = ['Prev Close','Open','High','Low','Last','Close','VWAP','Volume','Turnover','Trades','Deliverable Volume','%Deliverble']
col = st.sidebar.selectbox("select a column",cols)

# fig,ax = plt.subplots(figsize=(10,7))
# df[col].plot(title="Opening stocks",ax=ax)
# st.pyplot(fig)

fig = px.line(df, x=df.index, y=col,)
st.plotly_chart(fig,use_container_width=True)