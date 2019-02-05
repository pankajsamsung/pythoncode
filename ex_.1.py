# Author: PK    
# Description: Describe aws instances

#! /usr/bin/env python

import boto3
ec2obj = boto3.client('ec2')
response = ec2obj.describe_instances()
print (response)


