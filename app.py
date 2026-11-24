import streamlit as st
from catalog_utils import load_catalog, price_lines
from llm_utils import extract_lines
from quotes_utils import quote_totals

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
        totals = quote_totals(priced_lines, 10)
        st.metric("Total HT", f"{totals['excl_vat']:.2f} €")
        st.metric("TVA", f"{totals['vat']:.2f} €")
        st.metric("Total TTC", f"{totals['incl_vat']:.2f} €")
        if manual_lines:
            st.warning("À chiffrer manuellement :", )
            for line in manual_lines:
                st.warning(f"- {line['description']}")

