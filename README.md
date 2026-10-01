# 🌸 Iris Multiclass Classification

A beginner-friendly **Machine Learning project** that predicts the species of an Iris flower using **multiclass classification**.

The model learns from flower measurements and predicts one of three Iris species: **Setosa, Versicolor, or Virginica**.

---

## 📌 Project Overview

The model uses four features to identify the flower species:

* 🌿 Sepal Length
* 🌿 Sepal Width
* 🌸 Petal Length
* 🌸 Petal Width

This project demonstrates the complete basic workflow of a classification problem — from loading and preprocessing the dataset to training a model and predicting new data.

---

## 🎯 Classes

The model predicts one of three classes:

| Class | Flower          |
| ----- | --------------- |
| 0     | Iris-setosa     |
| 1     | Iris-versicolor |
| 2     | Iris-virginica  |

The class labels are converted into numerical values using **LabelEncoder** during training and converted back to their original names after prediction.

---

## 🧠 Machine Learning Workflow

```text
                Iris Dataset
                     ↓
              Data Preprocessing
                     ↓
          Separate Features & Target
                     ↓
               Label Encoding
                     ↓
             Train-Test Split
                     ↓
              Model Training
                     ↓
                Prediction
                     ↓
             Flower Species 🌸
```

---

## 🛠️ Technologies & Libraries

* 🐍 Python
* 🐼 Pandas
* 🤖 Scikit-learn
* 🔢 LabelEncoder
* 📊 Train-Test Split
* 📈 Classification Model

---

## 📚 Concepts Learned

Through this project, I practiced:

* Multiclass Classification
* Feature and target separation
* Data preprocessing
* Handling categorical target labels
* Label Encoding
* Train-Test Split
* Model Training
* Model Prediction
* Making predictions on new/unseen data
* Converting encoded predictions back to original class names

---

## 🚀 How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/iris-multiclass-classification.git
```

### 2️⃣ Open the project folder

```bash
cd iris-multiclass-classification
```

### 3️⃣ Install the required libraries

```bash
pip install pandas scikit-learn
```

### 4️⃣ Run the program

```bash
python main.py
```

The program will train the classification model and make predictions using the Iris dataset.

---

## 🔮 Example Prediction

The model can predict the species of a new flower using its measurements.

### Input

```text
Sepal Length: 6.0
Sepal Width: 2.9
Petal Length: 4.5
Petal Width: 1.5
```

### Output

```text
Predicted flower: Iris-versicolor
```

---

## 📂 Project Structure

```text
iris-multiclass-classification/
│
├── main.py
├── iris.csv
└── README.md
```

---

## 💡 Why This Project?

The Iris dataset is a simple way to understand how **classification models learn patterns from data** and use those patterns to classify new observations.

This project was built as part of my hands-on journey in **Machine Learning and AI**.

---

## 🌱 Learning Journey

This project helped me move from understanding **binary classification** to working with **multiple classes** in a real machine learning workflow.

> Learning Machine Learning one model at a time. 🤖🌸

---

## 👩‍💻 Author

**Preethi A**

CSE (AI & ML) Student | AI & ML Learner

Exploring **Python • Java • DSA • Machine Learning • AI**

---

⭐ If you found this project useful, feel free to explore the repository!
