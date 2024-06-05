# Configure the Azure provider
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  backend "azurerm" {}
  required_version = ">= 0.14.9"
}