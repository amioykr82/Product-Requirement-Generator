from openai import OpenAI

# ✅ Initialize OpenAI with environment variable (OPENAI_API_KEY must be set in Railway)
client = OpenAI()

def generate_answer(context: str, query: str) -> str:
    system_message = """
You are an AI assistant helping product managers convert specifications into structured and professional requirement documents.

Always respond in exactly two paragraphs with the following format:

Definitions: [Include a smaller 2–3 sentence paragraph here. Do not just restate the title. Clearly define what this requirement is about, and introduce it to someone who may not be familiar.]

Scope and Objective: [Write a separate paragraph that explains how this requirement is scoped, what its purpose is, and how it will be used in the product lifecycle.]
"""

    user_prompt = f"""Context from specification document:\n{context}\n\nWrite requirement for: "{query}"\nUse the format described above."""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.5
    )

    return response.choices[0].message.content.strip()
