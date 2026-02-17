import json
import os
from pathlib import Path
from typing import Dict, List

MEMORY_FILE = "conversation_memory.json"

def load_memory() -> Dict:
    """Load conversation memory from disk"""
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {"messages": [], "history": []}
    return {"messages": [], "history": []}

def save_memory(messages: List[Dict], history: List[Dict]) -> None:
    """Save conversation memory to disk"""
    memory_data = {
        "messages": messages,
        "history": history
    }
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory_data, f, indent=2)

def clear_memory() -> None:
    """Clear all conversation memory"""
    if os.path.exists(MEMORY_FILE):
        os.remove(MEMORY_FILE)
