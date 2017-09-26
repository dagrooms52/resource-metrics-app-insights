import sys
import argparse
from monitors.cpumonitor import CpuMonitor
from monitors.diskmonitor import DiskMonitor
from monitors.memorymonitor import MemoryMonitor
from monitors.networkmonitor import NetworkMonitor
from appinsights.appinsightsreporter import AppInsightsReporter
from applicationinsights import TelemetryClient
from utilities.argumentparsergenerator import ArgumentParserGenerator

def main(appinsightskey, upload_interval_seconds, event_prefix, quiet):

    # These are defined as volumes in the Dockerfile
    host_proc_path = "/host/proc"
    host_top_dir = "/host/dir"

    monitors = [
        MemoryMonitor(host_proc_path, event_prefix),
        CpuMonitor(host_proc_path, event_prefix),
        DiskMonitor(host_top_dir, event_prefix),
        NetworkMonitor(host_proc_path, event_prefix)
    ]
    reporter = AppInsightsReporter(appinsightskey, monitors, upload_interval_seconds, quiet)

    # The collection & upload process
    reporter.run()

if __name__ == '__main__':

    # Read instrumentation key from command line
    parser = ArgumentParserGenerator().parser
    args = parser.parse_args()

    main(args.instrumentation_key, args.interval, args.prefix, args.quiet)
