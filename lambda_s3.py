import json
import boto3

def lambda_handler(event, context):
    ssm = boto3.client('ssm')
    s3 = boto3.client('s3')
    
    # Retrieve SSM Parameter
    parameter = ssm.get_parameter(Name='UserName')
    parameter_value = parameter['Parameter']['Value']
    
    # Define S3 bucket and file name
    bucket_name = 'my-exercise-bucket-dxc-12345'
    file_name = 'parameter_store_value.txt'
    
    # Store the parameter value into the file in S3 bucket
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=parameter_value)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully retrieved SSM parameter and stored it in S3')
    }
