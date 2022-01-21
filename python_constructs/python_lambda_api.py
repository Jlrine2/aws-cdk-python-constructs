from dataclasses import dataclass
from typing import Mapping, Optional, Union

from aws_cdk import (
    Duration,
    aws_lambda_python_alpha as lambda_python,
    aws_logs as logs,
    aws_apigateway as apigateway
)
from constructs import Construct


@dataclass
class LambdaApiPythonParams:
    function_code_location: str
    function_handler: str
    function_index: str
    function_environment: Optional[Mapping[str, str]] = None
    function_log_retention: Optional[logs.RetentionDays] = None
    function_memory_size: Union[int, float, None] = None
    funtion_timeout: Optional[Duration] = Duration.seconds(30)
    api_deploy: Optional[bool] = None
    api_deploy_options: Optional[apigateway.StageOptions] = None
    api_domain_name: Optional[apigateway.DomainNameOptions] = None
    api_headers_parameters: Optional[Mapping[str, str]] = None



class LambdaApiPython(Construct):
    def __init__(self, scope: Construct, _id: str, params: LambdaApiPythonParams = None):
        super().__init__(scope, _id)
        if params is None:
            raise ValueError('Argument params is required')

        function = lambda_python.PythonFunction(
            self, f'{_id}_function',
            entry=params.function_code_location,
            handler=params.function_handler,
            index=params.function_index,
            environment=params.function_environment,
            log_retention=params.function_log_retention,
            memory_size=params.function_memory_size,
            timeout=params.funtion_timeout
        )

        api = apigateway.LambdaRestApi(
            self, f'{_id}-api',
            handler=function,
            proxy=True,
            deploy=params.api_deploy,
            deploy_options=params.api_deploy_options,
            domain_name=params.api_domain_name,
            parameters=params.api_headers_parameters,
        )
