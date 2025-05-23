


import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

models = genai.list_models()
for m in models:
    print(m.name, m.supported_generation_methods)




# models/chat-bison-001 ['generateMessage', 'countMessageTokens']
# models/text-bison-001 ['generateText', 'countTextTokens', 'createTunedTextModel']
# models/embedding-gecko-001 ['embedText', 'countTextTokens']
# models/gemini-1.0-pro-vision-latest ['generateContent', 'countTokens']
# models/gemini-pro-vision ['generateContent', 'countTokens']
# models/gemini-1.5-pro-latest ['generateContent', 'countTokens']
# models/gemini-1.5-pro-001 ['generateContent', 'countTokens', 'createCachedContent']
# models/gemini-1.5-pro-002 ['generateContent', 'countTokens', 'createCachedContent']
# models/gemini-1.5-pro ['generateContent', 'countTokens']
# models/gemini-1.5-flash-latest ['generateContent', 'countTokens']
# models/gemini-1.5-flash-001 ['generateContent', 'countTokens', 'createCachedContent']
# models/gemini-1.5-flash-001-tuning ['generateContent', 'countTokens', 'createTunedModel']
# models/gemini-1.5-flash ['generateContent', 'countTokens']
# models/gemini-1.5-flash-002 ['generateContent', 'countTokens', 'createCachedContent']
# models/gemini-1.5-flash-8b ['createCachedContent', 'generateContent', 'countTokens']
# models/gemini-1.5-flash-8b-001 ['createCachedContent', 'generateContent', 'countTokens']
# models/gemini-1.5-flash-8b-latest ['createCachedContent', 'generateContent', 'countTokens']
# models/gemini-1.5-flash-8b-exp-0827 ['generateContent', 'countTokens']
# models/gemini-1.5-flash-8b-exp-0924 ['generateContent', 'countTokens']
# models/gemini-2.5-pro-exp-03-25 ['generateContent', 'countTokens']
# models/gemini-2.5-pro-preview-03-25 ['generateContent', 'countTokens']
# models/gemini-2.0-flash-exp ['generateContent', 'countTokens', 'bidiGenerateContent']
# models/gemini-2.0-flash ['generateContent', 'countTokens']
# models/gemini-2.0-flash-001 ['generateContent', 'countTokens']
# models/gemini-2.0-flash-exp-image-generation ['generateContent', 'countTokens', 'bidiGenerateContent']
# models/gemini-2.0-flash-lite-001 ['generateContent', 'countTokens']
# models/gemini-2.0-flash-lite ['generateContent', 'countTokens']
# models/gemini-2.0-flash-lite-preview-02-05 ['generateContent', 'countTokens']
# models/gemini-2.0-flash-lite-preview ['generateContent', 'countTokens']
# models/gemini-2.0-pro-exp ['generateContent', 'countTokens']
# models/gemini-2.0-pro-exp-02-05 ['generateContent', 'countTokens']
# models/gemini-exp-1206 ['generateContent', 'countTokens']
# models/gemini-2.0-flash-thinking-exp-01-21 ['generateContent', 'countTokens']
# models/gemini-2.0-flash-thinking-exp ['generateContent', 'countTokens']
# models/gemini-2.0-flash-thinking-exp-1219 ['generateContent', 'countTokens']
# models/learnlm-1.5-pro-experimental ['generateContent', 'countTokens']
# models/gemma-3-1b-it ['generateContent', 'countTokens']
# models/gemma-3-4b-it ['generateContent', 'countTokens']
# models/gemma-3-12b-it ['generateContent', 'countTokens']
# models/gemma-3-27b-it ['generateContent', 'countTokens']
# models/embedding-001 ['embedContent']
# models/text-embedding-004 ['embedContent']
# models/gemini-embedding-exp-03-07 ['embedContent']
# models/gemini-embedding-exp ['embedContent']
# models/aqa ['generateAnswer']
# models/imagen-3.0-generate-002 ['predict']
# models/gemini-2.0-flash-live-001 ['bidiGenerateContent', 'countTokens']

