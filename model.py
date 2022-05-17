import joblib
import pandas as pd 
dataset = pd.read_csv("glass.csv")
x= dataset.iloc[:,:-1] #independent variable
y = dataset.iloc[:,9]   #dependent variable

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20,random_state=42)

from sklearn.preprocessing import StandardScaler

sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)


from sklearn.ensemble import RandomForestClassifier

cls = RandomForestClassifier(criterion= "entropy",n_estimators=300,random_state=42)
cls.fit(x_train,y_train)

# print("Accuracy is " ,cls.score(x_test,y_test)*100,"%")

filename = 'model.sav'
joblib.dump(cls,filename)
