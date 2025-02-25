import os
from dotenv import load_dotenv
from datetime import datetime
from semantic_kernel.kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from plugins.tf_generator import TFGenerator
from plugins.tf_validator import TFValidator

load_dotenv()

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../output/terraform_files")
os.makedirs(OUTPUT_DIR, exist_ok=True)


class TerraformAgent:
    def __init__(self):
        self.kernel = Kernel()

        # Kết nối Azure OpenAI
        self.kernel.add_service(
            AzureChatCompletion(
                deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
                api_key=os.getenv("AZURE_OPENAI_API_KEY"),
                endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            )
        )

        self.generator = TFGenerator(self.kernel)
        self.validator = TFValidator()

    async def generate_terraform(self, config):
        """Tạo file Terraform từ config và OpenAI."""
        print("[🤖] Generating Terraform file...")
        terraform_code = await self.generator.generate(config)

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_path = os.path.relpath(os.path.join(OUTPUT_DIR, f"main_{timestamp}.tf"))

        with open(file_path, "w") as f:
            f.write(terraform_code)

        print(f"[✅] Terraform file generated: {file_path}")

        if self.validator.validate(file_path):
            print("[✅] Terraform file is valid")
        else:
            print("[❌] Terraform file is invalid")


#
# if __name__ == "__main__":
#     agent = TerraformAgent()
#
#     user_config = {
#         "provider": "azure",
#         "region": "eastus",
#         "resource": "azurerm_virtual_machine",
#         "name": "my-vm",
#         "size": "Standard_D2s_v3",
#         "image": "UbuntuLTS"
#     }
#
#     agent.generate_terraform(user_config)
