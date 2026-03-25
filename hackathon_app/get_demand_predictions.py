import joblib

def get_demand_predictions(prediction_context):
    predictive_algorythm = joblib.load('demand_prediction_algorythm.joblib')
    predicted_demand = predictive_algorythm.predict(prediction_context)
    return predicted_demand