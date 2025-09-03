locals {
  rg-name  = "rg-projects-container-registry"
}

resource "azurerm_resource_group" "example" {
  name     = local.rg-name
  location = var.location
}