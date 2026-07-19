from openai import OpenAI

from config import OPENAI_API_KEY


client = OpenAI(
    api_key=OPENAI_API_KEY
)


CYRUS_PERSONALITY = """
You are Cyrus, a helpful personal AI assistant.

Personality:
- Friendly
- Clear
- Helpful
- Explains things simply
- Be concise unless the user asks for detail
"""


async def get_ai_response(message: str):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": CYRUS_PERSONALITY
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response.choices[0].message.content