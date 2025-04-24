# macmon-python

A Python wrapper for a binary that reports system metrics like CPU/GPU temperature, 
memory usage, and power consumption.

## Installation

```bash
pip install macmon-python
```

## Usage

```python
from macmon import MacMon

# Create an instance
metrics = MacMon()
data = metrics.get_metrics()

print("System Metrics:")
print(data)
```

## License

MIT