import streamlit as st
import re

st.set_page_config(page_title="eis translator", page_icon="🌐")

# --- Translation Logic ---
def eng_to_eis(text):
    text = re.sub(r'g([eiyEIY])', r'dz\1', text)
    text = re.sub(r'G([eiyEIY])', r'Dz\1', text)
    text = text.replace('j', 'dz').replace('J', 'Dz')
    text = text.replace('ch', 'ts').replace('Ch', 'Ts')
    text = re.sub(r'ti([oa]n|al)', r'si\1', text)
    text = text.replace('sh', 's').replace('Sh', 'S')
    return text

def eis_to_eng(text):
    text = text.replace('dz', 'j').replace('Dz', 'J')
    text = text.replace('ts', 'ch').replace('Ts', 'Ch')
    return text

# --- UI Setup ---
st.title("eis translator")

# Use session state to handle the "Switch"
if "mode" not in st.session_state:
    st.session_state.mode = "English to Eis"

# Layout
col1, col2, col3 = st.columns([5, 2, 5])

with col1:
    source_label = "English" if st.session_state.mode == "English to Eis" else "Eis"
    input_text = st.text_area(source_label, height=200)

with col2:
    st.write("##") # spacing
    if st.button("Swap ⇄"):
        st.session_state.mode = "Eis to English" if st.session_state.mode == "English to Eis" else "English to Eis"
        st.rerun()

with col3:
    target_label = "Eis" if st.session_state.mode == "English to Eis" else "English"
    
    # Perform translation
    if st.session_state.mode == "English to Eis":
        result = eng_to_eis(input_text)
    else:
        result = eis_to_eng(input_text)
        
    st.text_area(target_label, value=result, height=200, disabled=True)