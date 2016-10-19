import random

from numpy import percentile, round, average


class Results(object):
    def __init__(self, results):
        self.results = results

    def percentile(self, pct):
        return int(round(percentile(self.results, pct)))


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
            time_unit_count = 1
            while simulated_backlog > 0:
                simulated_backlog -= random.choice(throughputs)
                time_unit_count += 1
            results.append(time_unit_count)

        return Results(results)

    def forecast_avg(self, throughputs, backlog_size):
        return backlog_size / average(throughputs)
