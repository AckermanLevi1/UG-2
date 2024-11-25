from flask import Flask, render_template, request, jsonify
from shipment_tracker import ShipmentTracker
import random

app = Flask(__name__)

# Initialize Shipment Tracker
tracker = ShipmentTracker()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_shipment", methods=["GET", "POST"])
def add_shipment():
    if request.method == "POST":
        shipment_id = request.form["shipment_id"]
        location = request.form["location"]
        status = request.form["status"]

        tracker.add_shipment(shipment_id, location, status)
        return jsonify({"message": "Shipment added successfully!"})
    return render_template("add_shipment.html")

@app.route("/view_chain")
def view_chain():
    chain_data = [{"index": block.index, "data": block.data, "device": block.selected_device, "hash": block.hash} 
                  for block in tracker.blockchain.chain]
    return render_template("chain.html", chain=chain_data)

@app.route("/validate_chain")
def validate_chain():
    is_valid = tracker.validate_chain()
    return jsonify({"is_valid": is_valid})

@app.route("/energy_metrics")
def energy_metrics():
    metrics = [{"device_id": device.device_id, "latency": device.metrics["latency"],
                "uptime": device.metrics["uptime"], "energy": device.metrics["energy"]}
               for device in tracker.devices]
    return jsonify(metrics)

# @app.route("/visualize_energy")
# def visualize_energy():
#     return render_template("energy_metrics.html")

if __name__ == "__main__":
    app.run(debug=True)
