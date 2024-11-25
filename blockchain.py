import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, selected_device, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.selected_device = selected_device
        self.timestamp = timestamp or time.time()
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.data}{self.selected_device}{self.timestamp}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", "Genesis Block", "None")
        self.chain.append(genesis_block)

    def add_block(self, data, selected_device):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), previous_block.hash, data, selected_device)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.compute_hash() or current.previous_hash != previous.hash:
                return False
        return True
