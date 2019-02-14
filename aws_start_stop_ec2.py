# Author: 
# Description:

#! /usr/bin/env python3
## To start and Stop an instance

import boto3
import sys
from botocore.exceptions import ClientError

instance_id = str (sys.argv[2])
action = sys.argv[1].upper()

ec2_client = boto3.client('ec2')

if action == 'ON':
    ## Dry Run to test ec2 start permission
    """
    try:
        ec2_client.start_instances(InstanceIds=[instance_id], DryRun=True)
        
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    """        
    ## Actual run
    try:
        response = ec2_client.start_instances(InstanceIds=[instance_id], DryRun=False)
        print(response)
        
    except ClientError as e:
        print(e)
else:
    ## Dry run to test permission for ec2 stop
    """
    try:
        ec2_client.stop_instances(InstanceIds=[instance_id], DryRun=True)
    
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    """        
    ## Actual run to stop instance
    try:
        response = ec2_client.stop_instances(InstanceIds=[instance_id], DryRun=False)
        print(response)
        
    except ClientError as e:
        print(e)
    