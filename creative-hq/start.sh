#!/bin/bash

# Creative HQ - Dashboard Launcher
# Sets up a tmux layout with your files visible + Claude ready to go

SESSION="creative-hq"
DIR="$(cd "$(dirname "$0")" && pwd)"

# Check if tmux is installed
if ! command -v tmux &> /dev/null; then
    echo "tmux not installed. Installing..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install tmux
    else
        echo "Please install tmux: sudo apt install tmux (Linux) or brew install tmux (Mac)"
        exit 1
    fi
fi

# Kill existing session if it exists
tmux kill-session -t $SESSION 2>/dev/null

# Create new session
tmux new-session -d -s $SESSION -c "$DIR"

# Rename first window to "dashboard"
tmux rename-window -t $SESSION:0 'dashboard'

# Split into layout:
# +------------------+------------------+
# |                  |     tasks.md     |
# |     Claude       +------------------+
# |                  |   projects.md    |
# +------------------+------------------+

# Split vertically (left = Claude, right = files)
tmux split-window -h -t $SESSION:0 -c "$DIR"

# Split right pane horizontally (top = tasks, bottom = projects)
tmux split-window -v -t $SESSION:0.1 -c "$DIR"

# Set up each pane
# Pane 0 (left): Claude Code
tmux send-keys -t $SESSION:0.0 'claude' Enter

# Pane 1 (top right): Watch tasks.md
tmux send-keys -t $SESSION:0.1 'watch -n 5 -c "cat tasks.md"' Enter

# Pane 2 (bottom right): Watch inbox.md
tmux send-keys -t $SESSION:0.2 'watch -n 5 -c "cat inbox.md"' Enter

# Set pane sizes (Claude gets more space)
tmux select-layout -t $SESSION:0 main-vertical

# Focus on Claude pane
tmux select-pane -t $SESSION:0.0

# Attach to session
tmux attach-session -t $SESSION

echo "Creative HQ is running!"
echo ""
echo "Keyboard shortcuts:"
echo "  Ctrl+B, Arrow  - Switch between panes"
echo "  Ctrl+B, D      - Detach (keeps running in background)"
echo "  Ctrl+B, X      - Close current pane"
