"""Subnet resource management."""


def create_subnet(ec2, vpc_id, cidr_block="10.0.0.0/26", name="Boto3-PublicSubnet"):
    subnet = ec2.create_subnet(
        VpcId=vpc_id,
        CidrBlock=cidr_block,
        TagSpecifications=[
            {"ResourceType": "subnet", "Tags": [{"Key": "Name", "Value": name}]}
        ],
    )
    print(f"Created Subnet with ID: {subnet.id}")
    return subnet.id


def delete_subnet(ec2, subnet_id):
    ec2.Subnet(subnet_id).delete()
    print(f"Deleted Subnet with ID: {subnet_id}")
