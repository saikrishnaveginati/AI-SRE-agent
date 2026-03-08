from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("metrics-server")

METRICS_URL = "http://localhost:8000/metrics"


@mcp.tool()
def get_metrics():
    """Fetch raw metrics from Prometheus endpoint"""
    response = requests.get(METRICS_URL)
    return response.text


@mcp.tool()
def detect_latency_issue():
    """Check if latency is unusually high"""
    
    response = requests.get(METRICS_URL)
    data = response.text

    lines = data.split("\n")

    latency_sum = None
    latency_count = None

    for line in lines:
        if "app_request_latency_seconds_sum" in line:
            latency_sum = float(line.split(" ")[1])
        if "app_request_latency_seconds_count" in line:
            latency_count = float(line.split(" ")[1])

    if latency_sum and latency_count:
        avg_latency = latency_sum / latency_count

        if avg_latency > 0.5:
            return f"High latency detected. Avg latency: {avg_latency:.2f}s"
        else:
            return f"Latency normal. Avg latency: {avg_latency:.2f}s"

    return "Latency metrics not found"


if __name__ == "__main__":
    mcp.run()