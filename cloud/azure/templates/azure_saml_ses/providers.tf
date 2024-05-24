provider "azurerm" {
  features {}
}

provider "aws" {
  region = var.aws_region
  access_key = locals.aws-access-key-id
  secret_key = locals.aws-secret-access-token
}
