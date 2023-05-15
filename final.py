import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class model_input(BaseModel):
    hf_pipeline: str
    model_deployed_url: str
    inputs: str
    parameters: dict[str, list[str]]   


@app.post("/predict/")
async def predict(input : model_input):
    if(input.hf_pipeline == "object-detection"):
        payload['inputs'][0]['name'] = "inputs"
        payload['inputs'][0]['parameters']['content_type'] = "string"
        payload['inputs'][0]['data'] = input.inputs
        response = requests.post(input.model_deployed_url, json=payload, headers=headers)
        res = response.json()
        if(response.status_code==200):          
            return res['outputs'][0]['data'][0]
        return res
    
    if(input.hf_pipeline == "text-generation"):
        payload['inputs'][0]['name'] = "text_inputs"
        payload['inputs'][0]['parameters']['content_type'] = "string"
        payload['inputs'][0]['data'] = input.inputs
        response = requests.post(input.model_deployed_url, json=payload, headers=headers)
        res = response.json()
        if(response.status_code==200):          
            return res['outputs'][0]['data'][0]
        return res

    if(input.hf_pipeline == "zero-shot-classification"):
        payload2['inputs'][0]['parameters']['content_type'] = "string"
        payload2['inputs'][0]['data'] = input.inputs
        payload2['inputs'][1]['data'] = input.parameters['candidate_labels']
        response = requests.post(input.model_deployed_url, json=payload2, headers=headers)
        res = response.json()
        if(response.status_code==200):          
            return res['outputs'][0]['data'][0]
        return res

    if(input.hf_pipeline == "token-classification"):
        payload['inputs'][0]['name'] = "inputs"
        payload['inputs'][0]['parameters']['content_type'] = "string"
        payload['inputs'][0]['data'] = input.inputs
        response = requests.post(input.model_deployed_url, json=payload, headers=headers)
        res = response.json()
        if(response.status_code==200):          
            return res['outputs'][0]['data'][0]
        return res

    else: 
        return "Pipeline not found!"

payload = {
    "id": "string",
    "parameters": {
        "content_type": "string",
        "headers": {}
    },
    "inputs": [
        {
            "name": "",
            "shape": [-1],
            "datatype": "BYTES",
            "parameters": {
                "content_type": "",
                "headers": {}
            },
            "data": ""
        }
    ]
}
payload2 = {
    "id": "string",
    "parameters": {
        "content_type": "string",
        "headers": {}
    },
    "inputs": [
        {
            "name": "array_inputs",
            "shape": [-1],
            "datatype": "BYTES",
            "parameters": {
                "content_type": "string",
                "headers": {}
            },
            "data": ""
        },
        {
            "name": "candidate_labels",
            "shape": [-1],
            "datatype": "BYTES",
            "parameters": {
                "content_type": "string",
                "headers": {}
            },
            "data": ""
        }
    ],
    "outputs": [
        {
            "name": "string",
            "parameters": {
                "content_type": "string",
                "headers": {}
            }
        } 
    ]  
}
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}



    
