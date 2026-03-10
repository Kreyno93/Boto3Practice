def create_vpc_with_cidr_block(ec2):
    # Create VPC with CIDR block
    vpc = ec2.create_vpc(
        CidrBlock="10.0.0.0/24",
        TagSpecifications=[
            {"ResourceType": "vpc", "Tags": [{"Key": "Name", "Value": "Boto3-VPC"}]}
        ],
    )
    print("Created VPC with ID:", vpc.id)
    return vpc.id
