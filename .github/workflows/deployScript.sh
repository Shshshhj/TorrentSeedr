# Due to a bug in appleboy/ssh-action@master, some commands shows error and fails to execute.
# So, running a bash file instead of commands

echo $1 > /opt/TorrentSeedr/TorrentSeedr/src/config.json  && pkill -f torrentseedr.py ; source /opt/TorrentSeedr/venv/bin/activate && cd /opt/TorrentSeedr/TorrentSeedr && wget -P src/inline/ https://raw.githubusercontent.com/hemantapkh/TorrentHunt/main/src/inline/inlineSearch.py && screen -dm python3 torrentseedr.py