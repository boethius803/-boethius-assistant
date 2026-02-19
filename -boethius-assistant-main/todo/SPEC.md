# Task Spec: Simple TODO CLI

## Goal
Create a simple TODO CLI tool in Python that runs in the workspace.

## Requirements
- Add todos: `python todo.py add "Buy milk"`
- List todos: `python todo.py list`
- Mark done: `python todo.py done <id>`
- Delete todos: `python todo.py delete <id>`
- Persist to `todos.json`

## File Structure
```
/home/node/.openclaw/workspace/todo/
├── todo.py      # Main CLI
└── todos.json   # Data file (auto-created)
```

## Acceptance Criteria
1. Can add a todo and see it in list
2. Can mark todo as done (shows ✓)
3. Can delete a todo
4. Data persists after restart
5. Handles missing todos.json gracefully
