"""
Lesson 1: Connecting to GPT-5.2 with Python

This script demonstrates the simplest possible connection to OpenAI's GPT-5.2.
One request. One response. That's it.
"""

from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# Create the client (automatically uses OPENAI_API_KEY from environment)
client = OpenAI()

# Make a simple request
response = client.responses.create(
    model="gpt-5.2",
    input="Explain what an API is in one short paragraph."
)

# Print the response
print(response.output_text)
