import openai
import json
from functions import get_upregulated_genes, get_downregulated_genes

openai.api_key = "your-api-key-here" 

function_schemas = [
    {
        "name": "get_upregulated_genes",
        "description": "Retrieve top N upregulated genes for a species and stage",
        "parameters": {
            "type": "object",
            "properties": {
                "species": {"type": "string"},
                "stage": {"type": "string"},
                "top_n": {"type": "integer", "default": 5}
            },
            "required": ["species", "stage"]
        }
    },
    {
        "name": "get_downregulated_genes",
        "description": "Retrieve top N downregulated genes for a species and stage",
        "parameters": {
            "type": "object",
            "properties": {
                "species": {"type": "string"},
                "stage": {"type": "string"},
                "top_n": {"type": "integer", "default": 5}
            },
            "required": ["species", "stage"]
        }
    }
]

def run_llm(query: str):
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[{"role": "user", "content": query}],
        functions=function_schemas,
        function_call="auto"
    )

    msg = response["choices"][0]["message"]

    if msg.get("function_call"):
        fn_name = msg["function_call"]["name"]
        args = json.loads(msg["function_call"]["arguments"])

        if fn_name == "get_upregulated_genes":
            return get_upregulated_genes(**args)
        elif fn_name == "get_downregulated_genes":
            return get_downregulated_genes(**args)

    return msg["content"]
