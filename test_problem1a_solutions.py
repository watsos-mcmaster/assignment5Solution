from traffic_light_stubs import Intersection, MainTrafficLight, SideStreetTrafficLight

def test_1a_base_case():
    main_light = MainTrafficLight()
    side_light = SideStreetTrafficLight()

    assert main_light.colour() == "green", "Main street colour should be green by default"
    assert side_light.colour() == "red", "Side street light should be red by default"

def test_1a_transition():
    main_light = MainTrafficLight()
    side_light = SideStreetTrafficLight()
    intersection = Intersection([main_light, side_light])
    # precondition
    assert main_light.colour() == "green", "Main street colour should be green by default"
    assert side_light.colour() == "red", "Side street light should be red by default"

    intersection.switch_colours()

    # postcondition
    assert main_light.colour() == "red", "Main street colour should be switched to red"
    assert side_light.colour() == "green", "Side street light should be switched to green"

def test_1a_changing_one_light_fails():
    main_light = MainTrafficLight()
    # precondition
    assert main_light.colour() == "green", "Main street colour should be green by default"

    main_light.colour_value = "red"

    #postcondition
    assert main_light.colour() == "green", "Main street colour should be changeable on its own"
