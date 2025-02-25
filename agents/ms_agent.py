import os
from datetime import datetime
from dotenv import load_dotenv
from semantic_kernel.kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from plugins.ms_review import MicroserviceReviewPlugin

load_dotenv()

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../output/microservices_reviews")
os.makedirs(OUTPUT_DIR, exist_ok=True)


class MicroservicesAgent:
    def __init__(self, code_dir: str):
        """Initialize Kernel and plugin"""
        self.kernel = Kernel()
        self.kernel.add_service(
            AzureChatCompletion(
                deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
                api_key=os.getenv("AZURE_OPENAI_API_KEY"),
                endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            )
        )
        self.review_plugin = MicroserviceReviewPlugin(self.kernel, code_dir)

    async def execute(self):
        """Gọi plugin để thực hiện đánh giá kiến trúc microservices."""
        return await self.review_plugin.review_microservices()


# import asyncio
# if __name__ == "__main__":
#     agent = MicroservicesAgent()

#     architecture_description = """
#     The system consists of multiple microservices that communicate using REST APIs and gRPC.
#     It employs RabbitMQ as a messaging system for asynchronous communication.
#     Load balancing is handled via Kubernetes, which supports dynamic scaling.
#     Fault tolerance is achieved through retry policies, circuit breakers, and failover strategies.
#     Dependencies among services are managed via health checks and service discovery.
#     """

#     asyncio.run(agent.review_architecture(architecture_description))
