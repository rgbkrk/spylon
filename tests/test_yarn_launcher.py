from __future__ import print_function, absolute_import
from spylon.spark import prepare_pyspark_yarn_interactive
import spylon.spark.launcher as sparklauncher
import os


def test_prepare_interactive():
    c = sparklauncher.SparkConfiguration()

    new_conf = prepare_pyspark_yarn_interactive("conda", "hdfs://some/env/conda.zip", c)

    # Must be a new instance not a copy.
    assert new_conf is not c

    expected_python = os.path.join(".", "CONDA", "conda", "bin", "python")
    assert new_conf._python_path == expected_python
    # archive must be added tp the arguments that will be supplied.
    assert "hdfs://some/env/conda.zip#CONDA" in new_conf.archives
    assert os.environ["PYSPARK_PYTHON"] == expected_python
