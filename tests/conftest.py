import os
import sys

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../lambda_handler"))
)

# env variables
os.environ["AWS_REGION_NAME"] = "us-east-1"
os.environ["AWS_SAM_STACK_NAME"] = "flask-sam-app"
