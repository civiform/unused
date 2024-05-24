provider "azurerm" {
  features {}
}

provider "aws" {
  region = var.aws_region
  access_key = data.azurerm_key_vault_secret.aws_access_key_id.value
  secret_key = data.azurerm_key_vault_secret.aws_secret_access_token.value
}
