import os
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    Duration,
)
from constructs import Construct


class ServerlessStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        api = apigw.RestApi(self, "API")

        def build_lambda(scope, id, handler):
            return _lambda.Function(
                scope,
                id,
                runtime=_lambda.Runtime.PYTHON_3_12,
                handler=handler,
                code=_lambda.Code.from_asset(
                    "../aws/lambda_handlers",
                    bundling={
                        "image": _lambda.Runtime.PYTHON_3_12.bundling_image,
                        "command": [
                            "bash",
                            "-c",
                            "pip install -r requirements-lambda.txt -t /asset-output && cp -au . /asset-output",
                        ],
                    },
                ),
                memory_size=256,  # Increase memory to improve CPU performance
                timeout=Duration.seconds(30),  # Increase timeout
                environment={
                    "PYTHONOPTIMIZE": "2"  # Enable Python optimizations
                }
            )

        routes = ["route1", "route2"]
        for route in routes:
            lambda_function = build_lambda(
                self,
                f"{route.capitalize()}Function",
                f"{route}_handler.lambda_handler"
            )

            resource = api.root.add_resource(route)
            resource.add_method("GET", apigw.LambdaIntegration(lambda_function))

        # def build_lambda(scope, id, handler):
        #     return _lambda.Function(
        #         scope,
        #         id,
        #         runtime=_lambda.Runtime.PYTHON_3_12,
        #         architecture=_lambda.Architecture.ARM_64,
        #         handler=handler,
        #         code=_lambda.Code.from_asset(
        #             "../aws/lambda_handlers",
        #             bundling={
        #                 "image": _lambda.Runtime.PYTHON_3_12.bundling_image,
        #                 "command": [
        #                     "bash",
        #                     "-c",
        #                     "pip install -r requirements-lambda.txt -t /asset-output && cp -au . /asset-output",
        #                 ],
        #             },
        #         ),
        #         timeout=Duration.seconds(30),  # Increase timeout
        #         environment={"PYTHONOPTIMIZE": "2"},  # Enable Python optimizations
        #     )

        # routes = ["route1", "route2"]
        # for route in routes:
        #     lambda_function = build_lambda(
        #         self, f"{route.capitalize()}Function", f"{route}_handler.handler"
        #     )

        #     resource = api.root.add_resource(route)
        #     resource.add_method("GET", apigw.LambdaIntegration(lambda_function))
