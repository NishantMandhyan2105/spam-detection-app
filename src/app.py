from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pickle

app = FastAPI()

# static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# templates
templates = Jinja2Templates(directory="templates")

# model load
model = pickle.load(open("model/model_knn.pkl", "rb"))

# HOME ROUTE (IMPORTANT 🔥)
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

# PREDICT
@app.get("/predict", response_class=HTMLResponse)
def predict(request: Request, text: str):
    prediction = model.predict([text])[0]
    result = "Spam" if prediction == 1 else "Not Spam"

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": result
        }
    )