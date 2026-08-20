---
title: Weather App
sdk: docker
app_port: 7860
---

# Weather App

A Python Streamlit app that gets the current weather for a city using the OpenWeather API.

## Setup

Install the required libraries:

pip install streamlit requests python-dotenv

Create a .env file and add your API key:

OPENWEATHER_API_KEY=your_api_key_here

## Run the app:

streamlit run streamlit_app.py

Enter a city to see its temperature, humidity, and weather conditions.


## Python version
Python 3.13.9