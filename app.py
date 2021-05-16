import streamlit as st
import pandas as pd
import requests
import json

astronauts = requests.get("http://api.open-notify.org/astros.json")
astro = json.loads(astronauts.text)

st.header("Astronauts in the Ocean")
st.markdown("Currently, there are " + str(astro["number"]) + " astronauts in space (aka ocean).")
st.subheader("You can see their names here:")
for i in range(len(astro["people"])):
    st.markdown(astro["people"][i]["name"])

iss = requests.get("http://api.open-notify.org/iss-now.json")
issloc = json.loads(iss.text)

st.subheader("I wonder where the ISS has vanished to?")
st.markdown("Answer: The ISS currently can be located at longitude " + str(issloc["iss_position"]["longitude"]) + " and latitude "
            + str(issloc["iss_position"]["latitude"]) + ".")

st.subheader("But.. Where is this on the map?")
lat = issloc["iss_position"]["latitude"]
long = issloc["iss_position"]["longitude"]

st.markdown("Eazy. Just check the red dot and you will find it.")

df = pd.DataFrame([float(lat), float(long)])
df = df.transpose()
df.rename(columns={0:"lat", 1:"lon"}, inplace=True)
st.map(df, 2)