from macmon import MacMon
import json

try:
    metrics = MacMon()
    data = metrics.get_metrics()
    
    print("System Metrics:")
    print(data)

    d = json.loads(data)

    # pretty print:
    print(json.dumps(d, indent=4))
    
    # Additional functions to format and print data
    def print_temperature(temp_data):
        if temp_data:
            cpu_temp = temp_data.get("cpu_temp_avg", "N/A")
            gpu_temp = temp_data.get("gpu_temp_avg", "N/A")
            print(f"CPU Temperature: {cpu_temp:.2f}°C")
            print(f"GPU Temperature: {gpu_temp:.2f}°C")
        else:
            print("Temperature data not available.")

    def print_power_usage(data):
        print(f"Total Power: {data.get('all_power', 'N/A'):.2f} W")
        print(f"CPU Power: {data.get('cpu_power', 'N/A'):.2f} W")
        print(f"GPU Power: {data.get('gpu_power', 'N/A'):.2f} W")
        print(f"RAM Power: {data.get('ram_power', 'N/A'):.2f} W")
        print(f"System Power: {data.get('sys_power', 'N/A'):.2f} W")

    def print_memory_usage(memory_data):
        if memory_data:
            ram_total = memory_data.get("ram_total", 0) / (1024 ** 3)  # Convert bytes to GB
            ram_usage = memory_data.get("ram_usage", 0) / (1024 ** 3)  # Convert bytes to GB
            print(f"RAM Total: {ram_total:.2f} GB")
            print(f"RAM Usage: {ram_usage:.2f} GB")
            swap_total = memory_data.get("swap_total", 0) / (1024 ** 3)  # Convert bytes to GB
            swap_usage = memory_data.get("swap_usage", 0) / (1024 ** 3)  # Convert bytes to GB
            print(f"Swap Total: {swap_total:.2f} GB")
            print(f"Swap Usage: {swap_usage:.2f} GB")
        else:
            print("Memory data not available.")

    def print_cpu_gpu_usage(data):
        ecpu_usage = data.get("ecpu_usage", ["N/A", "N/A"])
        pcpu_usage = data.get("pcpu_usage", ["N/A", "N/A"])
        gpu_usage = data.get("gpu_usage", ["N/A", "N/A"])
        print(f"ECPU Frequency: {ecpu_usage[0]} MHz, Usage: {ecpu_usage[1] * 100:.2f}%")
        print(f"PCPU Frequency: {pcpu_usage[0]} MHz, Usage: {pcpu_usage[1] * 100:.2f}%")
        print(f"GPU Frequency: {gpu_usage[0]} MHz, Usage: {gpu_usage[1] * 100:.2f}%")

    # Call the functions to print formatted data
    print_temperature(d.get("temp"))
    print_power_usage(d)
    print_memory_usage(d.get("memory"))
    print_cpu_gpu_usage(d)

except Exception as e:
    print(f"Error: {e}")
