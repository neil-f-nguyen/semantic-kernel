import os
from dotenv import load_dotenv
from semantic_kernel.kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from plugins.tf_generator import TFGenerator
from plugins.tf_validator import TFValidator

# Load biến môi trường từ .env.example
load_dotenv()


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

    def generate_terraform(self, config):
        """Tạo file Terraform từ config và OpenAI."""
        terraform_code = self.generator.generate(config)

        # Lưu vào file
        file_path = "terraform_files/main.tf"
        with open(file_path, "w") as f:
            f.write(terraform_code)

        print(f"[✅] Terraform file generated: {file_path}")

        # Kiểm tra Terraform hợp lệ không
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
