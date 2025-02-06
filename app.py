import os

from dotenv import load_dotenv
from langflow.load import run_flow_from_json

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

TWEAKS = {
  "ChatOutput-k6v1e": {
    "background_color": "",
    "chat_icon": "",
    "data_template": "{text}",
    "input_value": "",
    "sender": "Machine",
    "sender_name": "AI",
    "session_id": "",
    "should_store_message": True,
    "text_color": ""
  },
  "Prompt-oKLPL": {
    "template": "Reference 1:\n\n{references_1}\n\n---\n\n{references_2}\n\n---\n\n{references_3}\n\n---\n\n{instructions}\n\nBlog:",
    "tool_placeholder": "",
    "instructions": "",
    "references_1": "",
    "references_2": "",
    "references_3": ""
  },
  "GoogleGenerativeAIModel-Vgpqc": {
    "api_key": GOOGLE_API_KEY,
    "input_value": "",
    "max_output_tokens": None,
    "model_name": "gemini-2.0-flash",
    "n": None,
    "stream": False,
    "system_message": "",
    "temperature": 1,
    "tool_model_enabled": False,
    "top_k": None,
    "top_p": None
  },
  "URL-VHUgA": {
    "format": "Text",
    "urls": []
  },
  "ParseDataFrame-feugf": {
    "sep": "\n",
    "template": "{text}"
  },
  "TextInput-iKIqk": {
    "input_value": "Use as referências que te dei para fazer um blog casual sobre cachorros. O público são pessoas adultas de 25 a 34 anos."
  },
  "APIRequest-R4KNy": {
    "body": [],
    "curl": "curl -X 'GET' \\   'https://dogapi.dog/api/v2/breeds' \\   -H 'accept: application/json'",
    "follow_redirects": True,
    "headers": [],
    "include_httpx_metadata": False,
    "method": "GET",
    "save_to_file": False,
    "timeout": 5,
    "urls": [
      "https://dogapi.dog/api/v2/breeds"
    ],
    "use_curl": False
  },
  "File-Tw2Ir": {
    "path": "Dog_Breeds_information.docx",
    "concurrency_multithreading": 1,
    "delete_server_file_after_processing": True,
    "ignore_unspecified_files": False,
    "ignore_unsupported_extensions": True,
    "silent_errors": False,
    "use_multithreading": True
  },
  "ParseDataFrame-uUXVv": {
    "sep": "\n",
    "template": "{result}"
  },
  "ParseDataFrame-sSU9x": {
    "sep": "\n",
    "template": "{text}"
  },
  "MergeDataComponent-bCrLn": {
    "operation": "Merge"
  },
  "MergeDataComponent-7wEWa": {
    "operation": "Merge"
  },
  "ChatInput-BBP8H": {
    "files": "",
    "background_color": "",
    "chat_icon": "",
    "input_value": "",
    "sender": "User",
    "sender_name": "User",
    "session_id": "",
    "should_store_message": True,
    "text_color": ""
  },
  "Prompt-181oX": {
    "template": "{prompt_message}\n\nBusque quaisquer URLS enviadas nessa mensagem acima e me entregue-a. Entregue somente o valor da URL, sem mais nenhum texto. Use emojis com moderação.",
    "tool_placeholder": "",
    "prompt_message": ""
  },
  "GoogleGenerativeAIModel-RjTS2": {
    "api_key": GOOGLE_API_KEY,
    "input_value": "",
    "max_output_tokens": None,
    "model_name": "gemini-1.5-flash",
    "n": None,
    "stream": False,
    "system_message": "",
    "temperature": 1,
    "tool_model_enabled": False,
    "top_k": None,
    "top_p": None
  },
  "ParseData-B4ci5": {
    "sep": "\n",
    "template": "{text}"
  }
}

result = run_flow_from_json(flow="basic_prompt.json",
                            session_id="", # provide a session id if you want to use session state
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)