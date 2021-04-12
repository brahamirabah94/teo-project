variable "resource_group_name" {
  type        = string
  description = "RG name in Azure"
}

variable "location" {
  type        = string
  description = "Resources location in Azure"
}
variable "storage-account-name" {
  type        = string
  description = "strorage account name"
}

variable "backend-rg" {
  type        = string
  description = "backend RG in Azure"
}
variable "container-name" {
  type        = string
  description = "container name"
}

variable "backend-name" {
  type        = string
  description = "backend name key in Azure"
}
variable "cluster_name" {
  type        = string
  description = "AKS name in Azure"
}

variable "kubernetes_version" {
  type        = string
  description = "Kubernetes version"
}

variable "system_node_count" {
  type        = number
  description = "Number of AKS worker nodes"
}
