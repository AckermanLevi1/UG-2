class HyPoPEConsensus:
    def __init__(self, devices):
        self.devices = devices

    def calculate_scores(self):
        scores = {}
        for device in self.devices:
            metrics = device.metrics
            normalized_latency = (1 - metrics["latency"] / max(d.metrics["latency"] for d in self.devices))
            normalized_energy = (1 - metrics["energy"] / max(d.metrics["energy"] for d in self.devices))
            normalized_uptime = metrics["uptime"] / max(d.metrics["uptime"] for d in self.devices)

            # Weights for different metrics
            w_latency = 0.4
            w_energy = 0.4
            w_uptime = 0.2

            # Final score calculation
            score = w_latency * normalized_latency + w_energy * normalized_energy + w_uptime * normalized_uptime
            scores[device.device_id] = score
        return scores

    def select_device(self):
        scores = self.calculate_scores()
        best_device = max(scores, key=scores.get)
        return best_device, scores[best_device]
