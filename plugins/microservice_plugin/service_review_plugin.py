from semantic_kernel.kernel import Kernel

class ServiceReviewPlugin:
    def __init__(self, kernel: Kernel):
        self.kernel = kernel

    async def review_service(self, service_name, service_path):
        """Gửi service lên AI để phân tích và review"""
        prompt = f"""
        You are an expert in Microservices Architecture.
        Analyze the following microservice and provide a structured review:

        ## 📌 Service Name: {service_name}
        ## 📂 Service Path: {service_path}

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

        📋 Provide strengths, weaknesses, and improvements.
        """
        response = await self.kernel.invoke_prompt(prompt)
        return response.text if response else "❌ No response from AI."

    async def review_all_services(self, services):
        """Review toàn bộ các microservices"""
        results = {}
        for service_name, service_path in services.items():
            results[service_name] = await self.review_service(service_name, service_path)
        return results
