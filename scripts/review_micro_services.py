# from agents.microservice_agent import MicroservicesAgent
# import asyncio


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


from agents.microservice_agent import MicroservicesAgent
import asyncio


async def main():
    agent = MicroservicesAgent(code_dir="C:\\Users\\Tu.d.nguyen\\Downloads\\complete-microservice-application-master")

    await agent.execute()


if __name__ == "__main__":
    asyncio.run(main())
