import os
import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[],
  temperature=0.8,
  max_tokens=256
)