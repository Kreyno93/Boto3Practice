import boto3
from ec2 import create_ec2_instance
from sg import create_security_group_for_Webserver
from vpc import create_vpc_with_cidr_block
from subnet import create_subnet_in_vpc
from igw import create_igw, attach_igw_to_vpc
from routeTable import (
    create_public_route_table,
    associate_route_table_with_subnet,
    create_route_to_igw,
)
from destroy import destroy_everything
from ami import get_latest_amazon_linux_2023_ami_id

# Principle: Single Responsibility Principle (SRP) - Each function has a single responsibility, making the code easier to maintain and understand.

ec2 = boto3.resource("ec2")

if __name__ == "__main__":
    vpc_id = create_vpc_with_cidr_block(ec2)
    subnet_id = create_subnet_in_vpc(ec2, vpc_id)
    route_table_id = create_public_route_table(ec2, vpc_id)
    associate_route_table_with_subnet(ec2, route_table_id, subnet_id)
    igw_id = create_igw(ec2, vpc_id)
    attach_igw_to_vpc(ec2, igw_id, vpc_id)
    create_route_to_igw(ec2, route_table_id, igw_id)
    sg_id = create_security_group_for_Webserver(ec2, vpc_id)
    ami_id = get_latest_amazon_linux_2023_ami_id(
        boto3.client("ssm"), boto3.Session().region_name
    )
    instance_id = create_ec2_instance(ec2, subnet_id, sg_id, ami_id)
    destroy_everything(
        ec2, instance_id, vpc_id, subnet_id, igw_id, route_table_id, sg_id
    )
