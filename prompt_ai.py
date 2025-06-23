import ollama
import openai
import anthropic
import google.generativeai as genai

# Get a response from the llama API
def llama_get_response(model, prompt):
    response = ""
    stream = ollama.chat(model = model,
                        messages=[{'role': 'user', 'content': prompt}],
                        stream=True)
    for chunk in stream:
        response += chunk['message']['content']
    
    return response

# Get a response from the GPT API
def gpt_get_response(model, prompt, api_key):
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(model=model,
                                        messages=[
                                            {"role": "user", "content": prompt}
                                        ])
    return response.choices[0].message.content

# Get a response from the Claude API
def claude_get_response(model, prompt, api_key):
    client = anthropic.Anthropic(api_key=api_key)

    response = client.messages.create(
        model=model,
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text;

# Get a response from the Gemini API
def gemini_get_response(model, prompt, api_key):
    genai.configure(api_key=api_key)
    gemini_model = genai.GenerativeModel(model)
    chat = gemini_model.start_chat()
    response = chat.send_message(prompt)
    return response.text