from dotenv import load_dotenv
load_dotenv()

import os
import google.generativeai as genai

def list_models():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY not set in environment.")
        return
    genai.configure(api_key=api_key)
    print("Available Gemini models:")
    for model in genai.list_models():
        print(f"- {model.name}")
        print(vars(model))
        print()

if __name__ == "__main__":
    list_models() 