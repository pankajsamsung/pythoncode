#! /usr/bin/env python3
## Monitor and Unmonitor Instances

#The example below shows how to:

# Enable detailed monitoring for a running instance using monitor_instances.
# Disable detailed monitoring for a running instance using unmonitor_instances.
# 
import boto3
import sys
from botocore.exceptions import ClientError

INSTANCE_ID = 'i-0c3fa418d3e5199f3'
ec2_client = boto3.client('ec2')
if sys.argv[1] == 'ON':
    response = ec2_client.monitor_instances(InstanceIds=[INSTANCE_ID])
    
else:
    response = ec2_client.unmonitor_instances(InstanceIds=[INSTANCE_ID])
    
print(response)