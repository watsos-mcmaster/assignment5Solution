from traffic_light_stubs import Intersection, MainTrafficLight, SideStreetTrafficLight

# note that these tests are almost identical to the tests for part A
def test_1b_base_case():
    main_light = MainTrafficLight()

    assert main_light.colour() == "green", "Main street colour should be green by default"
    assert main_light.walk_permitted(), "Main street walk signal should be enabled on a green light"

def test_1b_transition():
    main_light = MainTrafficLight()
    side_light = SideStreetTrafficLight()
    intersection = Intersection([main_light, side_light])
    # precondition
    assert main_light.colour() == "green", "Main street colour should be green by default"
    assert main_light.walk_permitted(), "Main street walk signal should be enabled on a green light"

    intersection.switch_colours()

    # postcondition
    assert main_light.colour() == "red", "Main street colour should be switched to red"
    assert not main_light.walk_permitted(), "Main street walk signal should be disabled on a red light"

def test_1b_changing_walk_signal_fails():
    main_light = MainTrafficLight()
    # precondition
    assert main_light.colour() == "red", "Main street colour should be initialized to red"
    assert not main_light.walk_permitted(), "Main street walk signal should be disabled on a red light"

    main_light.walk_permitted_value = True

    #postcondition
    assert not main_light.walk_permitted(), "Main street walk signal should remain disabled on a red light"

