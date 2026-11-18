from fastapi import FastAPI

from pydantic import BaseModel

app=FastAPI()

forms=[]


class Form(BaseModel):
    title:str

    questions:list



@app.post('/forms')

def create_form(form: Form):
    forms.append(form)
    return form

# uvicorn main:app --reload