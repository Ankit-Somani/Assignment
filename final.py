import requests
from fastapi import FastAPI
from pydantic import BaseModel, Field
app = FastAPI()
from typing import Dict, Any, Optional
import json
import requests


class model_input(BaseModel):
    hf_pipeline: str
    model_deployed_url: str
    inputs: str
    parameters: Dict[str, Any] = Field(default_factory=dict)


@app.post("/predict/")
async def predict(input : model_input):
    if(input.hf_pipeline == "object-detection"):
        payload['inputs'][0]['name'] = "inputs"
        if("http" in input.inputs):
            payload['inputs'][0]['parameters']['content_type'] = "str"  
            payload['inputs'][0]['data'] = input.inputs        
        else:
            payload['inputs'][0]['data'] = input.inputs
            payload['inputs'][0]['parameters']['content_type'] = "pillow_image" 

        response = requests.post(input.model_deployed_url, json=payload, headers=headers)
        print("response")
        res = response.json()
        if(response.status_code==200): 
            output = []
            output.append(json.loads(res['outputs'][0]['data'][0]))
            return output
        return res
    
    if(input.hf_pipeline == "text-generation"):
        payload_text['inputs'][0]['name'] = "text_inputs"
        payload_text['inputs'][0]['parameters']['content_type'] = "string"
        payload_text['inputs'][0]['data'] = input.inputs
        if('top_k' in input.parameters): payload_text['inputs'][1]['data'] = input.parameters['top_k']
        if('top_p' in input.parameters): payload_text['inputs'][2]['data'] = input.parameters['top_p']
        if('temperature' in input.parameters): payload_text['inputs'][1]['data'][0] = str(input.parameters['temperature'])
        if('repetition_penalty' in input.parameters): payload_text['inputs'][4]['data'] = input.parameters['repetition_penalty']
        if('max_new_tokens' in input.parameters): 
            payload_text['inputs'][2]['data'][0] = str(input.parameters['max_new_tokens']) 
            print(payload_text['inputs'][1])   
        if('min_new_tokens' in input.parameters): payload_text['inputs'][3]['data'][0] = str(input.parameters['min_new_tokens']) 
              
        if('max_time' in input.parameters): payload_text['inputs'][6]['data'] = input.parameters['max_time']
        # if('return_full_text' in input.parameters): payload_text['inputs'][7]['data'] = input.parameters['return_full_text']
        if('num_return_sequences' in input.parameters): payload_text['inputs'][4]['data'][0] = str(input.parameters['num_return_sequences'])
        if('do_sample' in input.parameters): payload_text['inputs'][5]['data'][0] = str(input.parameters['do_sample'])
        response = requests.post(input.model_deployed_url, json=payload_text, headers=headers)
        res = response.json()
        if(response.status_code==200):          
            output = []
            output.append(json.loads(res['outputs'][0]['data'][0]))
            return output
        return res

    if(input.hf_pipeline == "zero-shot-classification"):
        payload2['inputs'][0]['parameters']['content_type'] = "string"
        payload2['inputs'][0]['data'] = input.inputs
        payload2['inputs'][1]['data'] = input.parameters['candidate_labels']
        print(payload2['inputs'][1]['data'])
        if('multi_label' in input.parameters): payload2['inputs'][2]['data'] = input.parameters['multi_label']
        response = requests.post(input.model_deployed_url, json=payload2, headers=headers)
        res = response.json()
        if(response.status_code==200):          
            output = []
            output.append(json.loads(res['outputs'][0]['data'][0]))
            return output
        return res

    if(input.hf_pipeline == "token-classification"):
        payload_token['inputs'][0]['name'] = "inputs"
        payload_token['inputs'][0]['parameters']['content_type'] = "string"
        payload_token['inputs'][0]['data'] = input.inputs
        if('aggregation_strategy' in input.parameters):
            payload_token['inputs'][0]['name'] = "array_inputs"
            payload_token['inputs'][1]['data'][0] = input.parameters['aggregation_strategy']
        response = requests.post(input.model_deployed_url, json=payload_token, headers=headers)
        res = response.json()
        if(response.status_code==200):          
            output = []
            output.append(json.loads(res['outputs'][0]['data'][0]))
            return output[0]
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
        },
        {
            "name": "multi_label",
            "shape": [-1],
            "datatype": "BOOL",
            "parameters": {
                "content_type": "string",
                "headers": {}
            },
            "data": "FALSE"
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

payload_token = {
    "id": "string",
    "parameters": {
        "content_type": "string",
        "headers": {}
    },
    "inputs": [
        {
            "name": "inputs",
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
payload_text = {
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
           "name": "temperature",
            "shape": [-1],
            "datatype": "BYTES",
            "parameters": {
                "content_type": "hg_json",
                "headers": {}
            },
            "data": ["1.0"] 
        },
        {
           "name": "max_new_tokens",
            "shape": [-1],
            "datatype": "BYTES",
            "parameters": {
                "content_type": "hg_json",
                "headers": {}
            },
            "data": ["25"]
        },
        {
           "name": "min_new_tokens",
            "shape": [-1],
            "datatype": "BYTES",
            "parameters": {
                "content_type": "hg_json",
                "headers": {}
            },
            "data": ["2"]
        },
        {
            "name": "num_return_sequences",
            "shape": [-1],
            "datatype": "BYTES",
            "parameters": {
                "content_type": "hg_json",
                "headers": {}
            },
            "data": ["1"]
        },
        
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



    
