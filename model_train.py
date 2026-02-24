import pandas as pd
from xgboost import XGBRegressor
import pickle

cars_df = pd.read_csv("cars24-car-price-cleaned-new.csv")

x = cars_df[["km_driven", "mileage", "age", "Petrol", "Diesel", "Electric"]]
y = cars_df["selling_price"]

xgb_model = XGBRegressor(
    n_estimators=200,
    learning_rate=0.2,
    max_depth=6
)

#Fit the model
xgb_model.fit(x, y)

#Save the model
with open("xgb_cars_price_model.pkl", "wb") as f:
    pickle.dump(xgb_model, f)