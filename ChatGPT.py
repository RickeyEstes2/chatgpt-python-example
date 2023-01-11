import openai

openai.api_key = ('OPEN_API_KEY')

def generate_response(prompt):
    model_engine = "text-davinci-003"

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

prompt = input("Enter your question: ")
response = generate_response(prompt)
print(response)

with open('chatlog.txt', 'a') as f:
  f.write(prompt + '\n')
  f.write(response + '\n')
  
with open('webscraper.txt', 'w') as f:
  f.write('I asked ChatGPT:\n' + prompt + '\n')
  f.write('\n')
  f.write('ChatGPT replied:\n' + response + '\n')

with open('webscraper2.txt', 'w') as f:
   f.write(response)
  



