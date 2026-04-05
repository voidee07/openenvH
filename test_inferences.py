from openai import OpenAI

client = OpenAI(api_key="your-api-key-here")

def ask_ai(bug_report):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a bug triage expert."
            },
            {
                "role": "user", 
                "content": f"Triage this bug: {bug_report}"
            }
        ]
    )
    return response.choices[0].message.content

# Test it
result = ask_ai("App crashes when user clicks logout on mobile")
print(result)