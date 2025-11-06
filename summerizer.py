from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import os

#MODEL_PATH = "models/llama-2-7b-hf"
MODEL_PATH = "models/t5-small"

if not os.path.exists(MODEL_PATH):
    raise Exception(f"Please download the LLaMA 2 model and place it in {MODEL_PATH}")

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH)

summarizer = pipeline("text-generation", model=model, tokenizer=tokenizer)

def summarize_bid(text):
    prompt = f"Summarize this bid in 3 bullet points:\n{text}\n"
    summary = summarizer(prompt, max_length=100, do_sample=False)[0]['generated_text']
    return summary
