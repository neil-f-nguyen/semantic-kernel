from semantic_kernel.kernel import Kernel


class TFGenerator:
    def __init__(self, kernel: Kernel):
        self.kernel = kernel

    async def generate(self, config):
        """Generate Terraform file using LLM."""
        prompt = f"""
        Generate only the content of a complete Terraform configuration file for {config["provider"]}.

        ## Requirements:
        - **Cloud Provider**: {config["provider"]}
        - **Region**: {config["region"]}
        - **Resource Type**: {config["resource"]}
        - **Resource Name**: {config["name"]}
        - **Additional Details**: {config}

        ## Expected Output:
        This Terraform script should:
        - Define all necessary **resource blocks** for services such as VPC, Subnets, EC2 Instances, Security Groups, Load Balancers, and any other requested components.
        - Ensure correct **syntax** and follow **best practices** for cloud resource provisioning.
        - Include **variables and outputs** where applicable to promote reusability and modularity.
        - Apply **least privilege principles** when defining IAM roles and security group rules.
        - Optimize **network configurations** for scalability and high availability.

        🚀 Please return only the Terraform script content without additional explanations or metadata.
        """
        # Call Azure OpenAI to generate Terraform code
        response = await self.kernel.invoke_prompt(prompt)
        return str(response)
