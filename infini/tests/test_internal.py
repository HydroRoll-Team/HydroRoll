from infini.internal import require
from ipm import api

import shutil


def test_internal():
    api.new("test_ipk")
    registers = require("test_ipk")
    assert registers
    shutil.rmtree("test_ipk")
