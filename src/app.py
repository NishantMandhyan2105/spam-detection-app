from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pickle

model = pickle.load(open("model/model_knn.pkl", "rb"))
app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,          # 👈 IMPORTANT (first arg nahi, named arg)
        name="index.html",
        context={}
    )
model = pickle.load(open("model/model_knn.pkl", "rb"))
@app.get("/predict", response_class=HTMLResponse)
def predict(request: Request, text: str):
    prediction = model.predict([text])[0]
    result = "🚨 Spam" if prediction == 1 else "✅ Not Spam"

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"result": result}
    )