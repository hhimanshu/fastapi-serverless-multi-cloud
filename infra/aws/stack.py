from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)
from constructs import Construct

class ServerlessStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        api = apigw.RestApi(self, "API")

        routes = ["route1", "route2"]
        for route in routes:
            lambda_function = _lambda.Function(
                self, f"{route.capitalize()}Function",
                runtime=_lambda.Runtime.PYTHON_3_9,
                handler=f"{route}_handler.handler",
                code=_lambda.Code.from_asset("infra/aws/lambda_handlers"),
            )

            resource = api.root.add_resource(route)
            resource.add_method("GET", apigw.LambdaIntegration(lambda_function))