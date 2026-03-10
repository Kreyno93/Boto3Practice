"""Internet Gateway resource management."""


def create_igw(ec2, name="Boto3-IGW"):
    igw = ec2.create_internet_gateway(
        TagSpecifications=[
            {"ResourceType": "internet-gateway", "Tags": [{"Key": "Name", "Value": name}]}
        ]
    )
    print(f"Created Internet Gateway with ID: {igw.id}")
    return igw.id


def attach_igw(ec2, igw_id, vpc_id):
    ec2.InternetGateway(igw_id).attach_to_vpc(VpcId=vpc_id)
    print(f"Attached Internet Gateway {igw_id} to VPC {vpc_id}")


def detach_igw(ec2, igw_id, vpc_id):
    ec2.InternetGateway(igw_id).detach_from_vpc(VpcId=vpc_id)
    print(f"Detached Internet Gateway {igw_id} from VPC {vpc_id}")


def delete_igw(ec2, igw_id):
    ec2.InternetGateway(igw_id).delete()
    print(f"Deleted Internet Gateway with ID: {igw_id}")
