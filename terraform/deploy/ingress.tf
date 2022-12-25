resource "kubernetes_ingress_v1" "resty_ingress" {
  count = var.env_type == "local" ? 0 : 1
  metadata {
    name = "resty-ingress"
  }

  spec {
    default_backend {
      service {
        name = "resty-chart"
        port {
          number = 5000
        }
      }
    }

    tls {
      secret_name = "tls-secret"
    }
  }
  depends_on = [
    helm_release.resty_deploy
  ]
}
