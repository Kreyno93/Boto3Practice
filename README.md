# Boto3 Practice

AWS infrastructure automation using Python and Boto3 to provision a complete VPC environment with an EC2 web server.

## Overview

This project demonstrates infrastructure as code using Boto3 to create and manage AWS resources. It provisions a complete networking stack including VPC, subnet, internet gateway, route tables, security groups, and an EC2 instance configured as a web server.

## Features

- VPC creation with custom CIDR block
- Public subnet configuration
- Internet Gateway setup and attachment
- Route table configuration for internet access
- Security group with HTTP and SSH access
- EC2 instance deployment with user data script
- Automated cleanup/teardown functionality

## Prerequisites

- Python 3.12+
- AWS account with appropriate permissions
- AWS credentials configured (via `~/.aws/credentials` or environment variables)
- SSH key pair named `vockey` in your AWS account

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd boto3Practice
```

2. Create and activate virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Update the following values in `ec2.py` if needed:
- `ImageId`: AMI ID (default: Amazon Linux 2023)
- `InstanceType`: Instance size (default: t3.small)
- `KeyName`: SSH key pair name (default: vockey)

Update CIDR blocks in `vpc.py` and `subnet.py` if custom networking is required.

## Usage

Run the main script to provision infrastructure:
```bash
python main.py
```

The script will:
1. Create a VPC with CIDR block 10.0.0.0/24
2. Create a public subnet with CIDR block 10.0.0.0/26
3. Create and attach an Internet Gateway
4. Configure route tables for internet access
5. Create a security group allowing HTTP (80) and SSH (22)
6. Launch an EC2 instance with Apache web server
7. Prompt for cleanup confirmation

## Project Structure

```
boto3Practice/
├── main.py              # Main orchestration script
├── vpc.py               # VPC creation
├── subnet.py            # Subnet creation
├── igw.py               # Internet Gateway setup
├── routeTable.py        # Route table configuration
├── sg.py                # Security group setup
├── ec2.py               # EC2 instance provisioning
├── destroy.py           # Resource cleanup
├── userdata.sh          # EC2 user data script
├── requirements.txt     # Python dependencies
└── .gitignore          # Git ignore rules
```

## Architecture

The project creates the following AWS infrastructure:

```
VPC (10.0.0.0/24)
├── Public Subnet (10.0.0.0/26)
│   └── EC2 Instance (Web Server)
│       └── Security Group (HTTP:80, SSH:22)
├── Internet Gateway
└── Route Table (0.0.0.0/0 → IGW)
```

## Security Considerations

- Security group allows SSH (port 22) from 0.0.0.0/0 - restrict this in production
- HTTP access (port 80) is open to the internet
- Ensure AWS credentials are properly secured
- Review IAM permissions before running

## Cleanup

The script includes an automated cleanup function that removes all created resources. When prompted, type `yes` to destroy all infrastructure.

To manually clean up resources, run the destroy function or delete resources via AWS Console in this order:
1. EC2 instance
2. Internet Gateway (detach first)
3. Route table associations
4. Security groups
5. Subnets
6. VPC

## License

This project is for educational purposes.

## Contributing

Contributions are welcome. Please open an issue or submit a pull request.

## Acknowledgments

Built following AWS best practices and the Single Responsibility Principle for maintainable code structure.
