import joblib
import pandas as pd

#Takes a dictionary of values and returns predicted demand
def get_demand_predictions(prediction_context):
    predictive_algorythm = joblib.load('predictive_algorythm/demand_prediction_algorythm.joblib')
    encoder = joblib.load('predictive_algorythm/encoder.joblib')

    df = pd.DataFrame([prediction_context])
    
    #Split the date into year, month, day
    df[['Year', 'Month', 'Day']] = df['Date'].str.split('-', expand=True)
    df = df.drop('Date', axis = 1)

    # Convert string columns storing int values to int columns
    df['Year'] = df['Year'].astype(int)
    df['Month'] = df['Month'].astype(int)
    df['Day'] = df['Day'].astype(int)
    df['Store ID'] = df['Store ID'].astype(int)
    df['Product ID'] = df['Product ID'].astype(int)
    df['Inventory Level'] = df['Inventory Level'].astype(int)
    df['Units Sold'] = df['Units Sold'].astype(int)
    df['Units Ordered'] = df['Units Ordered'].astype(int)
    df['Price'] = df['Price'].astype(int)
    df['Discount'] = df['Discount'].astype(int)
    df['Promotion'] = df['Promotion'].astype(int)
    df['Competitor Pricing'] = df['Competitor Pricing'].astype(int)
    df['Epidemic'] = df['Epidemic'].astype(int)

    #Encode the string columns which have repeating values
    columns_to_encode = ['Category', 'Region', 'Weather Condition', 'Seasonality']
    encoded_columns = encoder.transform(df[columns_to_encode])
    encoded_columns = pd.DataFrame(encoded_columns)
    df = df.drop('Category', axis=1)
    df = df.drop('Region', axis=1)
    df = df.drop('Weather Condition', axis=1)
    df = df.drop('Seasonality', axis=1)

    formated_data = pd.concat([df, encoded_columns], axis=1)
    #Ensure column names match those used in training
    formated_data.columns = formated_data.columns.astype(str)
    formated_data = formated_data.reindex(columns=predictive_algorythm.feature_names_in_, fill_value=0)



    predicted_demand = predictive_algorythm.predict(formated_data)
    return predicted_demand

prediction_context = {"Date": "2022-01-01",
                      "Store ID": 1,
                      "Product ID": 1,
                      "Category": "Electronics",
                      "Region": "North",
                      "Inventory Level": 24,
                      "Units Sold": 22,
                      "Units Ordered": 2,
                      "Price": 72.72,
                      "Discount": 5,
                      "Weather Condition": "Snowy",
                      "Promotion": 1,
                      "Competitor Pricing": 92.02,
                      "Seasonality": "Winter",
                      "Epidemic": 0,
                      }
banana = get_demand_predictions(prediction_context)