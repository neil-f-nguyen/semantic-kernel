# from agents.microservice_agent import MicroservicesAgent
# import asyncio
from agents.microservice_agent import MicroserviceAgent


# async def main():
#     agent = MicroservicesAgent()

#     architecture_description = """
#     The system consists of multiple microservices that communicate using REST APIs and gRPC.
#     It employs RabbitMQ as a messaging system for asynchronous communication.
#     Load balancing is handled via Kubernetes, which supports dynamic scaling.
#     Fault tolerance is achieved through retry policies, circuit breakers, and failover strategies.
#     Dependencies among services are managed via health checks and service discovery.
#     """

#     await agent.review_architecture(architecture_description)


# if __name__ == "__main__":
#     asyncio.run(main())

#
# from agents.microservice_agent import MicroservicesAgent
# import asyncio
#
#
# async def main():
#     agent = MicroservicesAgent(code_dir="C:\\Users\\Tu.d.nguyen\\Downloads\\complete-microservice-application-master")
#
#     await agent.execute()
#
#
# if __name__ == "__main__":
#     asyncio.run(main())


async def main():
    agent = MicroserviceAgent(root_dir="./your_microservices_project")

    results = await agent.execute()

    print("📋 Microservices Architecture Review Report:")
    for service, report in results.items():
        print(f"\n🔹 {service}:\n{report}\n")

import asyncio
if __name__ == "__main__":
    asyncio.run(main())