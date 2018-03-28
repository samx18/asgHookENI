import boto3

def lambda_handler(event,context):

	ec2Client = boto3.client('ec2')
	ec2 = boto3.resource('ec2')
	# sgID = metadata.SecurityGroups
	sgID = event['SecurityGroups']
	print sgID
	# subnetID = metadata.SubnetId
	subnetID = event['SubnetId']
	print subnetID
	response = ec2Client.create_network_interface(Groups=[sgID],SubnetId=subnetID)

	# get the networkwork interface id for the eni created above

	eniID = response.get("NetworkInterface").get("NetworkInterfaceId")

	print eniID

	# attach the network interface to the instance

	network_interface = ec2.NetworkInterface(eniID)

	network_interface.attach(
	    DeviceIndex=1,
	    InstanceId='i-0233bf7c4ffd9b062',

	)
	return
