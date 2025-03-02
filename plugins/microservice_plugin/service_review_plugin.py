from semantic_kernel.kernel import Kernel
from plugins.microservice_plugin import CodeReaderPlugin


class ServiceReviewPlugin:
    """A plugin that analyzes microservice architecture using AI."""

    def __init__(self, kernel: Kernel):
        """
        Initializes the plugin with an AI kernel and a code reader.

        :param kernel: The AI execution engine.
        """
        self.kernel = kernel
        self.code_reader = CodeReaderPlugin()  # Injecting the CodeReaderPlugin

    async def review_service(self, service_name, service_path):
        """
        Performs an AI-driven review of a microservice by analyzing its source code in batches.

        :param service_name: The name of the microservice.
        :param service_path: Path to the microservice directory.
        :return: A comprehensive review report.
        """
        batches = self.code_reader.get_batches(service_path)
        all_reviews = []

        for i, batch in enumerate(batches):
            batch_content = "\n".join([f"\n📄 {file}:\n{content}" for file, content in batch])

            prompt = f"""
            You are an expert in Microservices Architecture.
            Analyze the following batch of microservice code:

            ## 📌 Service Name: {service_name}
            ## 📂 Batch {i + 1}/{len(batches)}

            ## 🔄 API Design
            - Detect REST, GraphQL, or gRPC endpoints.
            - Check if API design follows best practices.

            ## 🛢️ Database & Dependencies
            - Identify the database used (SQL, NoSQL).
            - Check for external dependencies.

            ## 📡 Message Queue & Events
            - Detect message brokers (Kafka, RabbitMQ, SQS).
            - Check for asynchronous event-driven design.

            ## ⚖️ Scalability & Performance
            - Identify scaling mechanisms (Kubernetes, Load Balancer).
            - Review performance optimizations.

            ## 🛡️ Security
            - Check authentication (JWT, OAuth).
            - Identify potential security issues.

            --- 📂 Microservice Code (Batch {i + 1}) ---
            {batch_content}

            📋 Provide strengths, weaknesses, and improvements.
            """

            response = await self.kernel.invoke_prompt(prompt)
            review = response.text if response else f"❌ No response for batch {i + 1}"
            all_reviews.append(f"📂 **Batch {i + 1}/{len(batches)}**:\n{review}")

        return "\n\n".join(all_reviews)
