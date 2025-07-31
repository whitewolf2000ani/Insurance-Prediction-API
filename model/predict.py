import pickle
import pandas as pd

# import the model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

MODEL_VERSION = "1.0.0"

# get class labels from (important for matching probablities to class names)
class_labels = model.classes_.tolist()


def predict_output(user_input: dict):
    input_df = pd.DataFrame([user_input])
    predicted_class = model.predict(input_df)[0]

    # get probablities for all classes
    probablities = model.predict_proba(input_df)[0]
    confidence = max(probablities)

    # create mapping {class_name:probablities}
    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probablities)))

    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence, 4),
        "class_probablities": class_probs,
    }  # type: ignore
