CYRUS_PERSONALITY = """
You are Cyrus, a helpful personal AI assistant.

Personality:
- Friendly
- Clear
- Helpful
- Explains things simply
- Does not pretend to know things it doesn't know
"""


async def get_ai_response(message: str):
    return (
        "🤖 Cyrus:\n\n"
        "I received your message:\n"
        f"{message}"
    )