resource "digitalocean_ssh_key" "this" {
  name = "Manjaro NL"
  public_key = file("${path.module}/files/digitalocean.pub")
}
