from dotenv import load_dotenv
import os
from prompt_ai import llama_get_response, gemini_get_response, claude_get_response, gpt_get_response
from sentiment_analysis import get_sentiment_value
import json
import numpy as np

# Load API Keys
load_dotenv()
claude_key = os.getenv("CLAUDE_API_KEY")
gpt_key = os.getenv("GPT_API_KEY")
gemini_key = os.getenv("GEMINI_API_KEY")

# Define LLM Models to use
gpt_model = 'gpt-4'
gemini_model = 'gemini-2.0-flash'
claude_model = 'claude-opus-4-20250514'

models = {
    gpt_model: lambda prompt: gpt_get_response(gpt_model, prompt, gpt_key),
    gemini_model: lambda prompt: gemini_get_response(gemini_model, prompt, gemini_key),
    claude_model: lambda prompt: claude_get_response(claude_model, prompt, claude_key)
}

# Data Collection Settings
runs_per_prompt = 3

# Load Prompts
with open('prompts.json', 'r') as f:
    prompts = json.load(f)


# Create data structure of output
data = {model: {'scores': [], 'average': 0.0, 'std_dev': 0.0, 'responses': {}} for model in models}

# Collect Data / Sentiment Values
for prompt in prompts:
    for model_name, get_response in models.items():
        for _ in range(runs_per_prompt):
            response = get_response(prompt)
            score = get_sentiment_value(response)

            data[model_name]['scores'].append(score)
            if prompt not in data[model_name]['responses']:
                data[model_name]['responses'][prompt] = []
            
            data[model_name]['responses'][prompt].append({
                'response': response,
                'sentiment': score
            })

# Calculate mean/standard deviation
for model in data:
    scores = data[model]['scores']
    data[model]['average'] = float(np.mean(scores))
    data[model]['std_dev'] = float(np.std(scores))

# Dump Data to File
with open("data.json", 'w') as f:
    json.dump(data, f, indent=4)