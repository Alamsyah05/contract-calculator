import streamlit as st

st.set_page_config(
    page_title="Futures Position Size Calculator", layout="centered")

st.title("📘 Futures Position Size Calculator")

# ===============================
# 1. DATA KONTRAK FUTURES
# ===============================
contracts = {
    "Nasdaq 100 E-mini (NQ)": {"tick_size": 0.25, "tick_value": 5, "point_value": 20},
    "Nasdaq 100 Micro (MNQ)": {"tick_size": 0.25, "tick_value": 0.5, "point_value": 2},
    "S&P 500 E-mini (ES)": {"tick_size": 0.25, "tick_value": 12.5, "point_value": 50},
    "S&P 500 Micro (MES)": {"tick_size": 0.25, "tick_value": 1.25, "point_value": 5},
    "Dow Jones E-mini (YM)": {"tick_size": 1, "tick_value": 5, "point_value": 5},
    "Dow Jones Micro (MYM)": {"tick_size": 1, "tick_value": 0.5, "point_value": 0.5},
}

# ===============================
# 2. USER INPUTS
# ===============================
selected = st.selectbox("Futures Contract", list(contracts.keys()), index=1)

risk_dollar = st.number_input("Risk per Trade ($)", min_value=1, value=500)
stop_loss_input = st.number_input("Stop Loss (in points)", min_value=1, value=25)

# ambil data kontrak terpilih
tick_size = contracts[selected]["tick_size"]
tick_value = contracts[selected]["tick_value"]

# konversi stop loss → tick
stop_loss_ticks = stop_loss_input / tick_size

# ===============================
# 3. PERHITUNGAN
# ===============================
risk_per_contract = stop_loss_ticks * tick_value

if risk_per_contract > 0:
    contract_qty = risk_dollar / risk_per_contract
else:
    contract_qty = 0

# ===============================
# 4. OUTPUT
# ===============================
st.subheader("📊 Calculation Result")

st.write(f"**Tick Size:** {tick_size}")
st.write(f"**Tick Value:** ${tick_value:.2f}")
st.write(f"**Risk per Contract:** ${risk_per_contract:.2f}")

st.success(f"👉 **Max Contract: {contract_qty:.2f}**")




