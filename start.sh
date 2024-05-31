echo "Cloning Repo...."
git clone https://github.com/CodeXBots/Link-Search-Bot /Link-Search-Bot
cd /Link-Search-Bot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 main.py
