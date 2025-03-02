import os
import math


class CodeReaderPlugin:
    """A plugin to read and analyze microservice source code efficiently."""

    def __init__(self, max_files_per_batch=3):
        """
        Initializes the plugin with batch processing settings.

        :param max_files_per_batch: Number of files per batch for AI processing.
        """
        self.important_keywords = ["controller", "service", "repository", "config", "messaging"]
        self.max_files_per_batch = max_files_per_batch  # Controls batch size

    def is_important_file(self, filename):
        """
        Determines if a file is important based on keywords.

        :param filename: The name of the file to check.
        :return: True if the file is relevant for analysis, otherwise False.
        """
        return any(keyword in filename.lower() for keyword in self.important_keywords)

    def read_service_code(self, service_path):
        """
        Reads and collects relevant source code files from a microservice.

        :param service_path: Path to the microservice directory.
        :return: A list of (filename, content) tuples.
        """
        code_content = []

        for root, _, files in os.walk(service_path):
            for file in files:
                if file.endswith((".java", ".yml", ".properties")):
                    if self.is_important_file(file):
                        file_path = os.path.join(root, file)
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = "".join(f.readlines()[:300])  # Limit to 300 lines per file
                            code_content.append((file, content))

        return code_content

    def get_batches(self, service_path):
        """
        Splits collected files into smaller batches to avoid AI processing limitations.

        :param service_path: Path to the microservice directory.
        :return: A list of batches, each containing a set of (filename, content) tuples.
        """
        all_files = self.read_service_code(service_path)
        num_batches = math.ceil(len(all_files) / self.max_files_per_batch)

        return [all_files[i * self.max_files_per_batch: (i + 1) * self.max_files_per_batch] for i in range(num_batches)]
