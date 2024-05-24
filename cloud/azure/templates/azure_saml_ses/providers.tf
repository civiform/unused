provider "azurerm" {
  features {}
}

provider "aws" {
  region = var.aws_region
  access_key = var.aws-access-key-id
  secret_key = var.aws-secret-access-token
}
