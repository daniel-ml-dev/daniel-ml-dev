import streamlit as st

st.set_page_config(page_title="Previsor de Imóveis", layout="wide")
st.title("🏖️ Previsor de Imóveis - Litoral Norte SC")

st.sidebar.header("Dados do Imóvel")

cidades_preco = {
    "Joinville": 6500, "Barra Velha": 6800, "Penha": 7000,
    "Piçarras": 8000, "Navegantes": 8500, "Itajaí": 9500,
    "Balneário Camboriú": 12000, "Itapema": 11000, "Florianópolis": 10500
}

cidade = st.sidebar.selectbox("Cidade", list(cidades_preco.keys()))
area = st.sidebar.slider("Área m2", 30, 600, 80)
quartos = st.sidebar.selectbox("Quartos", [1,2,3,4,5,6])
vista_mar = st.sidebar.radio("Vista Mar", ["Não", "Sim"])
dist_praia = st.sidebar.slider("Distância da praia (metros)", 0, 3000, 200)

preco_m2 = cidades_preco[cidade]
preco_base = (preco_m2 * area) + (quartos * 40000)

# Lógica de preço
preco_final = preco_base
if dist_praia > 1000:
    preco_final = preco_final * 0.90 # desconto 10%
if vista_mar == "Sim":
    preco_final = preco_final * 1.35 # +35%
if dist_praia < 200:
    preco_final = preco_final * 1.20 # +20% por ser pé na areia

st.metric("Preço m² em " + cidade, f"R$ {preco_m2:,.2f}")
st.divider()
st.success(f"### Valor Estimado: R$ {preco_final:,.2f}")
st.caption(f"Cálculo: (R$ {preco_m2} * {area}m²) + ({quartos} quartos * R$40k) + ajustes de localização")

if st.button("Calcular novamente 🎈"):
    st.balloons()
