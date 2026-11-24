import streamlit as st
from catalog_utils import load_catalog, price_lines
from llm_utils import extract_lines

st.title("Quotes AI")
st.write("Transform tradespeoples site notes into a priced quote")
catalog = load_catalog()
note = st.text_area("Notes de chantier")
if st.button("générer le devis"):
    if note == "":
        st.error("Note vide")
    else:
        lines = extract_lines(note, catalog)
        priced_lines, manual_lines = price_lines(lines, catalog)
        st.table(priced_lines)
        if manual_lines:
            st.warning("À chiffrer manuellement :", )
            for line in manual_lines:
                st.warning(f"- {line['description']}")

