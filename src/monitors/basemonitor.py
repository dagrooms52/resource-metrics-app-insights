# Define the monitor interface that will be picked up by the reporter

import abc

class BaseMonitor(metaclass=abc.ABCMeta):

    # Get all telemetry readings from the monitor
    # This clears the monitor queue
    # Returns: Schema.Telemetry[]
    @abc.abstractmethod
    def get_telemetry(self):
        pass