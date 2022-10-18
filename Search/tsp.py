import numpy as np
import random


def nearest(M, very_next_cities,current_city):
    """Return the index of the city which is closest to 'current'."""
    min_cost_city = very_next_cities[0]
    for next_city in very_next_cities:
        if M[current_city][next_city] < min_cost_city:
            min_cost_city = next_city
    return min_cost_city






#i) Re-start of greedy is correct (including choice of next city)
def random_backtrack(visited_cities,running_tour):
    random_backtrack_at = random.randint(0, max(0, (len(visited_cities) - 1)))
    if random_backtrack_at == 0:

        running_tour = [0]
        visited_cities = [0]
        current_city = random_backtrack_at
        avoid_city = 0
    else:
        running_tour = running_tour[:random_backtrack_at]
        avoid_city = visited_cities[random_backtrack_at]
        visited_cities = (visited_cities[:random_backtrack_at])
        current_city = random_backtrack_at - 1
    return visited_cities,running_tour,current_city,avoid_city







def get_tour(M,max_city_visits,start_city=0, current_city=0,visited_cities=[0],running_tour=[0],avoid_city=0,counter=1):
    counter += 1
    if(counter < max_city_visits):
        if len(running_tour) != len(M):
            #It then visits the city which is closest to city 1, say city 5.
            very_next_cities = [x for x in range(len(M)) if M[current_city][x] > 0 and x not in (visited_cities+[avoid_city])]


            if len(very_next_cities) != 0:
                #Then it visits the city closest to that (but does not go back to 1!), and so on.
                min_cost_city= nearest(M, very_next_cities,current_city)
                running_tour.append(min_cost_city)
                return get_tour(M,max_city_visits, start_city, min_cost_city, visited_cities + [min_cost_city],running_tour,current_city,counter)

            # If there is no next city: how will the algorithm tell that greedy search is not returning a tour? I.e. when does it decide to backtrack?
            #1. If we reach a dead city without outgoing paths
            else:
                new_visited_cities, new_running_tour,new_current_city, new_avoid_city=random_backtrack(visited_cities,running_tour)
                return get_tour(M, max_city_visits,start_city,  new_current_city, new_visited_cities, new_running_tour, new_avoid_city,counter)

        else:
        #how will the algorithm tell that greedy search is not returning a tour? I.e. when does it decide to backtrack?
        #2.f cannot go back to start city:


            if M[current_city][start_city] > 0:
            # If doing this returns a tour, great, we're done. Else, we have to backtrack.
              running_tour= running_tour + [start_city]


            else:
                new_visited_cities, new_running_tour, new_current_city, new_avoid_city = random_backtrack(visited_cities, running_tour)
                return get_tour(M, max_city_visits, start_city, new_current_city, new_visited_cities, new_running_tour, new_avoid_city,counter)
        return running_tour
    else:
        print("Could not find a path in: ", max_city_visits ," iterations")
        return []






def evaluate_path(M, tour):
    tour_cost = 0
    for i in range(len(tour) - 1):
        # print(M[i-1][i])
        tour_cost += M[tour[i]][tour[i + 1]]
    # print(tour_cost)
    return float(tour_cost)



def check_if_tour_exists(M):
    blocked_paths = 0
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] < 0:
                blocked_paths += 1
        if (blocked_paths == len(M)):   # if all paths=blocked paths for a city
            print("This matrix does not contain any tours")
            exit()

def tsp(M,K):
    check_if_tour_exists(M)
    tour=get_tour(M, start_city=0, current_city=0, visited_cities=[0],running_tour=[0],avoid_city=0,counter=0,max_city_visits=K)
    print(tour)
    print("Cost of Tour: ",evaluate_path(M,tour))


if __name__ == '__main__':
    #
    # M = [[-1, 3, 2, 1, 3],
    #      [3, -1, 1, -1, 1],
    #      [2, 1, -1, 4, 4],
    #      [1, -1, 4, -1, 2],
    #      [3, 1, 4, 2, -1]]
    #
    M = [
        [-1, 1, 1],
        [1, -1, 4],
        [-1, 1, -1]]
    K=15
    tsp(M,K)