import json
import heapq

# Map used: https://www.desmos.com/geometry/x50j7pctii

class Neighbor:
    def __init__(self, city, distance):
        self.city = city
        self.distance = distance


class City:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, neighbor_city, distance):
        self.neighbors.append(Neighbor(neighbor_city, distance))


class RouteFinder:
    
    def __init__(self, map_data):
        with open(map_data, 'r') as f:
            data = json.load(f)
        self.build_map(data)

    def build_map(self, data):
        self.cities = {}

        for city_name in data.keys():
            self.cities[city_name] = City(city_name)

        for city_name, info in data.items():
            for neighbor in info["neighbors"]:
                neighbor_city = self.cities[neighbor["name"]]
                distance = neighbor["distance"]
                self.cities[city_name].add_neighbor(neighbor_city, distance)

    def find_shortest_route(self, start_city, end_city):
        counter = 0  # Tie-breaker

        pq = [(0, counter, start_city, [])]
        costs = {start_city: 0}

        while pq:
            cost, _, city, path = heapq.heappop(pq)
            path = path + [city]

            if city == end_city:
                return [c.name for c in path], cost

            for neighbor in city.neighbors:
                next_city = neighbor.city
                new_cost = cost + neighbor.distance

                if next_city not in costs or new_cost < costs[next_city]:
                    costs[next_city] = new_cost
                    counter += 1
                    heapq.heappush(pq, (new_cost, counter, next_city, path))

        return None, None

    def select_route(self):
        begin = input("Enter the starting city: ")
        end = input("Enter the destination city: ")

        starting_city = self.cities.get(begin)
        destination_city = self.cities.get(end)

        if starting_city is None or destination_city is None:
            print("Invalid city entered.")
            return

        route, total_distance = self.find_shortest_route(starting_city, destination_city)

        if route is None:
            print("No route found.")
            return

        print("Shortest route:")
        print(" -> ".join(route))
        print(f"Total distance: {total_distance} miles")


def main():
    map_data = 'map.json'
    route_finder = RouteFinder(map_data)
    route_finder.select_route()

    
if __name__ == "__main__":
    main()
