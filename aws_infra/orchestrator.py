"""Infrastructure orchestration."""

import boto3
from aws_infra.resources.vpc import create_vpc, delete_vpc
from aws_infra.resources.subnet import create_subnet, delete_subnet
from aws_infra.resources.igw import create_igw, attach_igw, detach_igw, delete_igw
from aws_infra.resources.route_table import (
    create_route_table,
    associate_route_table,
    create_route,
    delete_route_table,
)
from aws_infra.resources.security_group import create_security_group, delete_security_group
from aws_infra.resources.ec2 import create_instance, terminate_instance
from aws_infra.utils.ami import get_latest_amazon_linux_2023_ami
from aws_infra.config import *


class InfrastructureManager:
    def __init__(self):
        self.ec2 = boto3.resource("ec2")
        self.ssm = boto3.client("ssm")
        self.session = boto3.Session()
        self.region = self.session.region_name
        self.resources = {}

    def provision(self):
        print("Starting infrastructure provisioning...")
        
        self.resources["vpc_id"] = create_vpc(self.ec2, VPC_CIDR, VPC_NAME)
        self.resources["subnet_id"] = create_subnet(self.ec2, self.resources["vpc_id"], SUBNET_CIDR, SUBNET_NAME)
        self.resources["route_table_id"] = create_route_table(self.ec2, self.resources["vpc_id"], ROUTE_TABLE_NAME)
        associate_route_table(self.ec2, self.resources["route_table_id"], self.resources["subnet_id"])
        self.resources["igw_id"] = create_igw(self.ec2, IGW_NAME)
        attach_igw(self.ec2, self.resources["igw_id"], self.resources["vpc_id"])
        create_route(self.ec2, self.resources["route_table_id"], INTERNET_ROUTE, self.resources["igw_id"])
        self.resources["sg_id"] = create_security_group(self.ec2, self.resources["vpc_id"], SG_NAME, SG_DESCRIPTION)
        ami_id = get_latest_amazon_linux_2023_ami(self.ssm, self.region)
        self.resources["instance_id"] = create_instance(
            self.ec2, self.resources["subnet_id"], self.resources["sg_id"], ami_id, INSTANCE_TYPE, KEY_NAME, USERDATA_FILE
        )
        
        print("\nInfrastructure provisioning complete!")
        return self.resources

    def destroy(self):
        user_input = input("\nAre you sure you want to destroy everything? (yes/no): ")
        if user_input.lower() != "yes":
            print("Operation cancelled.")
            return
        
        print("Destroying infrastructure...")
        
        terminate_instance(self.ec2, self.resources["instance_id"])
        detach_igw(self.ec2, self.resources["igw_id"], self.resources["vpc_id"])
        delete_igw(self.ec2, self.resources["igw_id"])
        delete_route_table(self.ec2, self.resources["route_table_id"])
        delete_security_group(self.ec2, self.resources["sg_id"])
        delete_subnet(self.ec2, self.resources["subnet_id"])
        delete_vpc(self.ec2, self.resources["vpc_id"])
        
        print("Infrastructure destroyed successfully!")
