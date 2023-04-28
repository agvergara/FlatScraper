# FlatScraper
Multiple Lambdas to perform web-scraping from the primary flat listing pages

## Requirements

1. Docker
1. Node.js, NPM
1. Python >= 3.7

## Setting up local environment:
1. Run `npm install` to install the serverless framework
1. Download your CHROMEDRIVER from https://chromedriver.chromium.org/downloads and add to the project root folder
1. Set CHROMIUM_PATH and CHROMEDRIVER_PATH in `/src/settings.py`
1. Run `python -m venv venv` to initiate a python virtual environment
1. Run `source ./venv/bin/activate` to activate the virtual enviroment
1. Run `pip install -r requirements.txt` to install the production dependencies
1. Run `pip install -r requirements-dev.txt` to install the development dependencies

## Deploy using Serverless
1. Run `serverless --org={YOUR_ORG}`
1. Deployment should be automatically done first time you're creating the app
1. For future deployments use `sls deploy`
1. Remember to add your AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY for AWS

## What does it do in AWS?
1. First it will create a AWS Cloudformation template and deploy the image to the Elastic Container Registry (ECR) in AWS
1. Then it will create the Lambda function in AWS (REMEMBER TO CHECK THE REGION!)
1. From now on, you can play with the function through the serverless dashboard or invoke it from the AWS CLI