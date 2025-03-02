# import os
# from datetime import datetime
# from dotenv import load_dotenv
# from semantic_kernel.kernel import Kernel
# from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
# from plugins.ms_review import MicroservicesReview

# load_dotenv()

# OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../output/microservices_reviews")
# os.makedirs(OUTPUT_DIR, exist_ok=True)


# class MicroservicesAgent:
#     def __init__.py(self):
#         """Initialize Kernel and plugin"""
#         self.kernel = Kernel()
#         self.kernel.add_service(
#             AzureChatCompletion(
#                 deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
#                 api_key=os.getenv("AZURE_OPENAI_API_KEY"),
#                 endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
#             )
#         )

#         self.review_plugin = MicroservicesReview(self.kernel)

#     async def review_architecture(self, architecture_desc: str) -> str:
#         """Call AI to review architecture and save report."""
#         try:
#             print("[🤖] Reviewing microservices architecture...")
#             report = await self.review_plugin.review(architecture_desc)

#             # Create timestamp & name the report file
#             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#             file_path = os.path.relpath(
#                 os.path.join(OUTPUT_DIR, f"microservices_review_{timestamp}.txt")
#             )

#             # Save report content to file
#             with open(file_path, "w", encoding="utf-8") as f:
#                 f.write(
#                     f"""Microservices Architecture:\n{architecture_desc}\nReview Report:\n{report}"""
#                 )

#             print(f"[✅] Review report saved at: {file_path}")
#             return report
#         except Exception as e:
#             print(f"[❌] Error reviewing architecture: {e}")
#             return ""


# # import asyncio
# # if __name__ == "__main__":
# #     agent = MicroservicesAgent()

# #     architecture_description = """
# #     The system consists of multiple microservices that communicate using REST APIs and gRPC.
# #     It employs RabbitMQ as a messaging system for asynchronous communication.
# #     Load balancing is handled via Kubernetes, which supports dynamic scaling.
# #     Fault tolerance is achieved through retry policies, circuit breakers, and failover strategies.
# #     Dependencies among services are managed via health checks and service discovery.
# #     """

# #     asyncio.run(agent.review_architecture(architecture_description))


# import os
# from dotenv import load_dotenv
# from semantic_kernel.kernel import Kernel
# from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
# from plugins.ms_review import MicroserviceReviewPlugin
#
# load_dotenv()
#
# OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../output/microservices_reviews")
# os.makedirs(OUTPUT_DIR, exist_ok=True)
#
#
# class MicroservicesAgent:
#     def __init__(self, code_dir: str):
#         """Initialize Kernel and plugin"""
#         self.kernel = Kernel()
#         self.kernel.add_service(
#             AzureChatCompletion(
#                 deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
#                 api_key=os.getenv("AZURE_OPENAI_API_KEY"),
#                 endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
#             )
#         )
#         self.review_plugin = MicroserviceReviewPlugin(self.kernel, code_dir)
#
#     async def execute(self):
#         """Gọi plugin để thực hiện đánh giá kiến trúc microservices."""
#         print("[🤖] Reviewing microservices architecture...")
#         return await self.review_plugin.review_microservices()


# import asyncio

# if __name__ == "__main__":
#     agent = MicroservicesAgent(code_dir="./your_project_folder")
#     asyncio.run(agent.execute())

from semantic_kernel.kernel import Kernel
from plugins.microservice_plugin import ServiceExtractorPlugin, ServiceReviewPlugin


class MicroserviceAgent:
    def __init__(self, root_dir: str):
        self.kernel = Kernel()
        self.extractor = ServiceExtractorPlugin(root_dir)
        self.review_plugin = ServiceReviewPlugin(self.kernel)

    async def execute(self):
        """Phát hiện & review toàn bộ các microservices"""
        services = self.extractor.find_microservices()
        if not services:
            return "❌ No microservices found."
        return await self.review_plugin.review_all_services(services)


async def main():
    agent = MicroserviceAgent(root_dir="./your_microservices_project")

    results = await agent.execute()

    print("📋 Microservices Architecture Review Report:")
    for service, report in results.items():
        print(f"\n🔹 {service}:\n{report}\n")

import asyncio
if __name__ == "__main__":
    asyncio.run(main())