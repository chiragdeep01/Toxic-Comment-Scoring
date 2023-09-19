# Toxic-Comment-Scoring

In the modern era of online communication, managing and moderating user-generated content is crucial for maintaining healthy and safe online communities. The "Toxic Comment Scoring" project is a Deep learning solution designed to automatically identify and score toxic comments in online discussions, forums, social media platforms, and more.

# Setup
- Clone the repo using:
```console
git clone https://github.com/chiragdeep01/Toxic-Comment-Scoring.git
```
- Create Enviroment:
```console
conda create -n toxic python==3.11.5
cd Toxic-Comment-Scoring
pip install -r requirements.txt
````
# Usage

I have trained a LSTM based deep learning model to output score for 6 different classes for toxicity measure and they are:
- toxic
- severe_toxic
- obscene
- threat
- insult
- identity_hate

The model implementation and inference is under [./toxicModel/](https://github.com/chiragdeep01/Toxic-Comment-Scoring/tree/main/toxicModel)
## API
I have created an API using FASTAPI to generate predictions and for that you can just use the [run.py](https://github.com/chiragdeep01/Toxic-Comment-Scoring/blob/main/run.py) file:
```console
python run.py
```
API DESCRIPTION:
```http
POST localhost:8080
```
| Key | Value | Type | 
| :--- | :--- | :---|
| `text` | `You are an idiot` | `string` |

JSON:
```json
{
    "text" : "You are an idiot"
}
```

RESPONSE:
```javascript
{
    "toxic": "0.81315887",
    "severe_toxic": "0.050926227",
    "obscene": "0.48636666",
    "threat": "0.017364092",
    "insult": "0.43801567",
    "identity_hate": "0.052807126"
}
```
## PYTHON 
For Python you can Import toxicModel and do direct inference. Example:
```python
import toxicModel

toxic_model = toxicModel.Model(device = "gpu:0")
result = toxic_model.predict("hello how are you")
print(result)
```
By default the device is set to auto and will automatically find the gpu id if present and will load the model to gpu otherwise onto cpu. For cpu just pass "cpu" as device.

# DATASET
I have trained the model on dataset I found on kaggle - [LINK](https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge/data)