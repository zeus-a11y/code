"""Configuration placeholders.

This file no longer stores secret API keys in plaintext. Instead it reads
values from environment variables. Set your keys in a `.env` file or in
your environment and do NOT commit the `.env` file.
"""
import os

# Read secrets from environment. These default to an empty string so the
# application can start; the backend code will raise a clear error if a key
# is required at runtime.
GROK_API_KEY = os.getenv("GROK_API_KEY", "")
OTHER_ENV_VARIABLE = os.getenv("OTHER_ENV_VARIABLE", "")