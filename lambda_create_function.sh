#!/bin/bash

source lambda_setup_deployment.sh

echo "Creating function...."
aws lambda create-function \
--function-name $function_name \
--runtime python3.7 \
--handler $module_name.lambda_handler \
--role $aws_role \
--zip-file fileb://~/$temporary_dir/$function_name.zip
echo "Function has been created."

echo "Change directory back to project root"
cd $project_root