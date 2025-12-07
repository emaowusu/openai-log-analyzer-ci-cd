import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

log_file = "pipeline.log"

if not os.path.exists(log_file):
    print("Log file not found!")
    exit()

with open(log_file, "r") as f:
    logs = f.read()

response = client.chat.completions.create(
    model="gpt-4o-mini",   
    messages=[
        {"role": "system", "content": "You are a DevOps assistant."},
        {"role": "user", "content": f"Analyze these CI/CD logs and suggest fixes:\n{logs}"}
    ]
)

print("===== AI Log Summary & Suggestions =====")
print(response.choices[0].message.content)
