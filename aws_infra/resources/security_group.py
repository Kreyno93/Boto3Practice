"""Security Group resource management."""


def create_security_group(ec2, vpc_id, name="WebServerSG", description="Security group for web server"):
    sg = ec2.create_security_group(
        GroupName=name,
        Description=description,
        VpcId=vpc_id,
        TagSpecifications=[
            {"ResourceType": "security-group", "Tags": [{"Key": "Name", "Value": name}]}
        ],
    )
    sg.authorize_ingress(CidrIp="0.0.0.0/0", IpProtocol="tcp", FromPort=80, ToPort=80)
    sg.authorize_ingress(CidrIp="0.0.0.0/0", IpProtocol="tcp", FromPort=22, ToPort=22)
    print(f"Created Security Group with ID: {sg.id}")
    return sg.id


def delete_security_group(ec2, sg_id):
    ec2.SecurityGroup(sg_id).delete()
    print(f"Deleted Security Group with ID: {sg_id}")
