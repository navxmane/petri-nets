from classes.place import Place
from classes.transition import Transition
from utils.parcer import str_parcer


places = []
transitions = []

def main():

    n_places = int(input("Enter number of places: "))
    n_transitions = int(input("Enter number of transitions: "))

    for i in range(n_places):
        places.append(Place(id=i))
    for i in range(n_transitions):
        transitions.append(Transition(id=i))

    print("Places:")
    print(" - ".join(str(place.get_id()) for place in places))

    print("\nTransitions:")
    print(" - ".join(str(transition.get_id()) for transition in transitions))


    for place in places:
        pre_place = input("Enter pre of transitions" + " of " + str(place.get_id()) + ": ")
        pre_transitions = str_parcer(pre_place)


if __name__ == "__main__":
    main()
