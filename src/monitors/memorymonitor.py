from monitors.basemonitor import BaseMonitor
from schema.telemetry import Telemetry
import psutil

class MemoryMonitor(BaseMonitor):
    
    def __init__(self, host_proc, event_prefix):
        psutil.PROCFS_PATH = host_proc
        self.event_prefix = event_prefix

    def get_telemetry(self):
        meminfo = psutil.virtual_memory()
        
        telemetry = [
            Telemetry(self.event_prefix + " Total Memory", meminfo.total),
            Telemetry(self.event_prefix + " Free Memory", meminfo.available),
            Telemetry(self.event_prefix + " Used Memory", meminfo.used),
            Telemetry(self.event_prefix + " Used Memory Percentage", meminfo.percent)
        ]

        return telemetry
    