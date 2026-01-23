#!/bin/bash

# Creative HQ - Simple Launcher (no tmux required)
# Opens your files in your editor + starts Claude

DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Starting Creative HQ..."
echo ""

# Open files in default editor (works with VS Code, Cursor, etc.)
if command -v code &> /dev/null; then
    code "$DIR"
elif command -v cursor &> /dev/null; then
    cursor "$DIR"
else
    open "$DIR"  # Opens in Finder, user can open files manually
fi

# Start Claude Code
echo "Launching Claude..."
echo "Tip: Run /chief-of-staff to get your briefing"
echo ""

cd "$DIR"
claude
