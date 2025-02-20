from agents.terraform_agent import TerraformAgent


def main():
    agent = TerraformAgent()

    user_config = {
        "provider": "azure",
        "region": "eastus",
        "resource": "azurerm_virtual_machine",
        "name": "my-vm",
        "size": "Standard_D2s_v3",
        "image": "UbuntuLTS"
    }

    agent.generate_terraform(user_config)


if __name__ == "__main__":
    main()
