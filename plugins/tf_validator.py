import subprocess

class TFValidator:
    def validate(self, file_path):
        """Kiểm tra Terraform syntax."""
        try:
            result = subprocess.run(["terraform", "fmt", "-check", file_path], capture_output=True, text=True)
            return result.returncode == 0
        except Exception as e:
            print(f"[❌] Validation error: {e}")
            return False
