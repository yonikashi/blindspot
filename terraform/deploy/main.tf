provider "kubernetes" {
  config_path    = "~/.kube/config"
}

resource "kubernetes_namespace" "blindspot_namespace" {
count = var.namespace == "default" ? 0 : 1
  metadata {
    name = var.namespace
  }
}

provider "helm" {
  kubernetes {
    config_path = "~/.kube/config"
  }
}

resource "helm_release" "resty_deploy" {
  name       = "resty-helm-deploy"
  chart      = "${path.module}/automate"
}
