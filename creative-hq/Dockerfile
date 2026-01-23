# Creative HQ Test Environment
FROM node:20-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    tmux \
    curl \
    git \
    vim \
    watch \
    && rm -rf /var/lib/apt/lists/*

# Install Claude Code
RUN npm install -g @anthropic-ai/claude-code

# Create workspace
WORKDIR /home/creative

# Copy Creative HQ files
COPY . /home/creative/

# Make scripts executable
RUN chmod +x start.sh start-simple.sh 2>/dev/null || true

# Set up a nice prompt
RUN echo 'PS1="\[\033[1;36m\]creative-hq\[\033[0m\] \w $ "' >> /root/.bashrc

# Default command
CMD ["/bin/bash"]
