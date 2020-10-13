from joblib import  load
import pandas as pd
from datetime import datetime
import numpy as np

import streamlit as st

model = load('regressor.joblib')


def predict_death_case(date, total_cases, new_cases, weekly_cases,biweekly_cases):
	date = pd.to_datetime(date)
	date = np.array(date.strftime('%y%m%d'))
	date = date.astype(np.int)
	prediction = model.predict([[date, total_cases, new_cases, weekly_cases,biweekly_cases]])

	return int(prediction)

def main():
	st.title("Nepal CoronaVirus Forecast")
	html_temp = """
	<div style="background-color:tomato;padding=10px">
	<h2 style="color:white;text-align:center;">CoronaVirus Forecast</h2>
	</div>
	"""

	st.markdown(html_temp, unsafe_allow_html=True)
	date = st.text_input("date", "Type Here(format: 2020-02-11)")
	total_cases = st.text_input("total_cases", "Type Here")
	new_cases = st.text_input("new_cases", "Type Here")
	weekly_cases = st.text_input("weekly_cases", "Type Here")
	biweekly_cases = st.text_input("biweekly_cases", "Type Here")
	
	result = ""

	if st.button("Predict"):
		result = predict_death_case(date, total_cases, new_cases, weekly_cases,biweekly_cases)
	st.success('New Death Case: {}'.format(result))
	if st.button('About'):
		st.text("CoronaVirus Forecast Powered by AI")


if __name__=='__main__':
	main()	
