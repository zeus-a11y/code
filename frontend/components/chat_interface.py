from backend.chat_engine import ChatEngine
import streamlit as st

class ChatInterface:
    def __init__(self, chat_engine: ChatEngine):
        self.chat_engine = chat_engine

    def send_message(self, message: str) -> str:
        """
        Processes the user's message and returns a response from the ChatEngine.
        """
        if 'pdf_text' in st.session_state and st.session_state.pdf_text:
            return self.chat_engine.process_input(message, st.session_state.pdf_text)
        else:
            return "Please upload a PDF first."

    def get_response(self, message: str) -> str:
        """
        Returns a response for a given message.
        """
        if message == 'summarize':
            if 'pdf_text' in st.session_state and st.session_state.pdf_text:
                return self.chat_engine.process_input("summarize", st.session_state.pdf_text)
            else:
                return "Please upload a PDF to summarize."
        return self.send_message(message)
