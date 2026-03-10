def create_public_route_table(ec2, vpc_id):
    # Create a public route table
    route_table = ec2.create_route_table(
        VpcId=vpc_id,
        TagSpecifications=[
            {
                "ResourceType": "route-table",
                "Tags": [{"Key": "Name", "Value": "Boto3-PublicRouteTable"}],
            }
        ],
    )
    print("Created Route Table with ID:", route_table.id)
    return route_table.id


def associate_route_table_with_subnet(ec2, route_table_id, subnet_id):
    # Associate the route table with the subnet
    association = ec2.RouteTable(route_table_id).associate_with_subnet(
        SubnetId=subnet_id
    )
    print(f"Associated Route Table {route_table_id} with Subnet {subnet_id}")


def create_route_to_igw(ec2, route_table_id, igw_id):
    # Create a route to the Internet Gateway
    route_table = ec2.RouteTable(route_table_id)
    route_table.create_route(
        DestinationCidrBlock="0.0.0.0/0",
        GatewayId=igw_id,
    )
    print(f"Created route to Internet Gateway {igw_id} in Route Table {route_table_id}")
