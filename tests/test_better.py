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

    assert r.percentile(50.0) == 5


def test_forecast_average(mut):
    throughputs = [2, 2, 2, 2]
    backlog_size = 2 * 5

    result = mut.Forecaster().forecast_avg(throughputs, backlog_size)  # Fix the seed so we get predictable results
    assert result == 5


def test_forecast_sanity(mut):
    """With a uniform historical distribution, we should get the same result for all percentiles."""
    throughputs = [2, 2, 2, 2]
    backlog_size = 2 * 5

    result = mut.Forecaster().forecast(throughputs, backlog_size, seed=1)

    assert result.percentile(50.0) == 5
