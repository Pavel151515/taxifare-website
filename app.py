import streamlit as st

'''
# TaxiFareModel Price Predictor
'''

'''
# Please provide us with the needed informations
'''


import datetime

d = st.date_input(
    "When would you like a taxi? ",
    datetime.date(2019, 7, 6))
st.write('Your chosen time is:', d)

number_long_p = st.number_input('Insert the pickup longitude')
number_lat_p = st.number_input('Insert the pickupt latitude')
number_long_d = st.number_input('Insert the dropoff longitude')
number_lat_d = st.number_input('Insert the dropoff latitude')
number_pass = st.number_input('Insert number of passengers')



url = 'https://taxifare-34544785528.asia-northeast1.run.app'


import requests

import streamlit as st
import datetime
import pandas as pd
import requests


if number_pass and number_lat_p and number_long_p and number_lat_d and number_long_d:
    locs = pd.DataFrame([
        {"lat": number_lat_p, "lon": number_long_p, "marker": "pickup"},
        {"lat": number_lat_d, "lon": number_long_d, "marker": "dropoff"},
    ])
    st.map(locs)


if st.button("Get your fare prediction"):

    dt = datetime.datetime.combine(d, datetime.time(12,0,0))
    payload = {
        "pickup_datetime": dt.strftime("%Y-%m-%d %H:%M:%S"),
        "pickup_longitude": number_long_p,
        "pickup_latitude":  number_lat_p,
        "dropoff_longitude": number_long_d,
        "dropoff_latitude":  number_lat_d,
        "passenger_count":   int(number_pass),
    }


    resp = requests.get(f"{url}/predict", params=payload)
    resp.raise_for_status()
    fare = resp.json()["fare"]


    st.success(f"💸 Predicted fare: ${fare:.2f}")

    st.write("### Route on the map")
    st.map(locs)
