import os

from dotenv import load_dotenv
from openai import OpenAI


def main():
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    
    if not api_key:
         raise RuntimeError(f"api_key is not founded")
    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    
    message_user = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    print(f"User prompt: {message_user}")


    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": message_user,
            }

        ],
    )

    if not response.usage:
        raise RuntimeError("Usage is not actively")

    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")
    print("Response:")
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
