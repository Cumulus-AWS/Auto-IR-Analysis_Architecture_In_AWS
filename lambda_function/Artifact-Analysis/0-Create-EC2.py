import boto3
from datetime import datetime, timedelta
import time

def lambda_handler(event, context):
    
    instance = event["detail"]["resource"]["instanceDetails"]["instanceId"]
    
    IR_instance = 'your-instance-ID'
    
    utc_datetime = datetime.strptime(event["detail"]["createdAt"], "%Y-%m-%dT%H:%M:%S.%fZ")
    korean_datetime = utc_datetime + timedelta(hours=9)
    time = korean_datetime.strftime("%Y%m%d%H%M%S")
    
    ami_name = f'{instance}_ami_{time}'
    
    #ami_id 추출
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_images(Filters=[{'Name': 'name', 'Values': [ami_name]}])
    
    if 'Images' in response and response['Images']:
        ami_id = response['Images'][0]['ImageId']
    else:
        raise Exception(f"AMI with name '{ami_name}' not found.")
    
    response = ec2_client.describe_images(ImageIds=[ami_id])
    block_device_mappings = response['Images'][0]['BlockDeviceMappings']
    
    #snapshot_id 추출
    ebs_snapshot_ids = []
    for mapping in block_device_mappings:
        if 'Ebs' in mapping and 'SnapshotId' in mapping['Ebs']:
            ebs_snapshot_ids.append(mapping['Ebs']['SnapshotId'])
    
    #volume 생성
    new_volume_ids = []
    for snapshot_id in ebs_snapshot_ids:
                
        waiter = ec2_client.get_waiter('snapshot_completed')
        waiter.wait(SnapshotIds=[snapshot_id], WaiterConfig={'Delay': 10, 'MaxAttempts': 25})
        
        response = ec2_client.create_volume(SnapshotId=snapshot_id, AvailabilityZone='ap-northeast-2a')
        new_volume_id = response['VolumeId']
        new_volume_ids.append(new_volume_id)
        
        waiter = ec2_client.get_waiter('volume_available')
        waiter.wait(VolumeIds=[new_volume_id], WaiterConfig={'Delay': 10, 'MaxAttempts': 25})
            
    #volume 연결 
    index = 98
    for volume_id in new_volume_ids:
        
        device_name = f'/dev/xvd{chr(index)}'
        response_attach = ec2_client.attach_volume(
            VolumeId=volume_id,
            InstanceId=IR_instance,
            Device=device_name
        )
        index = index + 1
    
    return {
        'statusCode': 200,
    }
