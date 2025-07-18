#!/usr/bin/env pyhont3
import os

def check_reboot():
    """Retunrns True if the computer has a pending reboot."""
    return os.path.exist("/run/reboot-required")
def main():
    pass

main()
#this is a test