import uuid
from cryptography.hazmat.primitives.asymmetric import rsa # type: ignore
from cryptography.hazmat.primitives import serialization # type: ignore
import random

class IoTDevice:
    def __init__(self, device_id=None):
        self.device_id = device_id or str(uuid.uuid4())
        self.private_key = self.generate_private_key()
        self.public_key = self.generate_public_key()
        self.metrics = {
            "latency": round(random.uniform(0.1, 1.0), 3),
            "uptime": round(random.uniform(90, 100), 1),
            "energy": round(random.uniform(10, 50), 1),
        }

    def generate_private_key(self):
        return rsa.generate_private_key(public_exponent=65537, key_size=2048)

    def generate_public_key(self):
        return self.private_key.public_key()

    def serialize_keys(self):
        private_pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return private_pem, public_pem
