import openai
import os

# Load the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Read evaluation criteria from README
with open("README.md", "r") as file:
    readme_content = file.read()

# Define your prompt with extracted data (test results, README instructions)
prompt = f"""
Evaluate the following project based on these criteria:
{readme_content}
"""

# Generate evaluation and grade with ChatGPT
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

# Extract and print the evaluation
feedback = response['choices'][0]['message']['content']
print(feedback)

# Save feedback to GRADE.md
with open("GRADE.md", "w") as grade_file:
    grade_file.write(feedback)
