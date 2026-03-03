import json
from pathlib import Path

PROMPT_FOLDER = Path(__file__).parent

def read_template(file_name: str) -> str:
    path = PROMPT_FOLDER / file_name
    if not path.exists():
        raise FileNotFoundError(f"Template file not found: {file_name}")
    return path.read_text(encoding="utf-8").strip()

def file_message(content: list) -> str:
    template = read_template("message.txt")
    chat_memory_message = "\n".join(
        f"{msg['role'].upper()}: {msg['content']}" for msg in content
    ).strip()

    return template.format(chat_memory=chat_memory_message)

def file_memory(content: dict) -> str:
    template = read_template("memory.txt")
    return template.format(
        name=", ".join(content.get("name", [])).strip(),
        positive=", ".join(content.get("positive", [])).strip(),
        negative=", ".join(content.get("negative", [])).strip(),
        work=", ".join(content.get("work", [])).strip(),
        study=", ".join(content.get("study", [])).strip(),
        family=", ".join(content.get("family", [])).strip(),
        location=", ".join(content.get("location", [])).strip()
    )

def file_response_instruction(content: str) -> str:
    template = read_template("response.txt")
    return template.format(text=content.strip())