class Intersection:
    def __init__(self, lights):
        self.lights = lights

    def switch_colours(self):
        return None


class TrafficLight:
    def colour(self):
        return None

    def walk_permitted(self):
        return None


class MainTrafficLight(TrafficLight):
    # we are generating an empty class here
    pass


class SideStreetTrafficLight(TrafficLight):
    def set_traffic_present(self, is_traffic_present):
        return None

    def traffic_wait_time(self):
        return None

    def traffic_light_green_time(self):
        return None