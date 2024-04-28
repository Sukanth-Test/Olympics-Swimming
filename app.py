import streamlit as st
# import datetime
import numpy as np
# from tensorflow import keras
from keras.models import load_model
from sklearn.preprocessing import StandardScaler
import joblib
import logging
import traceback

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

st.set_page_config(page_title="Local Swimming Records Prediction", page_icon=":swimmer:")

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #fff;
    color: #000;
    transition: .3s
}

div.stButton > button:hover {
    background-color: #094613 ;
    color: white;
}

</style>""", unsafe_allow_html=True)

def predict(athlete_name, athlete_gender, distance, stroke_style, age):
    try:
        loaded_model = load_model("models/finetuned_nn_model.h5")
        loaded_scaler = joblib.load("scaler_obj.joblib")

        input = np.array([distance, stroke_style, athlete_gender, age]).reshape(1, -1)
        input_scaled = loaded_scaler.transform(input)

        pred = loaded_model.predict(input_scaled)
        pred = np.round(pred[0][0], 2)

        result = ""
        mins = str(int(pred // 60))
        secs = str(np.round((pred % 60), 2))
        
        secs = secs.split(".")
        if len(secs[0]) == 1:
            secs[0] = "0"+secs[0]
        secs = ".".join(secs)

        if len(mins) == 1:
            mins = "0"+mins
        
        result = mins+":"+secs

        prediction = st.header(f"Prediction for {athlete_name}: {result}")

        return prediction
    except Exception as e:
        logging.error("An error occurred in predict function:")
        logging.error(traceback.format_exc())
        raise e

# Main function to create the Streamlit app
def main():
    st.header("Utilising Olympic Swimming Record Times to Predict Local Swimming Records :swimmer:")
    st.info('Fill in the details below and click submit to get the prediction.')

    # current_year = datetime.datetime.now().year

    # Input fields
    athlete_name = st.text_input('Athlete Name')

    athlete_gender = st.radio('Athlete Gender', ['Male', 'Female'])
    athlete_gender = 0 if athlete_gender=='Male' else 1
    
    birth_year = st.number_input('Athlete Birth Year', min_value=1900, max_value=2090, step=1)

    distance_category = st.selectbox('Distance (in meters)', ['50m', '100m', '200m', '400m', '800m', '1500m'])
    distance_mapping = {
    '50m': 0,
    '100m': 1,
    '200m': 2,
    '400m': 3,
    '800m': 4,
    '1500m': 5
    }
    distance = distance_mapping.get(distance_category)


    stroke_style_category = st.selectbox('Stroke Style', ['Freestyle', 'Backstroke', 'Breaststroke', 'Butterfly', 'Medley'])
    stroke_style_mapping = {
    'Backstroke': 0,
    'Breaststroke': 1,
    'Butterfly': 2,
    'Freestyle': 3,
    'Medley': 4
    }
    stroke_style = stroke_style_mapping.get(stroke_style_category)

    game_year = st.number_input('Game Year', min_value=1900, max_value=2090, step=1)

    age = game_year - birth_year

    # Submit button
    if st.button('Submit') and athlete_name:
        # Call predict function with input values
        prediction = predict(athlete_name, athlete_gender, distance, stroke_style, age)
        # Display prediction
        print(prediction)

# Run the app
if __name__ == '__main__':
    main()
