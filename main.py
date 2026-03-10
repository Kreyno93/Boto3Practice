import boto3
from ec2 import create_ec2_instance


def create_vpc_with_cidr_block():
    # Create VPC with CIDR block
    ec2 = boto3.resource("ec2")

    vpc = ec2.create_vpc(CidrBlock="10.0.0.0/24")
    print("Created VPC with ID:", vpc.id)


# Principle: Single Responsibility Principle (SRP) - Each function has a single responsibility, making the code easier to maintain and understand.


def create_subnet_in_vpc(vpc_id):
    # Create Subnet in the VPC
    ec2 = boto3.resource("ec2")

    subnet = ec2.create_subnet(VpcId=vpc_id, CidrBlock="10.0.0.0/26")
    print("Created Subnet with ID:", subnet.id)


if __name__ == "__main__":
    create_ec2_instance()
    create_vpc_with_cidr_block()
    # Assuming you have a VPC ID, you can create a subnet in it
