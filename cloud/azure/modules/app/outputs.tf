output "app_service_default_hostname" {
  value = "https://${azurerm_linux_web_app.civiform_app.name}.azurewebsites.net"
}

output "app_service_canary_hostname" {
  value = "https://${azurerm_app_service_slot.canary.default_site_hostname}"
}

output "app_service_name" {
  value = azurerm_linux_web_app.civiform_app.name
}

output "resource_group_name" {
  value = data.azurerm_resource_group.rg.name
}

output "custom_domain_verification_id" {
  value = azurerm_linux_web_app.civiform_app.custom_domain_verification_id
}