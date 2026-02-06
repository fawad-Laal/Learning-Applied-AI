"""
Lesson 1: Connecting to GPT-5.2 with Python

This script demonstrates document summarization with GPT-5.2.
Load a text file. Send it to the model. Get a summary.
"""

from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
client = OpenAI()

# Load document text
document_text = Path("document.txt").read_text(encoding="utf-8")

# Ask GPT-5.2 to summarise it
response = client.responses.create(
    model="gpt-5.2",
    input=f"""
Summarise the following document in 5 bullet points:

{document_text}
"""
)

print(response.output_text)
