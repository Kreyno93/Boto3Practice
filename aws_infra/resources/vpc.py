"""VPC resource management."""


def create_vpc(ec2, cidr_block="10.0.0.0/24", name="Boto3-VPC"):
    vpc = ec2.create_vpc(
        CidrBlock=cidr_block,
        TagSpecifications=[
            {"ResourceType": "vpc", "Tags": [{"Key": "Name", "Value": name}]}
        ],
    )
    print(f"Created VPC with ID: {vpc.id}")
    return vpc.id


def delete_vpc(ec2, vpc_id):
    ec2.Vpc(vpc_id).delete()
    print(f"Deleted VPC with ID: {vpc_id}")
