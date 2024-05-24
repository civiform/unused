data "azurerm_key_vault_secret" "aws_secret_access_token" {
  name         = local.aws_secret_access_token
  key_vault_id = data.azurerm_key_vault.civiform_key_vault.id
}

data "azurerm_key_vault_secret" "aws_access_key_id" {
  name         = local.aws_access_key_id
  key_vault_id = data.azurerm_key_vault.civiform_key_vault.id
}
