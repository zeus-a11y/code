import streamlit as st
from frontend.components.chat_interface import ChatInterface
from frontend.views.main_page import main_page
from backend.chat_engine import ChatEngine
from backend.llm_config import get_llm_config

def _local_css():
    # small set of styles for the landing page and chat bubbles
    st.markdown(
        """
        <style>
        /* Option 3: Mobile-first dark conversational UI */
        :root { --bg: #0f1720; --card: #0b1220; --muted: #9aa4b2; --accent: #5fb0ff; --accent2: #6b46ff }
        html, body { background: var(--bg); }
        .logo-svg { display:block; margin-left:auto; margin-right:auto; width:36%; max-width:280px; }
        .center { text-align:center; color:#ffffff }
        .big-cta { background: linear-gradient(90deg,var(--accent),var(--accent2)); color: white; padding: 14px 28px; border-radius: 14px; font-size:18px; font-weight:700; text-decoration:none; display:inline-block }
        .panel { background: var(--card); padding:12px; border-radius:14px; color:#e6eef8 }
        .chat-user { background: linear-gradient(90deg,var(--accent),#2b80ff); color: white; padding:12px 16px; border-radius:20px; margin:8px 0; display:inline-block; max-width:85%; float:right }
        .chat-bot { background:#111827; border:1px solid #1f2937; padding:12px 16px; border-radius:20px; margin:8px 0; display:inline-block; max-width:85%; float:left }
        .chat-body { max-height:64vh; overflow:auto; padding:8px; }
        .fab { position: fixed; right: 22px; bottom: 92px; background: linear-gradient(90deg,var(--accent),var(--accent2)); color:white; padding:14px 18px; border-radius:28px; box-shadow: 0 8px 24px rgba(0,0,0,0.4); border:none; }
        .input-area { position: fixed; left: 0; right: 0; bottom: 0; padding:12px; background: linear-gradient(180deg, rgba(0,0,0,0), rgba(0,0,0,0.25)); }
        .send-btn { background: linear-gradient(90deg,var(--accent),var(--accent2)); color:white; padding:10px 18px; border-radius:12px; border:none }
        .muted { color: var(--muted) }
        </style>
        """,
        unsafe_allow_html=True,
    )

def main():
    # Page config must be called first
    st.set_page_config(page_title="PDF Chatbot", layout="wide")

    # Inject CSS
    _local_css()

    # App page
    st.title("PDF Chatbot")

    try:
        llm_config = get_llm_config()
        chat_engine = ChatEngine(llm_config=llm_config)
        chat_interface = ChatInterface(chat_engine=chat_engine)
        main_page(chat_interface)
    except ValueError as e:
        st.error(e)

if __name__ == "__main__":
    main()
