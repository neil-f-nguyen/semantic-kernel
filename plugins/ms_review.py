# from semantic_kernel.kernel import Kernel


# class MicroservicesReview:
#     def __init__.py(self, kernel: Kernel):
#         self.kernel = kernel

#     async def review(self, architecture_desc: str) -> str:
#         """Generate a detailed review report for the given microservices architecture."""
#         prompt = f"""
#         Conduct a comprehensive review of the given microservices architecture. Focus on these aspects:

#         - **Inter-Service Communication:** Analyze communication protocols (e.g., REST, gRPC, messaging systems) to ensure efficient data exchange, evaluate latency, serialization/deserialization overhead, and potential bottlenecks.
#         - **Load Balancing:** Assess load balancing mechanisms, including configurations for dynamic scaling under varying workloads, and identify any limitations or inefficiencies.
#         - **Fault Tolerance:** Review mechanisms for handling failures, such as retry policies, circuit breakers, and failover strategies. Verify the effectiveness of service degradation or fallback options during outages.
#         - **Service Dependencies:** Map and evaluate dependencies among services to identify potential risks of cascading failures. Analyze service startup sequences, health checks, and dependency management.

#         Architecture Description:
#         {architecture_desc}

#         Please provide a detailed review report with key findings and recommendations.
#         Only return the content of the report, without additional metadata or formatting.
#         """

#         response = await self.kernel.invoke_prompt(prompt)
#         return str(response)
import os
from semantic_kernel.kernel import Kernel

class MicroserviceReviewPlugin:
    def __init__(self, kernel: Kernel, code_dir: str):
        self.kernel = kernel
        self.code_dir = code_dir

    def read_code_files(self):
        """Đọc toàn bộ mã nguồn trong thư mục chỉ định."""
        code_files = []
        for root, _, files in os.walk(self.code_dir):
            for file in files:
                if file.endswith(('.py', '.js', '.ts', '.go', '.java', '.yaml', '.yml', '.json', 'Dockerfile')):
                    file_path = os.path.join(root, file)
                    code_files.append(file_path)
        return code_files

    async def analyze_file(self, file_path: str):
        """Phân tích một file mã nguồn để đánh giá kiến trúc microservices."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code_content = f.read()
        except Exception as e:
            print(f"⚠️ Không thể đọc file {file_path}: {e}")
            return f"❌ Không thể đọc file {file_path}: {e}"

        prompt = f"""
        You are an expert in Microservices Architecture. Analyze the provided source code based on these key areas:

        ## 🔄 Inter-Service Communication:
        - Identify communication patterns (REST, gRPC, Message Queue, WebSocket).
        - Check for possible latency issues.

        ## ⚖️ Load Balancing:
        - Review API Gateway and Load Balancer settings.
        - Detect inefficient traffic routing.

        ## 🛠️ Fault Tolerance:
        - Check retry policies, circuit breakers, and failover mechanisms.

        ## 🔗 Service Dependencies:
        - Identify risks of cascading failures.
        - Evaluate service health checks.

        **Source Code for Analysis:**
        {code_content}

        📌 Provide a structured review with strengths, weaknesses, and improvement suggestions.
        """
        print(f"[🤖] Sending code content to AI for analysis: {prompt}")
        response = await self.kernel.invoke_prompt(prompt)
        print(f"[🤖] AI Response: {response}")
        return str(response) if response else "❌ No response from AI."

    async def review_microservices(self):
        """Chạy đánh giá microservices bằng cách đọc code và gửi lên AI."""
        code_files = self.read_code_files()
        if not code_files:
            return "❌ No source code found for analysis."

        results = []
        for file_path in code_files:
            print(f"[🤖] Analyzing file: {file_path}")
            result = await self.analyze_file(file_path)
            results.append(f"### Review for {file_path} ###\n{result}\n")

        return "\n".join(results)
