def create_igw(ec2, vpc_id):
    # Create Internet Gateway
    igw = ec2.create_internet_gateway(
        TagSpecifications=[
            {
                "ResourceType": "internet-gateway",
                "Tags": [{"Key": "Name", "Value": "Boto3-IGW"}],
            }
        ]
    )
    print("Created Internet Gateway with ID:", igw.id)
    return igw.id


def attach_igw_to_vpc(ec2, igw_id, vpc_id):
    # Attach Internet Gateway to VPC
    igw = ec2.InternetGateway(igw_id)
    igw.attach_to_vpc(VpcId=vpc_id)
    print(f"Attached Internet Gateway {igw_id} to VPC {vpc_id}")
