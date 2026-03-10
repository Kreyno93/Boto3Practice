def create_subnet_in_vpc(ec2, vpc_id):
    # Create Subnet in the VPC
    subnet = ec2.create_subnet(
        VpcId=vpc_id,
        CidrBlock="10.0.0.0/26",
        TagSpecifications=[
            {
                "ResourceType": "subnet",
                "Tags": [{"Key": "Name", "Value": "Boto3-PublicSubnet"}],
            }
        ],
    )
    print("Created Subnet with ID:", subnet.id)
    return subnet.id
