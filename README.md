# Dice Roller Game

Starting point: [Intermediate-python course of GitHub Lab](https://lab.github.com/everydeveloper/intermediate-python)
- Create a dice-rolling program using python.
- This repo also contains the original course materials under the issues tab. 

Own implementation just for playing with Python and logic.

**The APP only runs in the terminal.**

<------------   **USING DOCKER**   ------------->

For using the app (overcoming docker-compose limits with terminal input - EOF ERROR)
Run following commands in this order:

docker-compose up
docker ps ----> copy container id
docker exec -it <container id> sh
python3 dice_roller.py

ctrl+d: close app inside sh

<------------   **WITHOUT DOCKER**   ------------->

python3 dice_roller.py
ctrl+c: close app