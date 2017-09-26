from monitors.basemonitor import BaseMonitor
from schema.telemetry import Telemetry
import psutil

class NetworkMonitor(BaseMonitor):
    
    def __init__(self, host_proc, event_prefix):
        self.event_prefix = event_prefix
        psutil.PROCFS_PATH = host_proc

    def get_telemetry(self):
        
        network_counters = psutil.net_io_counters()

        telemetry = [
            Telemetry(self.event_prefix + " Bytes Sent", network_counters.bytes_sent),
            Telemetry(self.event_prefix + " Bytes Recieved", network_counters.bytes_recv),
            Telemetry(self.event_prefix + " Packets Sent", network_counters.packets_sent),
            Telemetry(self.event_prefix + " Packets Recieved", network_counters.packets_recv),
            Telemetry(self.event_prefix + " Errors Incoming", network_counters.errin),
            Telemetry(self.event_prefix + " Errors Outgoing", network_counters.errout),
            Telemetry(self.event_prefix + " Dropped Packets Incoming", network_counters.dropin),
            Telemetry(self.event_prefix + " Dropped Packets Outgoing", network_counters.dropout)
        ]

        return telemetry
