import boto3
import json


def extarct_volume_id(arn):
    a = arn.split(':')
    b = a[-1].split('/')[-1]
    return b


def lambda_handler(event, context):
    print(event)
    volume_id = event['resources'][0]
    volume_name = extarct_volume_id(volume_id)
    ebs = boto3.client('ec2')

    response_check = ebs.describe_volumes(
        VolumeIds=[
            volume_name]
    )
    print(response_check)
    filtered_volumes = []
    for volume in response_check['Volumes']:
        volume_type = volume['VolumeType']
        if volume_type == 'gp3':
            print("No Modifications required")
        else:
            response = ebs.modify_volume(
                VolumeId=volume_name,
                VolumeType='gp3'
            )
            print("modification done changed to gp3")
