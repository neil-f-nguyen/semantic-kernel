```hcl
provider "azurerm" {
  features {}
}

variable "location" {
  default = "eastus"
}

variable "vm_size" {
  default = "Standard_D2s_v3"
}

variable "vm_name" {
  default = "my-vm"
}

variable "admin_username" {
  default = "adminuser"
}

variable "admin_password" {
  default = "AdminPassword123!"
}

resource "azurerm_resource_group" "rg" {
  name     = "myResourceGroup"
  location = var.location
}

resource "azurerm_virtual_network" "vnet" {
  name                = "myVnet"
  address_space       = ["10.0.0.0/16"]
  location            = var.location
  resource_group_name = azurerm_resource_group.rg.name
}

resource "azurerm_subnet" "subnet" {
  name                 = "mySubnet"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = ["10.0.1.0/24"]
}

resource "azurerm_network_security_group" "nsg" {
  name                = "myNSG"
  location            = var.location
  resource_group_name = azurerm_resource_group.rg.name
}

resource "azurerm_network_interface" "nic" {
  name                = "myNIC"
  location            = var.location
  resource_group_name = azurerm_resource_group.rg.name

  ip_configuration {
    name                          = "myNICConfiguration"
    subnet_id                     = azurerm_subnet.subnet.id
    private_ip_address_allocation = "Dynamic"
    primary                       = true
  }
}

resource "azurerm_linux_virtual_machine" "vm" {
  name                = var.vm_name
  resource_group_name = azurerm_resource_group.rg.name
  location            = var.location
  size                = var.vm_size
  admin_username      = var.admin_username
  admin_password      = var.admin_password

  network_interface_ids = [azurerm_network_interface.nic.id]

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
  
  computer_name  = var.vm_name
}

output "vm_id" {
  value = azurerm_linux_virtual_machine.vm.id
}

output "vm_public_ip" {
  value = azurerm_network_interface.nic.private_ip_address
}
```