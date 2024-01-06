import boto3
import os
import uuid
import time as system_time
import json  
from datetime import datetime, timedelta 

def lambda_handler(event, context):
    
    ssm = boto3.client('ssm', region_name="ap-northeast-2")
        
    utc_datetime = datetime.strptime(event["detail"]["updatedAt"],"%Y-%m-%dT%H:%M:%S.%fZ")
    korean_datetime = utc_datetime + timedelta(hours=9)
    time = korean_datetime.strftime("%Y-%m-%d_%H:%M:%S")
        
        
    instance = event["detail"]["resource"]["instanceDetails"]["instanceId"]
    Analysis_instance = 'your-Analysis-EC2-ID'
    
    restricted_s3_credentials = {
        'AccessKeyId': 'your-AccessKeyID',
        'SecretAccessKey': 'your-SecretAccessKey'
    }
    
    commands1 = [
        '#!/bin/bash',
        'export AWS_ACCESS_KEY_ID={}'.format(restricted_s3_credentials['AccessKeyId']),
        'export AWS_SECRET_ACCESS_KEY={}'.format(restricted_s3_credentials['SecretAccessKey']),
        'export AWS_DEFAULT_REGION=ap-northeast-2',
        'sudo xfs_repair -L /dev/xvdb1',
        'sudo xfs_admin -U generate /dev/xvdb1',
        'sudo mount -r /dev/xvdb1 /data',
        f'python3 /home/ec2-user/volatility3/analysis_software.py {instance} {time}',
        'sudo umount /dev/xvdb1'
    ]
    
    response1 = ssm.send_command(
        InstanceIds=[Analysis_instance],
        DocumentName='AWS-RunShellScript',
        Parameters={
            'commands': commands1,
            'executionTimeout': ['3200']
        },
        Comment='creat command result'
    )
    
    return {
        'statusCode': 200
    }
