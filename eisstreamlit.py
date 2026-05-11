import streamlit as st
import re

st.set_page_config(page_title="eis translator", page_icon="🌐")

# --- Translation Logic ---
def eng_to_eis(text):
    # 1. Exception: "what" -> "eis" (Case insensitive with word boundaries)
    # This ensures "what" becomes "eis" but "whatever" stays "whatever"
    text = re.sub(r'\bwhat\b', 'eis', text, flags=re.IGNORECASE)
    text = re.sub(r'\bWhat\b', 'Eis', text)

    # 2. Handle soft G (G followed by e, i, or y)
    text = re.sub(r'g(?=[eiy])', 'dz', text)
    text = re.sub(r'G(?=[eiyEIY])', 'Dz', text)
    
    # 3. Handle J
    text = text.replace('j', 'dz').replace('J', 'Dz')
    
    # 4. Handle CH -> TS
    text = text.replace('ch', 'ts').replace('Ch', 'Ts').replace('CH', 'TS')
    
    # 5. Handle "sh" sounds in middle of words (combination, spatial)
    text = re.sub(r'ti(?=[oa]n|al)', 'si', text)
    text = re.sub(r'Ti(?=[oa]n|al)', 'Si', text)
    
    # 6. Handle standard SH -> S
    text = text.replace('sh', 's').replace('Sh', 'S').replace('SH', 'S')
    
    return text

def eis_to_eng(text):
    # Reverse logic
    # First, reverse the special exception
    text = re.sub(r'\beis\b', 'what', text, flags=re.IGNORECASE)
    
    # Then reverse the patterns
    text = text.replace('dz', 'j').replace('Dz', 'J')
    text = text.replace('ts', 'ch').replace('Ts', 'Ch')
    return text

# --- UI Setup ---
st.title("eis translator")

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
        
    st.text_area(target_label, value=result, height=250)

st.caption("Special Rules: 'what' becomes 'eis' | Soft-G/J becomes 'dz' | CH becomes 'ts' | SH becomes 's'")