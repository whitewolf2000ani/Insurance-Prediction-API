from pydantic import BaseModel, Field
from typing import Dict


class PredictionResponse(BaseModel):
    predicted_category: str = Field(
        ...,
        description="The Predicted category of the Insurance Premium",
        example=["high", "medium", "low"]
    )

    confidence: float = Field(
        ...,
        description="The confidence or the Probablity of the predicted class(ranges from 0 to 1)",
        example=0.8543
    )

    class_probablities: Dict[str, float] = Field(
        ...,
        description="Confidence or Probabilities for the other classess",
        example={"low": 0.01, "medium": 0.15, "high": 0.84}
    )
