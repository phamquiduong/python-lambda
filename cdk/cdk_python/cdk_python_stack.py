from aws_cdk import Stack
from aws_cdk import aws_lambda as lambda_
from constructs import Construct


class CdkPythonStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.layer = self.create_layer()
        self.lambda_function = self.create_lambda_function(self.layer)

        # self.add_permission_lambda_access_layer(self.lambda_function, self.layer)

    def create_layer(self):
        return lambda_.LayerVersion(
            self, "MyLayer",
            code=lambda_.Code.from_asset("layer/packages"),
            compatible_runtimes=[lambda_.Runtime.PYTHON_3_11],
            description="Python dependencies",
        )

    def create_lambda_function(self, layer):
        return lambda_.Function(
            self, "MyFunction",
            runtime=lambda_.Runtime.PYTHON_3_11,
            handler="main.handler",
            code=lambda_.Code.from_asset("../src"),
            layers=[layer],
            description="My Lambda function using a layer",
        )

    def add_permission_lambda_access_layer(self, lambda_function, layer):
        layer.grant_usage(lambda_function)
