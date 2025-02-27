# FastAPI Serverless Multi-Cloud

This project demonstrates a FastAPI application that can be deployed as serverless functions on both AWS Lambda and Azure Functions, with support for local development using Conda.

## Local Development

1. Install Miniconda or Anaconda if you haven't already.
2. Create a new Conda environment

```
conda create -n fastapi-serverless python=3.12
```

3. Activate the Conda environment:

```
conda activate fastapi-serverless
```

4. Install dependencies:

```
pip install -r requirements-dev.txt
```

5. Run the local server:

```
python local/main.py
```

## Deploying to AWS

1. Install the AWS CDK CLI: `npm install -g aws-cdk`
2. Configure your AWS credentials
3. Navigate to the `infra/aws` directory
4. Run `cdk deploy`

Note: AWS Lambda will use the `requirements.txt` file to install dependencies in the cloud environment. The local Conda environment is not used for deployment.

## Deploying to Azure

1. Install the Azure Functions Core Tools
2. Navigate to the `infra/azure/functions` directory
3. Run `func azure functionapp publish <YourFunctionAppName>`

Note: This setup uses Azure Functions with FastAPI directly, without additional wrapper libraries.

## Running Tests

Ensure you're in the Conda environment:

```
conda activate fastapi-serverless
```

Then run pytest in the project root directory:

```
pytest
```

## Project Structure

- `app/`: Contains the FastAPI application code
- `infra/`: Contains infrastructure-as-code for AWS and Azure
- `local/`: Contains code for local development
- `tests/`: Contains test files
- `requirements.txt`: Python dependencies for cloud deployments
- `requirements-dev.txt`: Additional dependencies for local development
- `environment.yml`: Conda environment definition for local development

## Note on Development vs Deployment Environments

This project uses Conda for local development to provide a consistent and isolated environment. However, when deploying to AWS Lambda or Azure Functions, these services will use the `requirements.txt` file to create the runtime environment. The Conda environment is not used in the cloud deployments.
