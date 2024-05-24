provider "azurerm" {
  features {}
}

provider "aws" {
  region = var.aws_region
  access_key = locals.aws_access_key_id
  secret_key = locals.aws_secret_access_token
}
