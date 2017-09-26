from monitors.basemonitor import BaseMonitor
from schema.telemetry import Telemetry
import psutil

class DiskMonitor(BaseMonitor):
    
    def __init__(self, host_dir, event_prefix):
        self.event_prefix = event_prefix
        self.host_dir = host_dir

    def get_telemetry(self):
        disk_usage = psutil.disk_usage(self.host_dir)

        telemetry = [
            Telemetry(self.event_prefix + " Total Disk", disk_usage.total, { "disk", self.host_dir }),
            Telemetry(self.event_prefix + " Used Disk", disk_usage.used, { "disk", self.host_dir }),
            Telemetry(self.event_prefix + " Free Disk", disk_usage.free, { "disk", self.host_dir }),
            Telemetry(self.event_prefix + " Disk Percent Used", disk_usage.percent, { "disk", self.host_dir })
        ]

        return telemetry
