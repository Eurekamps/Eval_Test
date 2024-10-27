import openai
import os

# Load the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Read evaluation criteria from README
with open("README.md", "r") as file:
    readme_content = file.read()

# Define your prompt with extracted data (test results, README instructions)
# prompt = f"""
# Check all files in the Github Repository and Grade is according to these criteria:
# {readme_content}
# """

#prompt = f"""
#Check all the GitHub project, file by file and it's complete structure, and Grade is according to these criteria:
#{readme_content}
#"""

prompt = f"""
Evalua todos los ficheros del repositorio, los ficheros HTML, CSS, JS, VUE, KOTLIN, JAVA, DART, describe los aciertos y los fallos mostrando el sitio donde acerto y fallo, otorga puntuacion por cada seccion, y revisa que se hayan cumplido todos los puntos descritos a continuacion:
{readme_content}
"""

# Generate evaluation and grade with ChatGPT
#response = openai.ChatCompletion.create(
#    model="gpt-4",
#    messages=[{"role": "system", "content": prompt}],
#    max_tokens=150
#)

response = openai.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": prompt,
        }
    ],
    #model="gpt-3.5-turbo",
    model="gpt-4o"
)

# Extract and print the evaluation
feedback = response.choices[0].message.content
print(feedback)

# Save feedback to GRADE.md
with open("GRADE.md", "w") as grade_file:
    grade_file.write(feedback)
