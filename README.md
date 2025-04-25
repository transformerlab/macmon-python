# macmon-python

A Python wrapper for a binary that reports system metrics like CPU/GPU temperature, 
memory usage, and power consumption.

This just a simple wrapper around https://github.com/vladkens/macmon

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

### Async Usage

```python
from macmon import MacMon
import asyncio
async def main():
    # Create an instance
    metrics = MacMon()
    data = await metrics.get_metrics_async()

    print("System Metrics:")
    print(data)

asyncio.run(main())
```