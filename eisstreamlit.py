import streamlit as st
import re

st.set_page_config(page_title="Multi-Translator", page_icon="🌐")

# --- TRANSLATION LOGIC: EIS ---
def eng_to_eis(text):
    # Exception: what -> eis
    text = re.sub(r'\bwhat\b', 'eis', text, flags=re.IGNORECASE)
    text = re.sub(r'\bWhat\b', 'Eis', text)
    # Soft G -> dz
    text = re.sub(r'g(?=[eiy])', 'dz', text)
    text = re.sub(r'G(?=[eiyEIY])', 'Dz', text)
    # J -> dz
    text = text.replace('j', 'dz').replace('J', 'Dz')
    # CH -> ts
    text = text.replace('ch', 'ts').replace('Ch', 'Ts').replace('CH', 'TS')
    # sh sounds in middle (combination) -> si
    text = re.sub(r'ti(?=[oa]n|al)', 'si', text)
    text = re.sub(r'Ti(?=[oa]n|al)', 'Si', text)
    # SH -> s
    text = text.replace('sh', 's').replace('Sh', 'S').replace('SH', 'S')
    return text

def eis_to_eng(text):
    text = re.sub(r'\beis\b', 'what', text, flags=re.IGNORECASE)
    text = text.replace('dz', 'j').replace('Dz', 'J')
    text = text.replace('ts', 'ch').replace('Ts', 'Ch')
    return text

# --- TRANSLATION LOGIC: BUWGEH ---
def eng_to_buwgeh(text):
    # 1. R at the end of a word becomes H
    text = re.sub(r'r\b', 'h', text)
    text = re.sub(r'R\b', 'H', text)
    # 2. All other R's become W
    text = text.replace('r', 'w').replace('R', 'W')
    return text

def buwgeh_to_eng(text):
    # Best effort reverse: W -> R
    text = text.replace('w', 'r').replace('W', 'R')
    # Note: Reverse H -> R is skipped to avoid turning "the" into "tre"
    return text

# --- SHARED UI COMPONENT ---
def translator_ui(mode_key, eng_func, target_func, target_name):
    if mode_key not in st.session_state:
        st.session_state[mode_key] = f"English to {target_name}"

    col1, col2, col3 = st.columns([5, 2, 5])

    with col1:
        source_label = "English" if st.session_state[mode_key] == f"English to {target_name}" else target_name
        input_text = st.text_area(f"Input ({mode_key})", label_visibility="collapsed", height=250, placeholder=f"Enter {source_label} text...", key=f"input_{mode_key}")

    with col2:
        st.write("##")
        st.write("##")
        if st.button("Swap ⇄", key=f"btn_{mode_key}"):
            if st.session_state[mode_key] == f"English to {target_name}":
                st.session_state[mode_key] = f"{target_name} to English"
            else:
                st.session_state[mode_key] = f"English to {target_name}"
            st.rerun()

    with col3:
        target_label = target_name if st.session_state[mode_key] == f"English to {target_name}" else "English"
        
        if st.session_state[mode_key] == f"English to {target_name}":
            result = eng_func(input_text)
        else:
            result = target_func(input_text)
            
        st.text_area(target_label, value=result, height=250, key=f"output_{mode_key}")

# --- MAIN APP ---
st.title("Translator Hub")

tab1, tab2 = st.tabs(["eis", "buwgeh"])

with tab1:
    st.subheader("eis translator")
    st.markdown("`sh→s`, `ch→ts`, `j/soft-g→dz`, `what→eis`")
    translator_ui("eis_mode", eng_to_eis, eis_to_eng, "eis")

with tab2:
    st.subheader("buwgeh translator")
    st.markdown("`r→w`, `end-r→h` (Example: *River* → *Wiveh*)")
    translator_ui("buwgeh_mode", eng_to_buwgeh, buwgeh_to_eng, "buwgeh")

st.caption("Instructions: Choose a tab to switch patterns. Use the button in the middle to flip the direction.")