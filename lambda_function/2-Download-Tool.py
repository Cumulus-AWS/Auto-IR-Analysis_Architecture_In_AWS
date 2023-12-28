import boto3
import os
from datetime import datetime, timedelta

def lambda_handler(event, context):
    try:
        # Initialize AWS SSM client
        ssm = boto3.client('ssm', region_name="ap-northeast-2")
        
        # Convert UTC timestamp to Korean time format
        utc_datetime = datetime.strptime(event["detail"]["createdAt"], "%Y-%m-%dT%H:%M:%S.%fZ")
        korean_datetime = utc_datetime + timedelta(hours=9)
        time = korean_datetime.strftime("%Y-%m-%d_%H:%M:%S")
        
        # Extract EC2 instance ID from CloudTrail event
        instance = event["detail"]["resource"]["instanceDetails"]["instanceId"]
        
        # Commands to install Volatility tool on the EC2 instance
        commands = [
            '#!/bin/bash',
            'mkdir -p ./tools/volatility',
            'curl -L https://github.com/volatilityfoundation/profiles/raw/master/Linux/RedHat/x86/RedHat50.zip -o ./tools/volatility/volatility.zip',
            'unzip -j ./tools/volatility/volatility.zip -d ./tools/volatility',
            'rm ./tools/volatility/volatility.zip',
            'chmod +x ./tools/volatility/vol.py'
        ]

        # Send command to EC2 instance using AWS SSM
        response = ssm.send_command(
            InstanceIds=[instance],
            DocumentName='AWS-RunShellScript',
            Parameters={
                'commands': commands,
                'executionTimeout': ['43200']  # Set execution timeout to 43200 seconds (12 hours)
            },
            Comment='create command result'
        )
        
        return {
            'statusCode': 200,
        }

    except Exception as e:
        # Print and raise an error if an exception occurs
        print(f"An error occurred: {e}")
        raise
