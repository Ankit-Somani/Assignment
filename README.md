# TrueFoundry Assignment
This is a fastapi service, which takes input for the model (in the same format as the inference endpoints API of huggingface models on the huggingface hub website) and internally converts the input to V2 inference protocol and returns the response.

## Access the service hosted at:
* `https://fastapi-intern-ankit-8000.demo1.truefoundry.com/predict`

## Instructions to run the service locally: ##
* Clone the repository
  * `git clone https://github.com/Ankit-Somani/Assignment.git`
* Install the required python modules
  * `pip install -r requirements.txt`
* Run the FastAPI service using uvicorn
  * `uvicorn final:app --reload`
* Copy the url `http://127.0.0.1:8000/` shown in the terminal and open it in a browser.

## Utilizing the service: ##
* Make a POST request at `http://127.0.0.1:8000/predict`  OR  `https://fastapi-intern-ankit-8000.demo1.truefoundry.com/predict` with body as:
```
  {
      "hf_pipeline": "<hf-pipeline-name>", 
      "model_deployed_url": "<model-deployed-url>",
      "inputs": "<text>",
      "parameters": {...}
  }
   ```
   
* NOTE: Parameters support is not added for all optional parameters in text-generation model. Supported parameters are:
```
  "parameters": {
      "min_new_tokens": 10,
      "temperature": 1.0,
      "max_new_tokens": 20,
      "num_return_sequences": 5
  }
 
```

