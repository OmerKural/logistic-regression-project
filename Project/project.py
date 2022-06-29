import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


ad_data = pd.read_csv('advertising.csv')

ad_data.drop(["Ad Topic Line", "City", "Country", "Timestamp", "Male"] , axis=1, inplace=True)

x_train, x_test, y_train, y_test = train_test_split(ad_data.drop("Clicked on Ad", axis=1), 
                                                    ad_data["Clicked on Ad"], 
                                                    test_size=0.30, random_state=101)

logmodel = LogisticRegression()
logmodel.fit(x_train, y_train)

predictions = logmodel.predict(x_test)
print(classification_report(y_test, predictions))