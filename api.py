from fastapi import FastAPI
from pydantic import BaseModel
import toxicModel

toxic_model = toxicModel.Model()
app = FastAPI()

class Text(BaseModel):
    text:str

@app.post("/")
async def predict(text: Text):
    
    result = toxic_model.predict(text.text)
    # print(result)
    return {"toxic" : str(result[0]),
            "severe_toxic" : str(result[1]),
            "obscene" : str(result[2]),
            "threat" : str(result[3]),
            "insult" : str(result[4]),
            "identity_hate" : str(result[5]),
            }