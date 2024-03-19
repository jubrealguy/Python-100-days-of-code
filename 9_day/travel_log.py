travel_logs = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

def add_new_country(country, visits, cities):
    item = {}
    item["country"] = country
    item["visits"] = visits
    item["cities"] = cities
    travel_logs.append(item)

add_new_country("Russia", 6, ["Moscow", "Zenith"])

print(travel_logs)