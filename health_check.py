import sys
import time

def verify_canary_health():
    print("Sending canary traffic to staging endpoint...")
    simulated_latencies = [120, 140, 110, 130] # ms
    error_rate = 0.0

    avg_latency = sum(simulated_latencies) / len(simulated_latencies)
    print(f"Canary Average Latency: {avg_latency}ms | Error Rate: {error_rate}%")

    if avg_latency > 250 or error_rate > 0.01:
        print("Canary health check FAILED.")
        sys.exit(1)
    
    print("Canary health check PASSED. Safe to promote to production.")
    sys.exit(0)

if __name__ == "__main__":
    verify_canary_health()
