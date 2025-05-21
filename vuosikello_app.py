import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Oletusaineisto (voit muokata)
data = pd.DataFrame({
    "Kuukausi": [
        "Tammi", "Helmi", "Maalis", "Huhti", "Touko", "Kesä",
        "Heinä", "Elo", "Syys", "Loka", "Marras", "Joulu"
    ],
    "Tehtävä": [
        "Henkilöstöpalaveri", "Auditointi: Johto", "Työterveyskatsaus", "Asiakastyytyv.kysely",
        "Auditointi: Laatu", "Kaluston tarkistus", "Lomasuunnittelu", "Auditointi: Hankinta",
        "Kehityskeskustelut", "Dokumenttikatselmus", "Auditointi: Myynti", "Henkilöstötilinpäätös"
    ]
})

st.set_page_config(page_title="Vuosikello", layout="wide")
st.title("\ud83c\udf10 Interaktiivinen Vuosikello")

# Luo ympyräkellon näkymä Plotlylla
fig = go.Figure()
angles = list(range(0, 360, 30))

for i, row in data.iterrows():
    fig.add_trace(go.Scatterpolar(
        r=[1, 1.1],
        theta=[angles[i], angles[i]],
        mode='lines+text',
        text=["", row["Tehtävä"]],
        textposition="top center",
        line=dict(color='royalblue', width=3)
    ))

fig.update_layout(
    polar=dict(
        radialaxis=dict(visible=False),
        angularaxis=dict(
            tickvals=angles,
            ticktext=data["Kuukausi"].tolist(),
            rotation=90,
            direction="clockwise"
        )
    ),
    showlegend=False,
    margin=dict(l=50, r=50, t=50, b=50)
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("\ud83d\udcc5 Tehtävät kuukaudittain")
st.dataframe(data, use_container_width=True)

# Mahdollisuus lisätä uusi tehtävä
with st.expander("\u2795 Lisää uusi tehtävä"):
    uusi_kk = st.selectbox("Kuukausi", data["Kuukausi"].unique())
    uusi_t = st.text_input("Tehtävä")
    if st.button("Lisää"):
        if uusi_t:
            data.loc[len(data)] = [uusi_kk, uusi_t]
            st.success(f"Tehtävä lisätty: {uusi_kk} – {uusi_t}")
            st.experimental_rerun()
