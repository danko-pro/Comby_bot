"""
Example plugin showing the plugin system structure.
"""
from typing import Any, Dict

class ExamplePlugin:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    async def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Example plugin processing method.
        Extend this with your actual plugin logic.
        """
        return {
            "plugin": "example",
            "input": data,
            "result": "processed"
        }