locals {
  env_type = "local"
}

module "blind-app" {
  source = "../deploy"

  env_type = local.env_type  
  namespace = "default"
}
