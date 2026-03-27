from backend.llm_config import get_llm

class ChatEngine:
    def __init__(self, llm_config):
        self.llm_config = llm_config
        # self.llm = get_llm() # This will be used in the future

    def process_input(self, user_input, pdf_text):
        # Logic to process user input and interact with LangChain API
        if user_input.lower() == "summarize":
            response = self.summarize_text(pdf_text)
        else:
            response = self.generate_response(user_input, pdf_text)
        return response

    def generate_response(self, user_input, pdf_text):
        # Placeholder for response generation logic
        # This should interact with the LangChain API using the provided llm_config
        return f"I have received your message: '{user_input}' and the PDF content. I am not yet equipped to answer questions."

    def summarize_text(self, text: str, max_length: int = 150) -> str:
        """
        Generates a summary of the given text.
        """
        if not text:
            return "The document is empty, so no summary can be provided."

        words = text.split()
        summary = " ".join(words[:max_length])

        if len(words) > max_length:
            summary += "..."

        return f"Here is a summary of the document:\n\n{summary}"
