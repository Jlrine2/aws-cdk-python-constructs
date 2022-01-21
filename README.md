# Python AWS CDK Constructs
I created this project to contain common patters CDK Constructs, for use in other AWS projects.

### Disclaimer
This is something I maintain to make side projects easier, it's not meant to be reliable or robust but instead 
to alleviate the challenges with provisioning infrastructure for small personal projects. use at your own risk.

## Install
This project is not hosted on PyPi but can be installed using pip with
```shell
pip instal git+https://github.com/Jlrine2/aws-cdk-python-constructs.git
```

## Usage

#### Python Lambda Api

This package includes a construct to create a serverless api using api gateway and lambda with python code

```python
from aws_cdk import Stack
from constructs import Construct

from python_constructs import python_lambda_api

class YourStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        python_lambda_api.LambdaApiPython(
            self, "test-api",
            params=python_lambda_api.LambdaApiPythonParams(
                function_code_location='path/to/lambda/code/from/repo/root',
                function_index='file_lambda_hanlder_is_in',
                function_handler='name_of_lambda_handler_function'
            )
        )
```
if your api has dependancies, this construct will install any automatically from `requirements.txt` 
within the `function_code_location` directory
