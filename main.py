# Copyright 2018 Sam Palani under MIT License https://opensource.org/licenses/MIT


import boto3
import json

def lambda_handler(event,context):
	print event
	# Debug -- print json.loads(event)
	
	# Parse message portion from the event
	
	message = json.loads(event['Records'][0]['Sns']['Message'])
	# Debug --  print message
	
	# Parse the metadata portion from the event - Metadata is sent from the lifecyclehook

	metadata = json.loads(message['NotificationMetadata'])
	# Debug -- print metadata
	
	instanceId = message['EC2InstanceId'];
	
	# Get a EC2 client and a EC2 Resource 	
	ec2Client = boto3.client('ec2')
	ec2 = boto3.resource('ec2')
	
	sgID = metadata['SecurityGroups']
	subnetID = metadata['SubnetId']
	response = ec2Client.create_network_interface(Groups=[sgID],SubnetId=subnetID)

	# get the networkwork interface id for the eni created above

	eniID = response.get("NetworkInterface").get("NetworkInterfaceId")

	print eniID

	# attach the network interface to the instance

	network_interface = ec2.NetworkInterface(eniID)

	network_interface.attach(
	    DeviceIndex=1,
	    InstanceId=instanceId,

	)
	return eniID #optional for debugging
