def create_ec2_instance(ec2, subnet_id, sg_id, ami_id):
    # Launch Ec2 instance

    response = ec2.create_instances(
        ImageId="ami-0c4d678ed3b5d3259",  # AL2023
        MinCount=1,
        MaxCount=1,
        InstanceType="t3.small",
        KeyName="vockey",  # vockey aka labsuser.pem
        UserData=open("userdata.sh", "r").read(),
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
    print("Launched EC2 instance with ID:", response[0].id)
    return response[0].id
