# Insurance-Prediction-API

A production-grade API for **predicting the premium category of a patient** based on demographic and lifestyle information. This project lets insurance companies, brokers, or developers seamlessly integrate robust premium estimation capabilities into their workflows.

---

## 🚀 Features

- Accurate **premium prediction** using trained machine learning models.
- Predicts premium category based on commonly used attributes: age, height, weight, Income in LPA, city tier, smoking status, City, Occupation.
- Customizable pipeline to retrain or update the model with new data.

---

## 🏥 Use Cases

- **Insurance companies**: Quick premium estimation for new applicants.
- **Healthcare apps**: Quote simulation for patients or users.
- **Developers/Students**: Experiment and learn about deploying ML models as APIs.

---

## 📊 Tech Stack

- **Language:** Python 3.x  
- **Framework:** FastAPI
- **ML Libraries:** scikit-learn, pandas, numpy  
- **Model:** *[List the algorithms you used, e.g., Random Forest, Linear Regression, etc.]*  
- **Deployment:** Pending will be using Docker 

---

## ⚡️ Quickstart

1. **Clone the repository:**
```
git clone https://github.com/whitewolf2000ani/Insurance-Prediction-API.git
cd Insurance-Prediction-API
 ```

2. **Set up virtual environment:**
```
python -m venv venv
source venv/bin/activate # On Unix or MacOS
.\venv\Scripts\activate # On Windows
```

3. **Install dependencies:**
```
pip install -r requrirements.txt
```

4. **Run the API:**
```
uvicorn app:app --reload
```


5. **Access the API** at `http://localhost:8000` (FastAPI).
---

## 🛠 API Endpoints

| Endpoint   | Method | Description                       |
|------------|--------|-----------------------------------|
| `/predict` | POST   | Predicts insurance premium category|
| `/health`  | GET    | Health status of the API           |

### Example request:
```json
POST /predict
{
"age": 35,
"weight":75,
"height":1.25,
"income_lpa":10,
"smoker": "yes",
"city": "Kolkata",
"occupation":"retired"
}
```

### Example response:
```json
{
  "response": {
    "predicted_category": "Medium",
    "confidence": 0.49,
    "class_probablities": {
      "High": 0.29,
      "Low": 0.22,
      "Medium": 0.49
    }
  }
}
```
---

## 🧠 Model Details

- **Features used:** Age, Sex, BMI, Children, Smoker, Region  
- **Model selection:** Random Forest Classifier is implemented in Python via the scikit-learn library. This algorithm combines the predictions of multiple decision trees, each trained on different random subsets of your data and features. For classification tasks, the final prediction is decided by a majority vote among all the decision trees in the forest.
- **Evaluation:** Confidence Scores, Class Probabilites  

---

## 📜 License

This project is licensed under the **MIT License**.