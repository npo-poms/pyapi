#!/usr/bin/env python3

import subprocess
import os

subprocess.call(["npo_integration_tests", "-e", "test", "-c", os.path.dirname(os.path.dirname(os.path.realpath(__file__)))])
