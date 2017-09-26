# Using information from the monitors, report resource telemetry to Application Insights

from applicationinsights import TelemetryClient
from schema.telemetry import Telemetry
from monitors.basemonitor import BaseMonitor
import time

class AppInsightsReporter(object):
    
    def __init__(self, appinsightskey, monitor_list, upload_interval_seconds=60, quiet=False):
        self.monitors = monitor_list
        self.telemetry = []
        self.telemetry_client = TelemetryClient(appinsightskey)
        self.upload_interval_seconds = upload_interval_seconds
        self.quiet = quiet

    def run(self):
        while(True):
            self.collect_metrics()
            self.upload_metrics()
            self.purge_metrics()

            time.sleep(self.upload_interval_seconds)

    def collect_metrics(self):
        for monitor in self.monitors:
            self.telemetry.extend(monitor.get_telemetry())

    def upload_metrics(self):
        # Can just upload our telemetry schema since it matches MS schema
        if not self.quiet:
            print("Uploading telemetry...")

        for datapoint in self.telemetry:
            self.telemetry_client.track_metric(datapoint.name, datapoint.value)

        self.telemetry_client.flush()
        
        if not self.quiet:
            print("Upload complete")

    def purge_metrics(self):
        self.telemetry = []
