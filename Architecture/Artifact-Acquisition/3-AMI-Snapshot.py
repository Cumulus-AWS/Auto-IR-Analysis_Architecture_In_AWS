import boto3
import os
import uuid
import time as system_time
from datetime import datetime, timedelta 

def lambda_handler(event, context):
    try:
        # Initialize EC2 client
        ec2_client = boto3.client('ec2')

        # Convert UTC timestamp to Korean time format
        utc_datetime = datetime.strptime(event["detail"]["createdAt"],"%Y-%m-%dT%H:%M:%S.%fZ")
        korean_datetime = utc_datetime + timedelta(hours=9)
        time = korean_datetime.strftime("%Y%m%d%H%M%S")
        
        # Extract EC2 instance ID from CloudWatch event
        instance = event["detail"]["resource"]["instanceDetails"]["instanceId"]
        
        # Create an Amazon Machine Image (AMI) for the EC2 instance
        response = ec2_client.create_image(
            InstanceId=instance,
            Name=f'{instance}_ami_{time}',
            NoReboot=True  # Do not reboot the instance before creating the AMI
        )

        return {    
            'statusCode': 200,
        }

    except Exception as e:
        # Print and raise an error if an exception occurs
        print(f"An error occurred: {e}")
        raise
