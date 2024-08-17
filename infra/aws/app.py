#!/usr/bin/env python3
import aws_cdk as cdk
from stack import ServerlessStack

app = cdk.App()
ServerlessStack(app, "FastAPIServerlessStack")
app.synth()