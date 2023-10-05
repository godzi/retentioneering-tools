import os

import pandas as pd
import pytest

from retentioneering.eventstream import Eventstream


def read_test_data(filename):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    test_data_dir = os.path.join(current_dir, "../../../datasets/tooling/stattests")
    filepath = os.path.join(test_data_dir, filename)
    source_df = pd.read_csv(filepath, index_col=0)
    return source_df


@pytest.fixture
def test_stream():
    source_df = read_test_data("01_simple_data.csv")
    source_stream = Eventstream(source_df)
    return source_stream
