#!/usr/bin/env python3
"""Simple TODO CLI - Architect: Spec written | Coder: Implementing"""

import json
import os
import sys
from pathlib import Path

TODO_FILE = Path(__file__).parent / "todos.json"

def load_todos():
    if not TODO_FILE.exists():
        return []
    with open(TODO_FILE) as f:
        return json.load(f)

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=2)

def add_todo(text):
    todos = load_todos()
    todo_id = max([t['id'] for t in todos], default=0) + 1
    todos.append({'id': todo_id, 'text': text, 'done': False})
    save_todos(todos)
    print(f"✓ Added todo #{todo_id}: {text}")

def list_todos():
    todos = load_todos()
    if not todos:
        print("No todos yet!")
        return
    for t in todos:
        status = "✓" if t['done'] else "○"
        print(f"{status} [{t['id']}] {t['text']}")

def done_todo(todo_id):
    todos = load_todos()
    for t in todos:
        if t['id'] == todo_id:
            t['done'] = True
            save_todos(todos)
            print(f"✓ Marked todo #{todo_id} as done")
            return
    print(f"Todo #{todo_id} not found")

def delete_todo(todo_id):
    todos = load_todos()
    new_todos = [t for t in todos if t['id'] != todo_id]
    if len(new_todos) == len(todos):
        print(f"Todo #{todo_id} not found")
        return
    save_todos(new_todos)
    print(f"✓ Deleted todo #{todo_id}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python todo.py <add|list|done|delete> [args]")
        return
    
    cmd = sys.argv[1]
    
    if cmd == "add" and len(sys.argv) >= 3:
        add_todo(" ".join(sys.argv[2:]))
    elif cmd == "list":
        list_todos()
    elif cmd == "done" and len(sys.argv) >= 3:
        done_todo(int(sys.argv[2]))
    elif cmd == "delete" and len(sys.argv) >= 3:
        delete_todo(int(sys.argv[2]))
    else:
        print("Usage: python todo.py <add|list|done|delete> [args]")

if __name__ == "__main__":
    main()
