"""
MapsTool: generates Google Maps links (simple).
"""
class MapsTool:
    def __init__(self):
        pass

    def generate_link(self, lat: float, lng: float) -> str:
        if lat is None or lng is None:
            return "https://www.google.com/maps"
        return f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"
