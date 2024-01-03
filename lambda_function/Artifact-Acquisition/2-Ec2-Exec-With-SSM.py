import boto3
import os
import uuid
import time as system_time
import json  
from datetime import datetime, timedelta 

def lambda_handler(event, context):
    try:
        # Initialize AWS SSM client
        ssm = boto3.client('ssm', region_name="ap-northeast-2")
        
        # Convert UTC timestamp to Korean time format
        utc_datetime = datetime.strptime(event["detail"]["createdAt"],"%Y-%m-%dT%H:%M:%S.%fZ")
        korean_datetime = utc_datetime + timedelta(hours=9)
        time = korean_datetime.strftime("%Y-%m-%d_%H:%M:%S")
        
        # Extract EC2 instance ID from CloudTrail event
        instance = event["detail"]["resource"]["instanceDetails"]["instanceId"]
        
        # AWS S3 credentials for restricted access
        restricted_s3_credentials = {
            'AccessKeyId': 'your-AccessKeyID',
            'SecretAccessKey': 'your-SecretAccessKey'
        }
        
        # S3 path for uploading forensic artifacts
        s3_upload = '| aws s3 cp - s3://cumulus-forensic-artifact/{0}/{1}/command'.format(instance, time)
        
        # Shell commands to be executed on the EC2 instance
        commands1 = [
            '#!/bin/bash',
            'export AWS_ACCESS_KEY_ID={}'.format(restricted_s3_credentials['AccessKeyId']),
            'export AWS_SECRET_ACCESS_KEY={}'.format(restricted_s3_credentials['SecretAccessKey']),
            'export AWS_DEFAULT_REGION=ap-northeast-2',
            # Execute various commands and upload results to S3
            f'date {s3_upload}/date.txt',
            f'uname -a {s3_upload}/uname_output.txt',
            f'ifconfig -a || ip a {s3_upload}/ifconfig_output.txt',
            f'ps -ef {s3_upload}/ps_output.txt',
            f'netstat -anp {s3_upload}/netstat_output.txt',
            f'lsof -V {s3_upload}/lsof_output.txt',
            f'netstat -rn && route {s3_upload}/netstat_rn_route_output.txt',
            f'df && mount {s3_upload}/df_mount_output.txt',
            f'free {s3_upload}/free_output.txt',
            f'w {s3_upload}/w_output.txt',
            f'last -Faiwx {s3_upload}/last_output.txt',
            f'lsmod {s3_upload}/lsmod_output.txt',
            f'cat /etc/passwd {s3_upload}/passwd_output.txt',
            f'cat /etc/shadow {s3_upload}/shadow_output.txt',
            f'find /directory -type f -mtime -1 -print {s3_upload}/find_output.txt'
        ]

        # Send command to EC2 instance using AWS SSM
        response1 = ssm.send_command(
            InstanceIds=[instance],
            DocumentName='AWS-RunShellScript',
            Parameters={
                'commands': commands1,
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
