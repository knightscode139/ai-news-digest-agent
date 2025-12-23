# AI News Digest Agent

Automatically searches, analyzes, and summarizes the 5 most important AI technology news stories from the past 24 hours. Uses LangChain agents with Tavily web search and DeepSeek API to generate detailed explanations focused on AI engineers. Runs daily via systemd timers with persistent execution (catches missed runs when computer was off).

## Setup

```bash
# Install dependencies
uv venv
source .venv/bin/activate
(uv) pip install -r requirements.txt

# Add API keys to .env
echo "TAVILY_API_KEY=your_key" > .env
echo "DEEPSEEK_API_KEY=your_key" >> .env
```

Get API keys: [Tavily](https://tavily.com/) | [DeepSeek](https://platform.deepseek.com/)

**Edit `ai-news-agent.sh` with your paths:**

Open the file and update:
```bash
cd .../ai-news-digest-agent              # Your project path
source .venv/bin/activate                     # Your venv path
python3 ai-news-agent.py > .../daily-news.txt  # Output path
```

Adjust paths to match your setup.

**Make script executable:**
```bash
chmod +x ai-news-agent.sh
```

## Usage

**Manual run:**
```bash
python3 ai-news-agent.py
# or
./ai-news-agent.sh
```

**Automated (systemd timer):**

For daily automated execution, systemd user timers are configured. See systemd documentation or existing setup files for configuration details.