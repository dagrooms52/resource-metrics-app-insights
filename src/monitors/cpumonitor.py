from monitors.basemonitor import BaseMonitor
from schema.telemetry import Telemetry
import psutil

class CpuMonitor(BaseMonitor):
    
    def __init__(self, host_proc, event_prefix):
        self.event_prefix = event_prefix
        # Have to redirect this so we're not reading the container's /proc but the host's
        psutil.PROCFS_PATH = host_proc
        
        # Start the cpu_percent interval - this will return 0 the first time
        psutil.cpu_times_percent()

    # Get the monitor data for this monitor
    def get_telemetry(self):
        cpu_times_percent = psutil.cpu_times_percent()
       
        telemetry = [
            Telemetry(self.event_prefix + " User Percent CPU", cpu_times_percent.user),
            Telemetry(self.event_prefix + " NICE Percent CPU", cpu_times_percent.nice),
            Telemetry(self.event_prefix + " System Percent CPU", cpu_times_percent.system),
            Telemetry(self.event_prefix + " Idle Percent CPU", cpu_times_percent.idle)
        ]

        return telemetry
