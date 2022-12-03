import requests
from datetime import datetime
import smtplib
import time

my_Email = "" #USER EMAIL
password ="" #USER PASSWORD


MY_LAT = 12.971599
MY_LNG = 77.594566


def is_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    latitude =  float(data['iss_position']['latitude'])
    longitude = float(data['iss_position']['longitude'])
    iss_position = (latitude, longitude)
    if 8<=latitude<=17  and 72<=longitude<=82:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted":0,
    }
    response2 = requests.get(url="https://api.sunrise-sunset.org/json", params = parameters)
    response2.raise_for_status()
    data = response2.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])
    timenow = datetime.now()
    timehour = int(timenow.hour)
    if timehour>=sunset and timehour<=sunrise:
        return True

while True:
    time.sleep(60)

    if is_iss() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_Email,password=password)
        connection.sendmail(from_addr=my_Email, to_addrs="majumdar_utkarsh@srmap.edu.in", msg="Subject:LOOK UP \n\n THE ISS IS ABOVE YOU IN THE SKY!")


