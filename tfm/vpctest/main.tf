# variable "region" {
#   default = "ap-northeast-1"
# }

provider "aws" {
  region                  = "ap-northeast-1"
  shared_credentials_file = "/home/ec2-user/.aws/credentials"
  profile                 = "d"
}

resource "aws_vpc" "myVPC" {
  cidr_block           = "10.1.0.0/16"
  instance_tenancy     = "default"
  enable_dns_support   = "true"
  enable_dns_hostnames = "false"
  tags = {
    Name   = "myVPC"
    system = "common"
  }
}
