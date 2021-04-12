resource_group_name = "rg-teoschool-rabah-001"
location            = "West Europe"
cluster_name        = "teoSch-aks-cluster"
kubernetes_version  = "1.18"
system_node_count   = 1

backend-rg = "rg-teoschool-rabah-001"
storage-account-name = "sateotfrabah"
container-name = "container-tfstate"
backend-name = "terraform.state"
