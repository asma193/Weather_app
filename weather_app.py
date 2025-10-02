import streamlit as st
import requests

API_KEY = "169ebc28728e44fce0c30dc53c8c4eb1"  # apni key yahan daalo
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

st.title("🌤 Weather Forecast App")

city = st.text_input("Enter City Name")

if st.button("Get Weather"):
    if city:
        url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            main = data["main"]
            weather = data["weather"][0]
            st.success(f"📍 City: {city}")
            st.write(f"🌡 Temperature: {main['temp']}°C")
            st.write(f"🥵 Feels Like: {main['feels_like']}°C")
            st.write(f"💧 Humidity: {main['humidity']}%")
            st.write(f"🌥 Weather: {weather['description'].title()}")
        else:
            st.error("⚠️ City not found, please try again.")
    else:
        st.warning("Please enter a city name.")
