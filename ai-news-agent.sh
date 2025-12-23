#!/usr/bin/bash
cd /home/a*/projects/ai-news-digest-agent || exit 1
source .venv/bin/activate
python3 ai-news-agent.py > ~/Masaüstü/daily-news.txt
deactivate
cd - || exit 1
