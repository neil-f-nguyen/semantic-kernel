from semantic_kernel.kernel import Kernel


class TFGenerator:
    def __init__(self, kernel: Kernel):
        self.kernel = kernel

    async def generate(self, config):
        """Tạo file Terraform bằng LLM."""
        prompt = f"""
        Generate a Terraform configuration file for {config['provider']}:
        - Region: {config['region']}
        - Resource: {config['resource']}
        - Name: {config['name']}
        - Additional details: {config}
        """

        # Gọi Azure OpenAI để sinh Terraform code
        response = await self.kernel.invoke_prompt(prompt)
        return str(response)
