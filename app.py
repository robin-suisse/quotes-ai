import streamlit as st
from catalog_utils import load_catalog

st.title("Quotes AI")
st.write("Transform tradespeoples site notes into a priced quote")
catalog = load_catalog()
st.write(catalog)