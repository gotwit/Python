class Airport:
    def __init__(self, airport):
        self.airport = airport  # Nodes / Vertices
        self.isReachable = True
        self.connections = []  # Edges
        self.unreachableConnections = []


def airportConnections(airports, routes, startingAirport):
    airportGraph = createAirportGraph(airports, routes)
    unreachableAirportNodes = getUnreachableAirportNodes(
        airportGraph, airports, startingAirport)
    markUnreachableConnections(airportGraph, unreachableAirportNodes)
    return getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes, startingAirport)


def createAirportGraph(airports, routes):
    airportGraph = {}

    for airport in airports:
        airportGraph[airport] = Airport(airport)

    for route in routes:
        # unpack Start Airport, Destination/ Connection Airport.
        airport, connection = route
        airportGraph[airport].connections.append(connection)  # Adjacency list
    return airportGraph


def getUnreachableAirportNodes(airportGraph, airports, startingAirport):
    visistedAirports = {}
    depthFirstTraversalAirports(
        airportGraph, startingAirport, visistedAirports)

    unreachableAirportNodes = []
    for airport in airports:
        if airport in visistedAirports:
            continue
        airportNode = airportGraph[airport]
        airportNode.isReachable = False
        unreachableAirportNodes.append(airportNode)
    return unreachableAirportNodes


def depthFirstTraversalAirports(airportGraph, airport, visitedAirports):
    if airport in visitedAirports:
        return
    visitedAirports[airport] = True
    connections = airportGraph[airport].connections

    for connection in connections:
        depthFirstTraversalAirports(airportGraph, connection, visitedAirports)


def markUnreachableConnections(airportGraph, unreachableAirportNodes):
    for airportNode in unreachableAirportNodes:
        airport = airportNode.airport
        unreachableConnections = []
        depthFirstAddUnreachableConnections(
            airportGraph, airport, unreachableConnections, {})
        airportNode.unreachableConnections = unreachableConnections


def depthFirstAddUnreachableConnections(airportGraph, airport, unreachableConnections, visitedAirports):
    if airportGraph[airport].isReachable:
        return
    if airport in visitedAirports:
        return
    visitedAirports[airport] = True
    unreachableConnections.append(airport)
    connections = airportGraph[airport].connections
    for connection in connections:
        depthFirstAddUnreachableConnections(
            airportGraph, connection, unreachableConnections, visitedAirports)


def getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes, startingAirport):
    unreachableAirportNodes.sort(key=lambda airport: len(
        airport.unreachableConnections), reverse=True)
    
    numberOfNewConnections = []
    numberOfRoutes = 0
    newConnections = {
        
    }

    for airportNode in unreachableAirportNodes:
        if airportNode.isReachable:
            continue

        numberOfRoutes += 1
        numberOfNewConnections.append([startingAirport, airportNode.airport])
        for connection in airportNode.unreachableConnections:
            airportGraph[connection].isReachable = True
    newConnections = {"routes":numberOfRoutes, "connections":numberOfNewConnections}
    return newConnections

if __name__ == "__main__":
    airports = [
        "BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN",
        "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD",
    ]

    routes = [
        ["DSM", "ORD"],
        ["ORD", "BGI"],
        ["BGI", "LGA"],
        ["SIN", "CDG"],
        ["CDG", "SIN"],
        ["CDG", "BUD"],
        ["DEL", "DOH"],
        ["DEL", "CDG"],
        ["DEL", "SIN"],  # Added missing connection
        ["TLV", "DEL"],
        ["EWR", "HND"],
        ["HND", "ICN"],
        ["HND", "JFK"],
        ["ICN", "JFK"],
        ["JFK", "LGA"],
        ["EYW", "LHR"],
        ["LHR", "SFO"],
        ["SFO", "SAN"],
        ["SFO", "DSM"],
        ["SAN", "EYW"],
    ]

    startingAirport = "LGA"

    result = airportConnections(airports, routes, startingAirport)
    print(f"Airport connections: {result}\n")
