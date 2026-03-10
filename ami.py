def get_latest_amazon_linux_2023_ami_id(ssm, region):

    parameter = ssm.get_parameter(
        Name="/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64"
    )
    ami_id = parameter["Parameter"]["Value"]
    print(f"Latest Amazon Linux 2023 AMI ID in {region}: {ami_id}")
    return ami_id
