from datasetOrbit import datasetOrbit
from orbitCalcs import SimpleOrbit

def main():
    # Example usage of ClassA and ClassB
    dataset_orbit = datasetOrbit(plot_title="Test", name="Earth")
    print(dataset_orbit)

    simple_orbit = SimpleOrbit(plot_title="Test", name="Earth")
    print(simple_orbit)

if __name__ == '__main__':
    main()