import subprocess
import json

MODEL = "llama2"  # Ollama model name

def summarize_bid(text):
    """
    Summarize a bid using Ollama locally.
    """
    prompt = f"Summarize this procurement bid in 3 bullet points:\n{text}\n"

    result = subprocess.run(
        ["ollama", "generate", MODEL, "--prompt", prompt, "--json"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("Ollama error:", result.stderr)
        return "Summary failed"

    output = json.loads(result.stdout)
    return output.get("content", "")
