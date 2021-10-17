provider "digitalocean" {}

terraform {
    required_providers{
        digitalocean = {
            source = "digitalocean/digitalocean"
            version = "~> 2.0"
        }
    }
}

resource "digitalocean_droplet" "web" {
    image = "ubuntu-20-04-x64"
    name = "web-1"
    region = "ams3"
    size = "s-1vcpu-1gb"
}