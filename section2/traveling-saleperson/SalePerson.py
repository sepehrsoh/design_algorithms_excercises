import time
import numpy as np


class SalePerson:
    def __init__(self, values):
        self.values = values
        self.length = len(values)

    def sale_person(self):
        all_points_set = set(range(self.length))

        # memo keys: tuple(sorted_points_in_path, last_point_in_path)
        # memo values: tuple(cost_thus_far, next_to_last_point_in_path)
        memo = {(tuple([i]), i): tuple([0, None]) for i in range(self.length)}
        queue = [(tuple([i]), i) for i in range(self.length)]

        while queue:
            prev_visited, prev_last_point = queue.pop(0)
            prev_dist, _ = memo[(prev_visited, prev_last_point)]

            to_visit = all_points_set.difference(set(prev_visited))
            for new_last_point in to_visit:
                new_visited = tuple(sorted(list(prev_visited) + [new_last_point]))
                new_dist = prev_dist + self.values[prev_last_point][new_last_point]

                if (new_visited, new_last_point) not in memo:
                    memo[(new_visited, new_last_point)] = (new_dist, prev_last_point)
                    queue += [(new_visited, new_last_point)]
                else:
                    if new_dist < memo[(new_visited, new_last_point)][0]:
                        memo[(new_visited, new_last_point)] = (new_dist, prev_last_point)

        optimal_path, optimal_cost = self.retrace_optimal_path(memo)
        return optimal_path, optimal_cost

    def retrace_optimal_path(self, memo: dict) -> [[int], float]:
        points_to_retrace = tuple(range(self.length))

        full_path_memo = dict((k, v) for k, v in memo.items() if k[0] == points_to_retrace)
        path_key = min(full_path_memo.keys(), key=lambda x: full_path_memo[x][0])

        last_point = path_key[1]
        print(memo[path_key])
        optimal_cost, next_to_last_point = memo[path_key]

        optimal_path = [last_point]
        points_to_retrace = tuple(sorted(set(points_to_retrace).difference({last_point})))

        while next_to_last_point is not None:
            last_point = next_to_last_point
            path_key = (points_to_retrace, last_point)
            _, next_to_last_point = memo[path_key]

            optimal_path = [last_point] + optimal_path
            points_to_retrace = tuple(sorted(set(points_to_retrace).difference({last_point})))

        return optimal_path, optimal_cost

    def solve(self):
        return self.sale_person()
