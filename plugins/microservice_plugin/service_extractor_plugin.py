import os

class ServiceExtractorPlugin:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def find_microservices(self):
        """Tìm tất cả các thư mục chứa microservice"""
        services = {}

        for service_dir in os.listdir(self.root_dir):
            full_path = os.path.join(self.root_dir, service_dir)

            # Kiểm tra nếu thư mục chứa service (có pom.xml hoặc build.gradle)
            if os.path.isdir(full_path) and ("pom.xml" in os.listdir(full_path) or "build.gradle" in os.listdir(full_path)):
                services[service_dir] = full_path

        return services
