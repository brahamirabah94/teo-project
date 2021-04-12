resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}
# donner droit a notre cluster de pull des images
# resource "azurerm_role_assignment" "role_acrpull" {
#   scope                            = azurerm_container_registry.acr.id
#   role_definition_name             = "AcrPull"
#   principal_id                     = azurerm_kubernetes_cluster.aks.kubelet_identity.0.object_id
#   skip_service_principal_aad_check = true
# }
#
# resource "azurerm_container_registry" "acr" {
#   name                = var.acr_name
#   resource_group_name = azurerm_resource_group.rg.name
#   location            = var.location
#   sku                 = "Basic"
#   admin_enabled       = false
# }

resource "azurerm_kubernetes_cluster" "aks" {
  name                = var.cluster_name
  kubernetes_version  = var.kubernetes_version
  location            = var.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = var.cluster_name

  default_node_pool {
    name                = "system"
    node_count          = var.system_node_count
    vm_size             = "Standard_DS2_v2"
    type                = "VirtualMachineScaleSets"
    availability_zones  = [1, 2, 3]
    enable_auto_scaling = false
  }
/*
  service_principal  {
    client_id = var.serviceprinciple_id
    client_secret = var.serviceprinciple_key
  }
*/
  identity {
    type = "SystemAssigned"
  }
  # for flux configuration
  network_profile {
    network_plugin = "azure"
    network_policy = "calico"
  }
  # network_profile {
  #   load_balancer_sku = "Standard"
  #   network_plugin    = "kubenet"
  # }
}
