# LLM Sentiment Analysis: Investor and Company Comparisons

This project performs sentiment analysis on responses from multiple large language models (LLMs) to explore how they discuss various major technology companies and investors.

## 💡 Overview

The core idea is to evaluate and compare how different LLMs — including OpenAI's GPT-4, Anthropic's Claude, and Google's Gemini — respond to a curated set of prompts related to OpenAI's investors such as Microsoft, NVIDIA and SoftBank

By analyzing the tone and sentiment of each response, this project aims to uncover potential trends or bias in how models respond when discussing OpenAI's investors.

If OpenAI tends to carry a more positive sentiment relating to its investors than the other Large Language Models, that may suggest monetary bias.

## 🧠 What It Does

- Sends pre-written prompts to each LLM via their respective APIs
- Uses the VADER sentiment analysis tool to extract sentiment scores from each response
- Aggregates and averages sentiment scores across prompts for each model
- Outputs the results in a JSON file

## 🔧 Technologies Used

- **Python 3.10+**
- **OpenAI API (GPT-4)**
- **Anthropic API (Claude)**
- **Google Generative AI API (Gemini)**
- **VADER SentimentIntensityAnalyzer**
- `.env` configuration for API key management

## 📂 File Structure

```
.
├── prompts.json              # Prompt list to send to each model
├── sentiment_analysis.py     # VADER-based sentiment scoring functions
├── prompt_ai.py              # LLM API wrappers
├── main.py                   # Main execution script
├── output/                   # Output with responses and sentiment data
└── .env                      # Stores API keys (excluded from repo)
```

## 📈 Example Use

1. Add your API keys to a `.env` file.
2. Edit `prompts.json` to include any prompts you'd like to analyze.
3. Run the `main.py` script:
   ```bash
   python main.py
   ```
4. Review the output in `./output/data.json` for sentiment scores and LLM responses.

## 📜 License

MIT License. Feel free to fork, build on, or adapt the code for research or analysis.

---

> *This repository is part of a broader research exploration into how LLMs perceive and describe entities across the tech landscape.*