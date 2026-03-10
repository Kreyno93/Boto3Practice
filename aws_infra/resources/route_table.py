"""Route Table resource management."""


def create_route_table(ec2, vpc_id, name="Boto3-PublicRouteTable"):
    route_table = ec2.create_route_table(
        VpcId=vpc_id,
        TagSpecifications=[
            {"ResourceType": "route-table", "Tags": [{"Key": "Name", "Value": name}]}
        ],
    )
    print(f"Created Route Table with ID: {route_table.id}")
    return route_table.id


def associate_route_table(ec2, route_table_id, subnet_id):
    ec2.RouteTable(route_table_id).associate_with_subnet(SubnetId=subnet_id)
    print(f"Associated Route Table {route_table_id} with Subnet {subnet_id}")


def create_route(ec2, route_table_id, destination_cidr, gateway_id):
    ec2.RouteTable(route_table_id).create_route(
        DestinationCidrBlock=destination_cidr, GatewayId=gateway_id
    )
    print(f"Created route to {gateway_id} in Route Table {route_table_id}")


def delete_route_table(ec2, route_table_id):
    ec2.RouteTable(route_table_id).delete()
    print(f"Deleted Route Table with ID: {route_table_id}")
