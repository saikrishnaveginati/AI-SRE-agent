from prometheus_client import start_http_server, Counter, Histogram
import random
import time

# metrics
REQUEST_COUNT = Counter("app_requests_total", "Total requests")
REQUEST_LATENCY = Histogram("app_request_latency_seconds", "Request latency")

def simulate_traffic():
    while True:
        REQUEST_COUNT.inc()

        latency = random.uniform(0.1, 1.5)
        REQUEST_LATENCY.observe(latency)

        time.sleep(1)


if __name__ == "__main__":
    start_http_server(8000)
    print("Metrics server running on http://localhost:8000/metrics")

    simulate_traffic()