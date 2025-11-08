from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI # We'll use this as Grok isn't directly supported yet

# Load environment variables
load_dotenv()

# Get API key
GROK_API_KEY = os.getenv('GROK_API_KEY')

def get_llm_config():
    """Get LLM configuration settings"""
    if not GROK_API_KEY:
        raise ValueError("Grok API key is not set in the environment variables.")

    return {
        "api_key": GROK_API_KEY,
        "model": "grok-1",  # Update this to the correct Grok model name
        "temperature": 0.7,
        "max_tokens": 150
    }

def get_llm():
    """Initialize and return the LLM instance"""
    config = get_llm_config()

    # TODO: Replace this with actual Grok implementation when available
    # For now, using OpenAI as a placeholder
    llm = ChatOpenAI(
        api_key=config["api_key"],
        model=config["model"],
        temperature=config["temperature"],
        max_tokens=config["max_tokens"]
    )

    return llm