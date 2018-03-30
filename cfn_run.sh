#!/usr/bin/env bash

#bucket is where SAM uploads the code (zipped) and manages it
bucket_name=$1
if [ ! -z "$bucket_name" ]; then
	stack_name=sam-custom-resource-lambda-stack
    aws cloudformation package --template-file template.yaml --output-template-file serverless-output.yaml --s3-bucket $bucket_name
    aws cloudformation deploy --template-file serverless-output.yaml  --stack-name $stack_name --capabilities CAPABILITY_NAMED_IAM
else
    echo "Bucket name is a required parameter. Try by running the command in the below format"
    echo "sh cfn_run.sh {bucket_name}"
	exit 1
fi