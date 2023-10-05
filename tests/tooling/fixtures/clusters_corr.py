import pandas as pd
import pytest

from retentioneering import datasets


@pytest.fixture
def markov_corr() -> pd.DataFrame:
    correct_columns = [
        "event1~event1",
        "event1~event2",
        "event1~event3",
        "event1~event4",
        "event2~event1",
        "event2~event2",
        "event3~event1",
    ]
    correct_columns = [c + "_markov" for c in correct_columns]
    index = pd.Index([1, 2, 3, 4], name="user_id")
    correct_features = pd.DataFrame(
        [
            [0.4, 0.2, 0.4, 0.0, 1.0, 0.0, 1.0],
            [0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0],
            [0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0],
            [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        ],
        columns=correct_columns,
        index=index,
    )
    return correct_features


@pytest.fixture
def kmeans_corr() -> pd.Series:
    d = {1: 0, 2: 1, 3: 0, 4: 0}
    index = pd.Index([1, 2, 3, 4], name="user_id")
    corr = pd.Series(data=d, index=index)
    return corr


@pytest.fixture
def gmm_corr() -> pd.Series:
    d = {1: 0, 2: 0, 3: 1, 4: 0}
    index = pd.Index([1, 2, 3, 4], name="user_id")
    corr = pd.Series(data=d, index=index)
    return corr


@pytest.fixture
def count_corr() -> pd.DataFrame:
    correct_columns = ["event1", "event2", "event3", "event4"]
    correct_columns = [c + "_count" for c in correct_columns]
    index = pd.Index([1, 2, 3, 4], name="user_id")
    correct_features = pd.DataFrame(
        [
            [6, 1, 2, 0],
            [1, 2, 0, 0],
            [2, 0, 0, 1],
            [3, 0, 0, 0],
        ],
        columns=correct_columns,
        index=index,
    )
    return correct_features


@pytest.fixture
def time_corr() -> pd.DataFrame:
    correct_columns = ["event1", "event2", "event3", "event4"]
    correct_columns = [c + "_time" for c in correct_columns]
    index = pd.Index([1, 2, 3, 4], name="user_id")
    correct_features = pd.DataFrame(
        [
            [122.0, 58.0, 60.0, 0.0],
            [5.0, 60.0, 0.0, 0.0],
            [115.0, 0.0, 0.0, 0.0],
            [115.0, 0.0, 0.0, 0.0],
        ],
        columns=correct_columns,
        index=index,
    )
    return correct_features


@pytest.fixture
def time_fraction_corr() -> pd.DataFrame:
    correct_columns = ["event1", "event2", "event3", "event4"]
    correct_columns = [c + "_time_fraction" for c in correct_columns]
    index = pd.Index([1, 2, 3, 4], name="user_id")
    correct_features = pd.DataFrame(
        [
            [0.508, 0.242, 0.25, 0.0],
            [0.077, 0.923, 0.0, 0.0],
            [1.0, 0.0, 0.0, 0.0],
            [1.0, 0.0, 0.0, 0.0],
        ],
        columns=correct_columns,
        index=index,
    )
    return correct_features


@pytest.fixture
def cluster_mapping_corr() -> dict:
    corr = {0: [1, 2, 4], 1: [3]}
    return corr


@pytest.fixture
def ngram_range_corr() -> pd.DataFrame:
    correct_columns = [
        "event1 event1 event1",
        "event1 event1 event3",
        "event1 event1 event4",
        "event1 event2 event1",
        "event1 event2 event2",
        "event1 event3 event1",
        "event2 event1 event1",
        "event3 event1 event3",
    ]
    correct_columns = [c + "_count" for c in correct_columns]
    index = pd.Index([1, 2, 3, 4])
    correct_features = pd.DataFrame(
        [
            [1, 1, 0, 1, 0, 2, 1, 1],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
        ],
        columns=correct_columns,
        index=index,
    )
    return correct_features


@pytest.fixture
def set_clusters_corr() -> dict:
    corr = {0: [3], 1: [1], 2: [4], 3: [2]}
    return corr


@pytest.fixture
def X_corr() -> pd.Series:
    d = {1: 0, 2: 1, 3: 1, 4: 1}
    index = pd.Index([1, 2, 3, 4])
    corr = pd.Series(data=d, index=index)
    return corr


@pytest.fixture
def cluster_bar_values_corr() -> pd.DataFrame:
    corr = pd.DataFrame(
        [
            [0, "CR: event1", 1],
            [0, "CR: event3", 0.33333],
            [0, "cluster_size", 0.75],
            [1, "CR: event1", 1],
            [1, "cluster_size", 0.25],
        ],
        columns=["cluster_id", "metric", "value"],
    )
    return corr
