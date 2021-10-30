def calculate_result(max_flow, min_cut, start, end):
    print()
    print("Flights to advertise:")
    for edge in min_cut:
        print(f"\t{edge}")

    print()
    print(f"Maximum number of passengers that can go from {start} to {end}: {max_flow}")
