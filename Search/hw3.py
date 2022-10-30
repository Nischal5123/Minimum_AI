import numpy as np
import random

# M = [[-1, 3, 2, 1, 3],
#      [3, -1, 1, -1, 1],
#      [2, 1, -1, 4, 4],
#      [1, -1, 4, -1, 2],
#      [3, 1, 4, 2, -1]]

M = [
     [-1, 1, 3],
     [1, -1, 4],
     [-1, 1, -1]]

# M = [[-1, 1],
#      [3, -1]]



def all_tours(M, start_city=0, current_city=0,visited_cities=[],res_path=[0],avoid_city=0):
    if len(res_path) != len(M):
        #It then visits the city which is closest to city 1, say city 5.
        very_next_cities = [x for x in range(len(M)) if M[current_city][x] > 0 and x not in (visited_cities+[avoid_city])]

        if len(very_next_cities) != 0:
            #Then it visits the city closest to that (but does not go back to 1!), and so on.
            min_cost_city= nearest(M, very_next_cities,current_city)
            res_path.append(min_cost_city)
            return all_tours(M, start_city, min_cost_city, visited_cities + [min_cost_city],res_path)


        else:
            avoid_city = current_city
            random_backtrack_at = random.randint(0, max(0, (len(visited_cities) - 1)))
            if random_backtrack_at == 0:

                res_path = [0]
                visited_cities = [0]
                current_city = random_backtrack_at
            else:
                res_path = res_path[:random_backtrack_at]
                visited_cities = (visited_cities[:random_backtrack_at])
                current_city = random_backtrack_at - 1
            return all_tours(M, start_city, current_city, visited_cities, res_path, avoid_city)




        # temp_res_paths = all_tours(M, start_city, min_cost_city, visited_cities + [min_cost_city])
        #
        # for very_next_city in very_next_cities:
        #     #Then it visits the city closest to that (but does not go back to 1!), and so on.
        #     #doesn't go back to current city or very_next_city
        #     temp_res_paths = all_tours(M, start_city, very_next_city, visited_cities + [very_next_city])
        #     for path in temp_res_paths:
        #         res_paths.append([current_city] + path)
        # return res_paths


    else:
        #how will the algorithm tell that greedy search is not returning a tour? I.e. when does it decide to backtrack?

    #check to make sure only tours ie path that finishes in the start city are included
        if M[current_city][start_city] > 0:
          res_path= res_path + [start_city]
        else:
            avoid_city=current_city
            random_backtrack_at = random.randint(0, max(0,(len(visited_cities) - 1)))
            if random_backtrack_at == 0:

                res_path = [0]
                visited_cities = [0]
                current_city=random_backtrack_at
            else:
                res_path = res_path[:random_backtrack_at]
                visited_cities = (visited_cities[:random_backtrack_at])
                current_city = random_backtrack_at - 1
            return all_tours(M, start_city, current_city, visited_cities, res_path, avoid_city)



    return res_path


# res_paths = all_tours(M, start_city=0,current_city=0,visited_cities=[0])
# print(res_paths)


cooling = 0.1
K = 100

#d) Given a tour generated from matrix M, how do you compute its cost? (If this question feels easy, it is)
def evaluate_path(M, tour):
    tour_cost = 0
    for i in range(len(tour) - 1):
        # print(M[i-1][i])
        tour_cost += M[tour[i + 1]][tour[i]]
    # print(tour_cost)
    return tour_cost

def nearest(M, very_next_cities,current_city):
    """Return the index of the node which is closest to 'last'."""
    # find minimum cost city
    min_cost_city = very_next_cities[0]
    for next_city in very_next_cities:
        if M[current_city][next_city] < min_cost_city:
            min_cost_city = M[current_city][next_city]
    return min_cost_city


def nearest_neighbor(n, i, D):
    """Return tour starting from city 'i', using the Nearest Neighbor.

    Uses the Nearest Neighbor heuristic to construct a solution:
    - start visiting city i
    - while there are unvisited cities, follow to the closest one
    - return to city i
    """
    unvisited = [x for x in range(len(M))]
    unvisited.remove(i)
    last = i
    tour = [i]
    while unvisited != []:
        next = nearest(last, unvisited, D)
        tour.append(next)
        unvisited.remove(next)
        last = next
    return tour

def tsp(M, K):


    #e) Just in case your algorithm gets a matrix M that does not contain any tours (e.g., it is not possible to come back to the starting city 1),
    # it's a good idea to be able to detect that and output some message like "This matrix does not contain any tours" before you attempt to find non-existent tours. How do you detect that?



    for i in range(len(M)):
        a=0
        for j in range(len(M)):
            if M[i][j] < 0:
                a += 1
        if (a == len(M)):
            print("This matrix does not contain any tours")
            exit()

       ##########################################################

    else:
        T_init = 30
        factor = 0.99
        T = T_init * factor
        print(len(M))
       # tour=nearest_neighbor(len(M),0,M)
        tour=all_tours(M, start_city=0, current_city=0, visited_cities=[0],res_path=[0])

        index_shortest_tour = random.randint(0, len(res_paths) - 1)
        shortest_tour = res_paths[index_shortest_tour]
        cost_shortest_tour = evaluate_path(M, shortest_tour)

        for iteration in range(K):
            T = T * factor

            index_now_tour = random.randint(0, len(res_paths) - 1)
            now_path = res_paths[index_now_tour]
            cost_now_tour = evaluate_path(M, now_path)

            if cost_now_tour < cost_shortest_tour:
                shortest_tour = now_path
                cost_shortest_tour = cost_now_tour
            else:
                P = np.exp(-(cost_now_tour - cost_shortest_tour) / T)
                flip_coin = random.uniform(0, 1)
                if flip_coin < P:
                    shortest_tour = now_path
                    cost_shortest_tour = cost_now_tour
        #print(shortest_tour, cost_shortest_tour)
        return shortest_tour, cost_shortest_tour


print(tsp(M, 500))

#print(evaluate_path(M, [0, 4, 1, 3, 2, 0]))
