from blockchain import Blockchain
from iot_device import IoTDevice
from hypope_consensus import HyPoPEConsensus
import time

class ShipmentTracker:
    def __init__(self):
        self.blockchain = Blockchain()
        self.devices = [IoTDevice() for _ in range(5)]  # Register 5 IoT devices

    def add_shipment(self, shipment_id, location, status):
        consensus = HyPoPEConsensus(self.devices)
        best_device, score = consensus.select_device()
        self.centralized_db = []  # Simulated database

        
        data = {
            "shipment_id": shipment_id,
            "location": location,
            "status": status,
            "timestamp": time.time(),
        }

        self.blockchain.add_block(data, best_device)
        print(f"Shipment added with IoT Device: {best_device} (Score: {score:.2f})")

    def view_chain(self):
        return [{"index": block.index, "data": block.data, "device": block.selected_device, "hash": block.hash} 
                for block in self.blockchain.chain]

    def validate_chain(self):
        return self.blockchain.is_chain_valid()
    def tamper_data(self, index, key, new_value):
        # Tamper centralized database
        if index < len(self.centralized_db):
            self.centralized_db[index][key] = new_value

        # Tamper blockchain (for demo purposes)
        if index < len(self.blockchain.chain):
            self.blockchain.chain[index].data[key] = new_value

    def view_centralized_db(self):
        return self.centralized_db

