import argparse

class ArgumentParserGenerator(object):

    def __init__(self):
        self.parser = argparse.ArgumentParser(description = "Send resource usage to Application Insights")

        self.parser.add_argument(
            "-k",
            "--instrumentation-key", 
            help = "The Application Insights Instrumentation Key for your instance.", 
            type = str
        )

        self.parser.add_argument(
            "-i",
            "--interval",
            help = "Number of seconds to wait between measuring resource usage.",
            type = int,
            nargs = '?',
            default = 60,
            const = 60
        )

        self.parser.add_argument(
            "-p",
            "--prefix",
            help = "The name prefix for the custom Application Insights events. For example, the prefix \"Device\" yields events such as \"Device Packets Recieved.\"",
            type = str,
            nargs = '?',
            default = "Device",
            const = "Device"
        )

        self.parser.add_argument(
            "-q",
            "--quiet",
            help = "Signifies that the container should run without creating output, such as upload status.",
            action = "store_true"
        )
