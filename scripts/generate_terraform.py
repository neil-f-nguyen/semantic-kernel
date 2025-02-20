from agents.terraform_agent import TerraformAgent
import asyncio


async def main():
    agent = TerraformAgent()

    user_config = {
        "provider": "azure",
        "region": "eastus",
        "resource": "azurerm_virtual_machine",
        "name": "my-vm",
        "size": "Standard_D2s_v3",
        "image": "UbuntuLTS",
    }

    await agent.generate_terraform(user_config)


if __name__ == "__main__":
    asyncio.run(main())
