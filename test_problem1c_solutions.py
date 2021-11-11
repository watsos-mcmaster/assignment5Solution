from time import sleep
from traffic_light_stubs import Intersection, MainTrafficLight, SideStreetTrafficLight

# this test comes back again, because the main road needs to be green by default
def test_1c_base_case():
    main_light = MainTrafficLight()

    assert main_light.colour() == "green", "Main street colour should be green by default"

# some traffic is waiting, but we don't want it to change until 90s have passed
def test_1c_light_stays_after_short_wait():
    main_light = MainTrafficLight()
    side_light = SideStreetTrafficLight()
    intersection = Intersection([main_light, side_light])

    # preconditions
    assert main_light.colour() == "green", "Main street colour should be green by default"

    side_light.set_traffic_present(True)
    # wait a couple of seconds, not nearly enough for the lights to change
    sleep(3)

    # postcondition
    assert main_light.colour() == "green", "Main street colour should be green by default"

def test_1c_light_changes_after_90s_wait():
    main_light = MainTrafficLight()
    side_light = SideStreetTrafficLight()
    intersection = Intersection([main_light, side_light])

    # precondition
    assert main_light.colour() == "green", "Main street colour should be green by default"

    side_light.set_traffic_present(True)
    # wait 90s, after this the light should change
    sleep(90)

    # postcondition
    assert main_light.colour() == "red", "Main street colour should be switched to red"

def test_1c_light_stays_red_when_traffic_remains():
    main_light = MainTrafficLight()
    side_light = SideStreetTrafficLight()
    side_light.set_traffic_present(True)
    intersection = Intersection([main_light, side_light])

    # precondition
    assert main_light.colour() == "red", "Main street colour should be red"

    side_light.set_traffic_present(False)
    #wait a couple of seconds, but not long enough for it to change
    sleep(3)

    # postcondition
    assert main_light.colour() == "red", "Main street colour should stay red"
    
def test_1c_light_turns_green_when_traffic_has_passed():
    main_light = MainTrafficLight()
    side_light = SideStreetTrafficLight()
    side_light.set_traffic_present(True)
    intersection = Intersection([main_light, side_light])

    # precondition
    assert main_light.colour() == "red", "Main street colour should be red"

    side_light.set_traffic_present(False)
    #wait for 30s after the traffic is gone
    sleep(30)

    # postcondition
    assert main_light.colour() == "green", "Main street colour should change to green"

