#!/bin/bash

source lambda_setup_deployment.sh

echo "Updating function...."
aws lambda update-function-code \
--function-name $function_name \
--zip-file fileb://~/$temporary_dir/$function_name.zip
echo "Function has been updated."

echo "Change directory back to project root"
cd $project_root