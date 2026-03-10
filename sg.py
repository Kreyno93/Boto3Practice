def create_security_group_for_Webserver(ec2, vpc_id):
    security_group = ec2.create_security_group(
        GroupName="WebServerSG",
        Description="Security group for web server",
        VpcId=vpc_id,
        TagSpecifications=[
            {
                "ResourceType": "security-group",
                "Tags": [{"Key": "Name", "Value": "WebServerSG"}],
            }
        ],
    )
    security_group.authorize_ingress(
        CidrIp="0.0.0.0/0", IpProtocol="tcp", FromPort=80, ToPort=80
    )
    security_group.authorize_ingress(
        CidrIp="0.0.0.0/0", IpProtocol="tcp", FromPort=22, ToPort=22
    )
    return security_group.id
