import asyncio
from groq import Groq

from agent.core.memory import save_user_fact, get_user_facts
from agent.core.message import save_chat_message, get_chat_history
from prompts.system_prompts.load_system_prompts import (
    file_message,
    file_memory,
    file_response_instruction
)
from agent.nlp.router import route_intent
from config.settings import settings

client = Groq(api_key=settings.LLM_API_KEY)

def generate_assistant_response(user_text: str, user_id: str) -> str:
    save_user_fact(user_id=user_id, content=user_text)

    context_parts = []

    if chat_history := get_chat_history(user_id=user_id):
        context_parts.append(file_message(chat_history) + "\n\n")

    if memory_facts := get_user_facts(user_id=user_id):
        context_parts.append(file_memory(memory_facts) + "\n\n")

    if tool_response := route_intent(context=user_text, telegram_id=user_id):
        context_parts.append(tool_response)

    context_parts.append(file_response_instruction(content=user_text) + "\n\n")

    context = "\n\n".join(context_parts)

    response = client.chat.completions.create(
        model=settings.LLM_MODEL,
        messages=[{"role": "user", "content": context}]
    )

    response_text = response.choices[0].message.content

    save_chat_message(user_id=user_id, content=user_text, role="user")
    save_chat_message(user_id=user_id, content=response_text, role="assistant")

    return response_text


async def generate_assistant_response_async(user_text: str, user_id: str) -> str:
    return await asyncio.to_thread(generate_assistant_response, user_text, user_id)