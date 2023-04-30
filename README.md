# Citrus-Hack-2023 (24 hour hackathon)
AIWantToWorkout is an AI fitness web application that sends you personalized workouts based on your fitness goals and available equipment (such as dumbbells, barbells, cables, or no equipment). Every morning, you will receive a text message for your scheduled workout for the day (or motivational message on your rest days)!


## API Setup

1) First cd into the api folder and make sure you have python 3.10.2+ installed

2) Create a virtual enviorment by running the following command
```
python -m venv env
```
3) next you need to activate your virtual enviorment
![image](https://user-images.githubusercontent.com/1534805/235315579-7cb65531-3c5c-49d1-8bb4-48b5ec9572cb.png)

4) Finally download all required packages into the virtual enviorment from required.txt file with the following command
```
pip install -r requirements.txt
```


## Vue FrontEnd setup

1) Make sure you have Javascript, Node.js, and NPM installed
2) CD into frontend directory
3) install all package dependencies with the following command
```
npm install
```
4) Once you are done installing the packages your front end will be setup

## How to Start the APP

1) Open two terminals
2) In your 1st teerminal cd into your api directory and activate your python virtual enviorment. Once that is activate run the following command in your terminal
```
flask run
```
* note: make sure your flask server is running on the default port 5000
3) next in your 2nd terminal cd into your Vue frontend folder and run the following command
```
npm run dev
```
4) now that both servers are running you can use the app by accessing your frontend url displayed in terminal
