"""Configuration management."""

# VPC Configuration
VPC_CIDR = "10.0.0.0/24"
VPC_NAME = "Boto3-VPC"

# Subnet Configuration
SUBNET_CIDR = "10.0.0.0/26"
SUBNET_NAME = "Boto3-PublicSubnet"

# Internet Gateway Configuration
IGW_NAME = "Boto3-IGW"

# Route Table Configuration
ROUTE_TABLE_NAME = "Boto3-PublicRouteTable"
INTERNET_ROUTE = "0.0.0.0/0"

# Security Group Configuration
SG_NAME = "WebServerSG"
SG_DESCRIPTION = "Security group for web server"

# EC2 Configuration
INSTANCE_TYPE = "t3.small"
KEY_NAME = "vockey"
USERDATA_FILE = "userdata.sh"
INSTANCE_NAME = "WebServer"
