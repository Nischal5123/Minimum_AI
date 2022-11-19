import numpy as np
import random
import sys


# implementation of greedy
def get_nearest_city(M, very_next_cities, current_city):
    """
    get_nearest_city gets the nearest city to current city

    :param M: matrix of cities
    :param very_next_cities: reachable next cities
    :param current_city: current city
    :return: city with the minimum cost to visit
    """

    min_cost_city = very_next_cities[0]
    for next_city in very_next_cities:
        if M[current_city][next_city] < min_cost_city:
            min_cost_city = next_city
    return min_cost_city


# i) Re-start of greedy is correct (including choice of next city)
def random_backtrack(visited_cities, running_tour):

    """
    random_backtrack does a random backtrack to a previous city

    :param visited_cities: previously visited cities
    :param running_tour: tour so far
    :return: updated visited_cities, running_tour, current_city, avoid_city(city that made us backtrack)
    """
    random_backtrack_at = random.randint(0, max(0, (len(visited_cities) - 1)))
    if random_backtrack_at == 0:

        running_tour = [0]
        visited_cities = [0]
        current_city = random_backtrack_at
        avoid_city = 0
    else:
        running_tour = running_tour[:random_backtrack_at]
        avoid_city = visited_cities[
            random_backtrack_at
        ]  # but of course we now exclude whatever city we had visited previously on the previous attempt. Thus we exclude c(k+1), and pick the closest city to c(k) out of the remaining neighbors
        visited_cities = visited_cities[:random_backtrack_at]
        current_city = random_backtrack_at - 1
    return visited_cities, running_tour, current_city, avoid_city


def get_tour(
    M,
    max_city_visits,
    start_city=0,
    current_city=0,
    visited_cities=[0],
    running_tour=[0],
    avoid_city=0,
    counter=1,
):
    """
    random_backtrack does a random backtrack to a previous city
     :param M: matrix of cities
     :param max_city_visits: K
     :param start_city: City to start the tour from
     :param current_city: current city
    :param visited_cities: previously visited cities
    :param running_tour: tour so far
     :param avoid_city(city that made us backtrack)
    :return: random greedy tour based on the Matrix M
    """
    counter += 1
    if counter < max_city_visits:  # Checks maximum nb of computations
        if len(running_tour) != len(M):
            # It then visits the city which is closest to city 1, say city 5.

            valid_neighbors = [
                x
                for x in range(len(M))
                if M[current_city][x] > 0 and x not in (visited_cities + [avoid_city])
            ]

            if len(valid_neighbors) != 0:
                # Then it visits the city closest to that (but does not go back to 1!), and so on.
                min_cost_city = get_nearest_city(M, valid_neighbors, current_city)
                running_tour.append(min_cost_city)
                return get_tour(
                    M,
                    max_city_visits,
                    start_city,
                    min_cost_city,
                    visited_cities + [min_cost_city],
                    running_tour,
                    current_city,
                    counter,
                )

            # If there is no next city: how will the algorithm tell that greedy search is not returning a tour? I.e. when does it decide to backtrack?
            # 1. If we reach a dead city without outgoing paths
            else:
                (
                    new_visited_cities,
                    new_running_tour,
                    new_current_city,
                    new_avoid_city,
                ) = random_backtrack(
                    visited_cities, running_tour
                )  # Decision to backtrack
                return get_tour(
                    M,
                    max_city_visits,
                    start_city,
                    new_current_city,
                    new_visited_cities,
                    new_running_tour,
                    new_avoid_city,
                    counter,
                )

        else:
            # how will the algorithm tell that greedy search is not returning a tour? I.e. when does it decide to backtrack?
            # 2.f cannot go back to start city:

            if M[current_city][start_city] > 0:
                # If doing this returns a tour, great, we're done. Else, we have to backtrack.
                running_tour = running_tour + [start_city]

            else:
                (
                    new_visited_cities,
                    new_running_tour,
                    new_current_city,
                    new_avoid_city,
                ) = random_backtrack(
                    visited_cities, running_tour
                )  # Decision to backtrack
                return get_tour(
                    M,
                    max_city_visits,
                    start_city,
                    new_current_city,
                    new_visited_cities,
                    new_running_tour,
                    new_avoid_city,
                    counter,
                )
        print("Counter: ", counter)
        return running_tour
    else:
        print(
            "Could not find a path in: ", max_city_visits, " iterations"
        )  # Checks maximum nb of computations
        return []


def evaluate_path(M, tour):
    """
    get tour cost
     :param M: matrix of cities
     :param tour: tour list
    :return: cost of tour
    """
    tour_cost = 0
    if len(tour) == 0:
        return float("inf")
    else:
        for i in range(len(tour) - 1):
            # print(M[i-1][i])
            tour_cost += M[tour[i]][tour[i + 1]]
        # print(tour_cost)
        return float(tour_cost)


# to avoid running tsp
def check_if_unvisitable_city(M):
    """
    check if unvisitable city
     :param M: matrix of cities
    :return: boolean yes or no
    """
    for i in range(len(M)):
        blocked_paths = 0
        for j in range(len(M)):
            if M[j][i] < 0:
                blocked_paths += 1
        if blocked_paths == len(M):  # if all paths=blocked paths for a city
            print("This matrix has a unvisitable  city")
            return 1

    return 0


## to avoid running tsp
def check_if_dead_city(M):
    """
    check if dead city
     :param M: matrix of cities
    :return: boolean yes or no
    """
    for i in range(len(M)):
        blocked_paths = 0
        for j in range(len(M)):
            if M[i][j] < 0:
                blocked_paths += 1
        if blocked_paths == len(M):  # if all paths=blocked paths "from" a city
            print("This matrix has a dead node city")
            return 1
    return 0


# to avoid running tsp
def check_if_no_tour_exists(M):
    """
    check if can visit start city
     :param M: matrix of cities
    :return: boolean yes or no
    """
    no_way_home = 0
    for i in range(len(M)):
        if M[i][0] < 0:
            no_way_home += 1
    if no_way_home == len(M):  # if home city is not reachable from all cities in M
        print("This matrix has no way to return to start city")
        return 1
    else:
        return 0


# The signature of your function should be:

# [optimal_tour, optimal_value] = tsp(M, K)


def tsp(M, K):

    """
    run tsp
     :param M: matrix of cities
    :param K: max number of cities to visit with repetition
    :return: [ tour list, cost of tour]
    """

    # e) Just in case your algorithm gets a matrix M that does not contain any t
    # #ours (e.g., it is not possible to come back to the starting city 1), it's a good idea to be able to detect that and output some message like
    # "This matrix does not contain any tours" before you attempt to find non-existent tours. How do you detect that?

    if (
        check_if_no_tour_exists(M)
        or check_if_unvisitable_city(M)
        or check_if_dead_city(M)
    ):
        return [[], float("inf")]

    else:
        # Assuming 0 is start city

        tour = get_tour(
            M,
            start_city=0,
            current_city=0,
            visited_cities=[0],
            running_tour=[0],
            avoid_city=0,
            counter=0,
            max_city_visits=K,
        )
        cost = evaluate_path(M, tour)
        print("Tour: ", tour)
        print("Cost of Tour: ", cost)
        return [tour, cost]


if __name__ == "__main__":

    M = [[-1, 1, -1, 2, -1], [1, -1, 4, 1, 8], [-1, 4, -1, 10, 5], [2, 1, 10, -1, 100], [-1, 8, 5, 100, -1]]
    K = 1000
    print(tsp(M, K))
