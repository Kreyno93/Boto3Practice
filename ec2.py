def create_ec2_instance():
    # Launch Ec2 instance
    ec2 = boto3.resource("ec2")

    response = ec2.create_instances(
        ImageId="ami-0c4d678ed3b5d3259",  # AL2023
        MinCount=1,
        MaxCount=1,
        InstanceType="t3.small",
        KeyName="vockey",  # vockey aka labsuser.pem
    )
    print("Launched EC2 instance with ID:", response[0].id)
