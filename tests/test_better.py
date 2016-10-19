import pytest


@pytest.fixture
def mut():
    """Returns the module under test."""
    from better import lib
    return lib


def test_results_percentile(mut):
    """Ensure the Results.percentile function returns the right value."""
    Results = mut.Results
    r = Results([
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10
    ])

    assert r.percentile(50.0) == 6
