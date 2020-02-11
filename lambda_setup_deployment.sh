#!/bin/bash

project_root=$(pwd)
module_name="handler"
function_name="lambda-$module_name"
temporary_dir="Downloads"
aws_role="arn:aws:iam::"
current_path=$(pwd)

echo $project_root
echo $module_name
echo $function_name
echo $archive_path
echo $aws_role


echo "Make a temporary directory and move to it."
mkdir ~/$temporary_dir/$function_name
cd ~/$temporary_dir/$function_name

echo "Copy any Python files from project to temp directory."
cp $project_root/*.py .

echo "Pip install requirments into temp directory."
pip3 install -r $project_root/requiremtns.txt --target .

echo "Creating archive for AWS deployment."
zip -r ../$function_name.zip .

echo "Do some garbage cleanup by removing temp directory."
cd ../
rm -rf $function_name

