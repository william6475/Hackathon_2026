import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

#Importing data
#-----------------------------------------------------------------------------------------------------
model_data = pd.read_csv('sales_data.csv')
pd.set_option('display.max_rows', None)#Ensure pandas does not truncate data
pd.set_option('display.max_columns', None)
data_frame = pd.DataFrame(model_data) #Convert data to dataframe


#Clean the data
#-----------------------------------------------------------------------------------------------------
#Split Date into year, month, day
data_frame[['Year', 'Month', 'Day']] = data_frame['Date'].str.split('-',  expand = True)
data_frame = data_frame.drop('Date', axis = 1)

#Remove the S prefix from the Store_ID
data_frame['Store ID'] = data_frame['Store ID'].str.split('S').str[1]
#Remove the P prefix from Product ID
data_frame['Product ID'] = data_frame['Product ID'].str.split('P').str[1]

#Encode each string column (So skillet learn can understand it)
encoder = OneHotEncoder(sparse_output=False)
encoded_categories = encoder.fit_transform(data_frame[['Category']])
encoded_regions = encoder.fit_transform(data_frame[['Region']])
encoded_weather_conditions = encoder.fit_transform(data_frame[['Weather Condition']])
encoded_seasons = encoder.fit_transform(data_frame[['Seasonality']])

#Convert string columns storing int values to int columns
data_frame['Year'] = data_frame['Year'].astype(int)
data_frame['Month'] = data_frame['Month'].astype(int)
data_frame['Day'] = data_frame['Day'].astype(int)
data_frame['Store ID'] = data_frame['Store ID'].astype(int)
data_frame['Product ID'] = data_frame['Product ID'].astype(int)
data_frame['Inventory Level'] = data_frame['Inventory Level'].astype(int)
data_frame['Units Sold'] = data_frame['Units Sold'].astype(int)
data_frame['Units Ordered'] = data_frame['Units Ordered'].astype(int)
data_frame['Price'] = data_frame['Price'].astype(int)
data_frame['Discount'] = data_frame['Discount'].astype(int)
data_frame['Promotion'] = data_frame['Promotion'].astype(int)
data_frame['Competitor Pricing'] = data_frame['Competitor Pricing'].astype(int)
data_frame['Epidemic'] = data_frame['Epidemic'].astype(int)
data_frame['Demand'] = data_frame['Demand'].astype(int)

#Create, train and test the algorythm
#-----------------------------------------------------------------------------------------------------
#Give x the data from the dataframe (Not demand which will be predicted)
x_before_strings_added = data_frame.drop(['Demand', 'Category', 'Region', 'Weather Condition', 'Seasonality'], axis=1)
x = pd.concat([x_before_strings_added,
               pd.DataFrame(encoded_categories),
    pd.DataFrame(encoded_weather_conditions),
    pd.DataFrame(encoded_regions),
    pd.DataFrame(encoded_seasons),
               ], axis=1) #Add all the data to x

x.columns = x.columns.astype(str)

#Give Y past demand data
y = data_frame['Demand']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

#Creating random forrest regression model to make predictions
model = RandomForestRegressor(n_jobs = 1)
model.fit(x_train, y_train)

#Test how well the model fairs with new data
print(model.score(x_test, y_test))

#Sale the predictive_algorythm to a file
#-----------------------------------------------------------------------------------------------------
joblib.dump(model, "demand_prediction_algorythm.joblib")