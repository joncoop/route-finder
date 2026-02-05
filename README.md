# Route Finder (Shortest Path)

This program finds the shortest route between two cities using a weighted graph and a priority queue.  
It is an implementation of Dijkstra’s algorithm written in Python.

The city map and distances are loaded from a JSON file. The user selects a starting city and a destination city at runtime.


## Files

- **route_finder.py**  
  Contains all classes and logic for building the map and finding routes.

- **map.json**  
  A JSON file that defines cities and their neighboring cities with distances.


## The Map

The map used for this project was created and visualized in Desmos:

**Map link:**  
https://www.desmos.com/geometry/x50j7pctii


### Relationship to U.S. Interstates

This map is an approximation of the U.S. interstate highway system, not an exact model.

- In regions where many interstates run close together, some routes were removed or merged to reduce complexity.
- Connections are often approximated so cities link only to the most major nearby cities, rather than every possible interchange.
- When an interstate passes near a city, intersections were sometimes modeled as occurring directly at that city, even if the real interstate bypasses it.
- Distances are approximate and intended for experimentation, not real-world navigation.


### Map Format (`map.json`)

```json
{
  "CityA": {
    "neighbors": [
      {"name": "CityB", "distance": 5},
      {"name": "CityC", "distance": 10}
    ]
  },
  "CityB": {
    "neighbors": [
      {"name": "CityA", "distance": 5}
    ]
  }
}
```

- Each city has a list of neighbors.
- Distances are assumed to be in miles.
- Connections are directional unless explicitly added both ways. (This is intentional so that the map can be adapted to other contexts. For example, we could use this for flight times or flight costs between cities which may not be symmetric.)
