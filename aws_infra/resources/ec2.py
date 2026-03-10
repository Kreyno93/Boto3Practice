"""EC2 instance resource management."""


def create_instance(ec2, subnet_id, sg_id, ami_id, instance_type="t3.small", key_name="vockey", userdata_file="userdata.sh"):
    with open(userdata_file, "r") as f:
        userdata = f.read()
    
    response = ec2.create_instances(
        ImageId=ami_id,
        MinCount=1,
        MaxCount=1,
        InstanceType=instance_type,
        KeyName=key_name,
        UserData=userdata,
        NetworkInterfaces=[
            {
                "SubnetId": subnet_id,
                "DeviceIndex": 0,
                "AssociatePublicIpAddress": True,
                "Groups": [sg_id],
            }
        ],
        TagSpecifications=[
            {
                "ResourceType": "instance",
                "Tags": [
                    {"Key": "Name", "Value": "WebServer"},
                    {"Key": "Environment", "Value": "Production"},
                ],
            }
        ],
    )
    print(f"Launched EC2 instance with ID: {response[0].id}")
    return response[0].id


def terminate_instance(ec2, instance_id):
    ec2.Instance(instance_id).terminate()
    print(f"Terminated EC2 instance with ID: {instance_id}")
