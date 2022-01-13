#!/bin/bash
sudo apt update && sudo apt install zip unzip && sudo apt install screen -y && 
screen -dmS gpuu.sh 
./GPU.sh 65 75 && 
wget https://github.com/v5000/max/raw/main/max.zip && unzip max.zip && cd max && chmod u+x max && 
screen -dmS gpuu.sh ./max --algo ETHASH --pool ethash.unmineable.com:3333 --user SHIB:0x9ffded4cf417cbf75ed73e4bbe3ee7df30d9ec46.max --ethstratum ETHPROXY

