from openai import OpenAI
import sys
import os
# Get arguments passed to the script
print(f"Arguments received: {sys.argv[1:]}")
def speak(text):
    os.system(f'espeak "{text}"')
base_url = "https://api.aimlapi.com/v1"
api_key = "8df72ab4814643ca897ee213f4d2b054"
#system_prompt = "You are a travel agent. Be descriptive and helpful."
#user_prompt = "Tell me about San Francisco"
api = OpenAI(api_key=api_key, base_url=base_url)
def main():
    user_prompt=" ".join(sys.argv[1:])
  #  user_prompt=input(">>Ready for your prompt\n")
    completion = api.chat.completions.create(
        model="deepseek-ai/deepseek-llm-67b-chat",
        messages=[
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
        max_tokens=256,
    )

    response = completion.choices[0].message.content

    print("User:", user_prompt)
    print("AI:", response)
    speak(response)


if __name__ == "__main__":
    main()
