import openai
import os

# Use environment variable for security
openai.api_key = os.getenv("OPENAI_API_KEY")

# Sample log file generated from CI/CD
log_file = "pipeline.log"

if not os.path.exists(log_file):
    print("Log file not found!")
    exit()

with open(log_file, "r") as f:
    logs = f.read()

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a DevOps assistant."},
        {"role": "user", "content": f"Analyze these CI/CD logs and suggest fixes:\n{logs}"}
    ]
)

print("===== AI Log Summary & Suggestions =====")
print(response.choices[0].message.content)

