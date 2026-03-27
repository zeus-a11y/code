import os
import streamlit as st
import PyPDF2
from frontend.components.chat_interface import ChatInterface

def main_page(chat_interface: ChatInterface):
    """Render the main page UI: uploader, PDF preview and chat area.

    This layout avoids an empty page by showing helpful controls and the
    current chat history. It uses a form for message submission to ensure
    predictable reruns.
    """
    # Minimal mobile-first hero (dark)
    st.markdown(
        """
        <div style='text-align:center; color:white; margin-bottom:12px'>
            <h1 style='margin:4px 0'>PDF Chat — Compact</h1>
            <p style='margin:0; color:#9aa4b2'>A focused mobile-first conversational interface — upload, ask, and explore.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Ensure session state keys exist
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'pdf_text' not in st.session_state:
        st.session_state.pdf_text = ""
    if 'uploaded_filename' not in st.session_state:
        st.session_state.uploaded_filename = ""

    # Single-column mobile-first layout
    st.markdown('<div class="panel">', unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    if uploaded_file:
        uploads_dir = os.path.join(os.getcwd(), "uploads")
        os.makedirs(uploads_dir, exist_ok=True)
        file_path = os.path.join(uploads_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        try:
            reader = PyPDF2.PdfReader(file_path)
            text = "\n".join([p.extract_text() or "" for p in reader.pages])
            st.session_state.pdf_text = text.strip()
            st.session_state.uploaded_filename = uploaded_file.name
            st.success(f"Uploaded and extracted text from {uploaded_file.name}")
        except Exception as e:
            st.error(f"Failed to process PDF: {e}")

    if st.session_state.uploaded_filename:
        st.markdown(f"**Loaded:** {st.session_state.uploaded_filename}")
        st.download_button("Download text", st.session_state.pdf_text or "", file_name=f"{st.session_state.uploaded_filename}.txt")
    else:
        st.markdown("**No document loaded**", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="panel" style="margin-top:12px">', unsafe_allow_html=True)
    # Chat body
    st.markdown('<div class="chat-body">', unsafe_allow_html=True)
    for who, text in st.session_state.chat_history:
        if who == 'user':
            st.markdown(f'<div style="text-align:right;"><span class="chat-user">{text}</span></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div style="text-align:left;"><span class="chat-bot">{text}</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Floating upload FAB removed — it was non-functional on some devices and
    # confused the experience. The file uploader at the top remains available.

    # Input area fixed at bottom
    with st.form(key='chat_form', clear_on_submit=True):
        cols = st.columns([6,1])
        user_input = cols[0].text_input('Message')
        submit = cols[1].form_submit_button('Send')
        if submit and user_input:
            resp = chat_interface.send_message(user_input)
            st.session_state.chat_history.append(('user', user_input))
            st.session_state.chat_history.append(('bot', resp))