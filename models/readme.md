# News Classifier Models

This repository contains the final versions of the news classification models. These models are designed to categorize news articles into predefined labels using machine learning and deep learning techniques.

## 🚀 Model Downloads

You can download the final model files using the links below:

* [cite_start]**Pickle Format (Scikit-learn/Joblib):** [news-final-classifier-stage.pkl](https://drive.google.com/file/d/1fuhW4hpIsLmlKlwadirXNzquwU3F5Xxw/view?usp=sharing) 
* [cite_start]**ONNX Format (Cross-platform Inference):** [news-classifier-final-version.onnx](https://drive.google.com/file/d/1vwKPcRc28kgrJ_jS6MDkNyNx6eE6NEtd/view?usp=sharing) 
* [cite_start]**ONNX Data Weights:** [news-classifier-final-version.onnx.data](https://drive.google.com/file/d/1rILhNxyiOb8LnWiJbsRVwyVpnokjIBIf/view?usp=sharing) 

## 🛠 Usage

### Using the Pickle Model
The `.pkl` file is ideal for rapid deployment in Python environments using libraries like `pickle` or `joblib`.

```python
import joblib

# Load the model
model = joblib.load('news-final-classifier-stage.pkl')

# Make a prediction
prediction = model.predict(["Your news text here"])
print(prediction)