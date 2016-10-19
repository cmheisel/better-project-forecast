import random

from numpy import percentile, round, average


class Results(object):
    def __init__(self, results):
        self.results = results

    def percentile(self, pct):
        """What's the Xth percentile of the results.
        Arguments:
            pct(float): The percentile you'd like returned.
                Percentile to compute, which must be between 0 and 100 inclusive.
                Example: 50.0 == 50th percentile.
        Returns:
            int: The value from the results that that is at the percentile requested.
        """
        return percentile(self.results, pct, interpolation='nearest')


class Forecaster(object):
    def forecast(self, throughputs, backlog_size, num_simulations=10000, seed=None):
        """Forecasts how long a backlog will take to complete given the historical values provided.
        Arguments:
            throughputs(List[int]): Number of units completed per unit of time (stories per week, story points per month, etc.)
            backlog_size(int): Units in the backlog (stories, points, etc.)
        Returns:
            results
        Exceptions:
            None
        """
        results = []

        if seed is not None:
            random.seed(seed)

        for i in range(0, num_simulations):
            simulated_backlog = backlog_size
            time_unit_count = 0
            while simulated_backlog > 0:
                simulated_backlog -= random.choice(throughputs)
                time_unit_count += 1
            results.append(time_unit_count)

        return Results(results)

    def forecast_avg(self, throughputs, backlog_size):
        return backlog_size / average(throughputs)
