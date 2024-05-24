provider "azurerm" {
  features {}
}

provider "aws" {
  region = var.aws_region
  access_key = local.aws_access_key_id
  secret_key = local.aws_secret_access_token
}
