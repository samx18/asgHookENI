import boto3
import json

def lambda_handler(event,context):
	print event
	# print json.loads(event)
	# message = event['Records'][0]['Sns']['Message']
	message = json.loads(event['Records'][0]['Sns']['Message'])
	print message
	# metadata=json.loads(message.NotificationMetadata)
	metadata = json.loads(message['NotificationMetadata'])
	print metadata
	
	instanceId = message['EC2InstanceId'];
	ec2Client = boto3.client('ec2')
	ec2 = boto3.resource('ec2')
	sgID = metadata['SecurityGroups']
	#sgID = event['SecurityGroups']
	print sgID
	subnetID = metadata['SubnetId']
	#subnetID = event['SubnetId']
	print subnetID
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
	return eniID #optional
