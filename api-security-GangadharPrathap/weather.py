import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
# print("API Key:", API_KEY)
city = input("Enter city: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Temperature:", data["main"]["temp"])

elif response.status_code == 429:
    print("Error: Rate limit exceeded. Try again later.")

else:
    print("Error:", response.status_code, response.text)