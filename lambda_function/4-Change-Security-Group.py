import boto3
import json

# Lambda function to modify security group of an EC2 instance for isolation

def lambda_handler(event, context):
    # Initialize EC2 client
    ec2_client = boto3.client('ec2', region_name='ap-northeast-2')
    
    # Extract instance ID and target security group ID from the CloudWatch event
    instance_id = event["detail"]["resource"]["instanceDetails"]["instanceId"]
    security_group_id = 'your-SG-ID'  # Replace with the desired security group ID
    
    # Modify the security group of the specified EC2 instance
    response = ec2_client.modify_instance_attribute(
        InstanceId=instance_id,
        Groups=[security_group_id]
    )
    
    # Return success message
    return "Success"
