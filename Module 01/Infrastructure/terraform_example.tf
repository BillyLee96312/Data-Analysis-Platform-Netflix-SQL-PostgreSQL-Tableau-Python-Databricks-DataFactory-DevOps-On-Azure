// Terraform skeleton ? Module 01: Basic infra
// Note: This is a simplified example for lab/discussion purposes. Use secure state/backends for real deployments.

provider "azurerm" {
  features {}
}

variable "resource_group_name" {
  default = "rg-netflix-student-sprint1"
}

variable "location"{
  default = "eastus"
}

resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
  tags = {
    owner = "student"
    sprint = "sprint1"
  }
}

resource "azurerm_storage_account" "st" {
  name                     = "stnetflixexample" // Replace with your unique storage name
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  is_hns_enabled           = true
}

resource "azurerm_key_vault" "kv" {
  name                        = "kv-netflix-example"
  location                    = azurerm_resource_group.rg.location
  resource_group_name         = azurerm_resource_group.rg.name
  tenant_id                   = "<TENANT_ID>"
  sku_name                    = "standard"
}

// Placeholder: Add Databricks and PostgreSQL resources as modules or resources.

output "resource_group_name" {
  value = azurerm_resource_group.rg.name
}

// Usage: terraform init; terraform apply -var "resource_group_name=rg-netflix-{studentid}-sprint1" -auto-approve
