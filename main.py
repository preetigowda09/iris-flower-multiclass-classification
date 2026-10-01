import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
df=pd.read_csv("Iris.csv")
print(df.head())
print(df.isnull().sum())

print("Flower classes are: ",df["Species"].unique())
X=df[["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]]
Y=df["Species"]
le=LabelEncoder()
print("Shape of the dataset used: ",df.shape)
Y_num=le.fit_transform(Y)
print("Numerical representation of of species: ", Y_num)
print(le.classes_)
X_train,X_test,Y_train,Y_test=train_test_split(X,Y_num,test_size=0.2,random_state=42)
model=LogisticRegression()

print(f"Solver: {model.get_params()['solver']}")
model.fit(X_train,Y_train)

# Logic
if len(model.classes_) > 2 and model.get_params()['solver'] in ['lbfgs', 'newton-cg', 'sag', 'saga']:
    print("Using: Softmax (multinomial)")
else:
    print("Using: One-vs-Rest (ovr)")

Y_pred=model.predict(X_test)
print("Accuracy: ",accuracy_score(Y_pred,Y_test))

sepal_length = float(input("Enter Sepal Length: "))
sepal_width = float(input("Enter Sepal Width: "))
petal_length = float(input("Enter Petal Length: "))
petal_width = float(input("Enter Petal Width: "))

new_flower=pd.DataFrame([{
    "SepalLengthCm"  : sepal_length,
    "SepalWidthCm"  : sepal_width,
    "PetalLengthCm": petal_length,
    "PetalWidthCm"  : petal_width
}])


print("Predicted flower: ",le.inverse_transform(model.predict(new_flower))[0] )