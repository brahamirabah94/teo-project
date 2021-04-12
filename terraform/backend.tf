terraform {
  backend "azurerm" {
    resource_group_name   = "${var.backend-rg}"
    storage_account_name  = "${var.storage-account-name}"
    container_name        = "${var.container-name}"
    key                   = "${var.backend-name}"
  }
}
