import streamlit as st
import re

st.set_page_config(page_title="eis translator", page_icon="🌐")

# --- Improved Translation Logic ---
def eng_to_eis(text):
    # 1. Handle soft G (G followed by e, i, or y)
    # This looks for G/g followed by e, i, or y and replaces just the G part
    text = re.sub(r'g(?=[eiy])', 'dz', text)
    text = re.sub(r'G(?=[eiyEIY])', 'Dz', text)
    
    # 2. Handle J
    text = text.replace('j', 'dz').replace('J', 'Dz')
    
    # 3. Handle CH -> TS
    text = text.replace('ch', 'ts').replace('Ch', 'Ts').replace('CH', 'TS')
    
    # 4. Handle "sh" sounds in middle of words (combination, spatial)
    text = re.sub(r'ti(?=[oa]n|al)', 'si', text)
    text = re.sub(r'Ti(?=[oa]n|al)', 'Si', text)
    
    # 5. Handle standard SH -> S
    text = text.replace('sh', 's').replace('Sh', 'S').replace('SH', 'S')
    
    return text

def eis_to_eng(text):
    # Reverse logic (best effort)
    text = text.replace('dz', 'j').replace('Dz', 'J')
    text = text.replace('ts', 'ch').replace('Ts', 'Ch')
    return text

# --- UI Setup ---
st.title("eis translator")
st.markdown("Translates English patterns: `sh→s`, `ch→ts`, `j/soft-g→dz`")

if "mode" not in st.session_state:
    st.session_state.mode = "English to Eis"

# Layout
col1, col2, col3 = st.columns([5, 2, 5])

with col1:
    source_label = "English" if st.session_state.mode == "English to Eis" else "Eis"
    input_text = st.text_area(source_label, height=250, placeholder="Type here...")

with col2:
    st.write("##") # spacing
    st.write("##")
    if st.button("Swap ⇄"):
        st.session_state.mode = "Eis to English" if st.session_state.mode == "English to Eis" else "English to Eis"
        st.rerun()

with col3:
    target_label = "Eis" if st.session_state.mode == "English to Eis" else "English"
    
    if st.session_state.mode == "English to Eis":
        result = eng_to_eis(input_text)
    else:
        result = eis_to_eng(input_text)
        
    st.text_area(target_label, value=result, height=250, disabled=False)
    
    if result:
        st.button("Copy Translation", on_click=lambda: st.write(f"Result copied (manually highlight to copy for now)"))

st.info("Note: 'G' only converts to 'dz' when followed by 'e', 'i', or 'y' (e.g., 'Giant' becomes 'Dzaint').")