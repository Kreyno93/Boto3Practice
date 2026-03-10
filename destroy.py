def destroy_everything(
    ec2, instance_id, vpc_id, subnet_id, igw_id, route_table_id, sg_id
):
    # ask the user if they want to destroy everything
    user_input = input("Are you sure you want to destroy everything? (yes/no): ")
    if user_input.lower() != "yes":
        print("Operation cancelled.")
        return
    print("Destroying everything...")
    # Terminate EC2 instance
    ec2.Instance(instance_id).terminate()
    print(f"Terminated EC2 instance with ID: {instance_id}")
    # Detach Internet Gateway from VPC
    ec2.InternetGateway(igw_id).detach_from_vpc(VpcId=vpc_id)
    print(f"Detached Internet Gateway {igw_id} from VPC {vpc_id}")
    # Delete Internet Gateway
    ec2.InternetGateway(igw_id).delete()
    print(f"Deleted Internet Gateway with ID: {igw_id}")
    # Disassociate Route Table from Subnet
    ec2.RouteTable(route_table_id).disassociate_from_subnet(AssociationId=subnet_id)
    print(f"Disassociated Route Table {route_table_id} from Subnet {subnet_id}")
    # Delete Route Table
    ec2.RouteTable(route_table_id).delete()
    print(f"Deleted Route Table with ID: {route_table_id}")
    # Delete Security Group
    ec2.SecurityGroup(sg_id).delete()
    print(f"Deleted Security Group with ID: {sg_id}")
    # Delete Subnet
    ec2.Subnet(subnet_id).delete()
    print(f"Deleted Subnet with ID: {subnet_id}")
    # Delete VPC
    ec2.Vpc(vpc_id).delete()
    print(f"Deleted VPC with ID: {vpc_id}")
