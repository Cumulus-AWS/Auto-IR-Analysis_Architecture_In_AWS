import boto3
import os
import uuid
import time as system_time
import json
from datetime import datetime, timedelta

def lambda_handler(event, context):
    try:
        # Initialize AWS SSM and S3 clients
        ssm = boto3.client('ssm', region_name="ap-northeast-2")
        s3 = boto3.client('s3')

        # Convert UTC timestamp to Korean time format
        utc_datetime = datetime.strptime(event["detail"]["createdAt"], "%Y-%m-%dT%H:%M:%S.%fZ")
        korean_datetime = utc_datetime + timedelta(hours=9)
        time = korean_datetime.strftime("%Y-%m-%d_%H:%M:%S")

        # Extract EC2 instance ID and create S3 prefix
        instance = event["detail"]["resource"]["instanceDetails"]["instanceId"]
        s3_prefix = "{0}/{1}/memory/".format(instance, time)

        # AWS S3 credentials for restricted access
        restricted_s3_credentials = {
            'AccessKeyId': 'your-AccessKey-ID',
            'SecretAccessKey': 'your-SecretAccessKey-ID'
        }

        sizetag = '--metadata OriginalSize=$MEMSIZE'
        acl = '--acl bucket-owner-full-control'

        # S3 command to upload LiME memory dump
        s3_upload_command = f"aws s3 cp - s3://cumulus-forensic-artifact/{s3_prefix}{instance}.lime"

        # Commands to be executed on the EC2 instance for inserting LiME module
        commands1 = [
            '#!/bin/bash',
            # Install AWS CLI if not present
            'osname=$(cat /etc/os-release | grep PRETTY | cut -d \\" -f 2 | sed "s/ /_/g")',
            'if [ -e /usr/bin/yum ]; then',
            '  if [ $(rpm -qa | grep awscli | wc -l) -eq 0 ]; then yum -y install unzip && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip && ./aws/install; fi',
            'else',
            '  if [ $(dpkg -l | grep awscli | wc -l) -eq 0 ]; then DEBIAN_FRONTEND=noninteractive apt-get -y install unzip && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip && ./aws/install; fi',
            'fi',
            'if [ $(rpm -qa | grep awscli | wc -l) -eq 0 ]; then yum -y install unzip && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip && ./aws/install; fi',
            # Download and insert LiME module
            'aws s3 cp s3://cumulus-sec-data/memory-modules/lime-5.10.199-190.747.amzn2.x86_64.ko /tmp/lime.ko',
            'if [ $(lsmod | grep lime | wc -l) -gt 0 ]; then rmmod lime; fi',
            'sudo insmod /tmp/lime-5.10.199-190.747.amzn2.x86_64.ko "path=tcp:4444 format=lime localhostonly=1"'
        ]

        # Commands to be executed on the EC2 instance for dumping memory to S3
        commands2 = [
            '#!/bin/bash',
            'sleep 10',
            # Set environment variables and configure AWS CLI
            'export MEMSIZE=$(awk \'/MemTotal/ {print $2/1024/1024}\' /proc/meminfo)',
            'export AWS_ACCESS_KEY_ID={}'.format(restricted_s3_credentials['AccessKeyId']),
            'export AWS_SECRET_ACCESS_KEY={}'.format(restricted_s3_credentials['SecretAccessKey']),
            'export AWS_DEFAULT_REGION=ap-northeast-2',
            'aws configure set default.s3.max_concurrent_requests 20',
            # Stream memory dump to S3
            "cat < /dev/tcp/127.0.0.1/4444 | {0}".format(s3_upload_command),
            'rmmod lime.ko'
        ]

        # Send the first set of commands to insert LiME module
        response1 = ssm.send_command(
            InstanceIds=[instance],
            DocumentName='AWS-RunShellScript',
            Parameters={
                'commands': commands1,
                'executionTimeout': ['43200']
            },
            Comment='Insert LiME'
        )

        # Sleep for 30 seconds before sending the second set of commands
        system_time.sleep(30)

        # Send the second set of commands to dump memory to S3
        response2 = ssm.send_command(
            InstanceIds=[instance],
            DocumentName='AWS-RunShellScript',
            Parameters={
                'commands': commands2,
                'executionTimeout': ['43200']
            },
            Comment='Dump to S3'
        )

        # Prepare output and S3 export information
        output = {
            instance: [response1['Command']['CommandId'], response2['Command']['CommandId']]
        }

        s3_export = {
            'ArtifactRoot': f's3://cumulus-forensic-artifact/{s3_prefix}',
            'S3URL': f'{instance}.raw'
        }

        return {
            "Output": output,
            "S3": s3_export
        }

    except Exception as e:
        print(f"An error occurred: {e}")
        raise
