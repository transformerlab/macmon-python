from macmon import MacMon

try:
    metrics = MacMon()
    data = metrics.get_metrics()
    
    print("System Metrics:")
    print(data)

except Exception as e:
    print(f"Error: {e}")
