import streamlit as st
import math

# Function to compute y
def compute_y(T, N_pub, N_top5, D_assoc, D_full):
    log_y = 12.14 - 0.0104 * T + 0.0053 * N_pub + 0.0206 * N_top5 + 0.2269 * D_assoc + 0.4877 * D_full
    return math.exp(log_y)  # Convert log y to y

# Streamlit app
st.title("Compute y")

T = st.number_input("Enter T:", value=0.0)
N_pub = st.number_input("Enter N_pub:", value=0.0)
N_top5 = st.number_input("Enter N_top5:", value=0.0)
D_assoc = st.radio("Is D_assoc True?", [0, 1])
D_full = st.radio("Is D_full True?", [0, 1])

if st.button("Compute"):
    result = compute_y(T, N_pub, N_top5, D_assoc, D_full)
    st.success(f"Computed y = {result:.4f}")