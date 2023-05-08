def fare_calculator(distance_km):
    """Calculates a taxi fare that has a base cost of 4 dollars
    and costs an extra 25 cents every 140 meters."""
    #Base fare
    BASE_FARE = 4.0
    #converts km distance to m
    distance_m = distance_km*1000
    #Calculates the additional fare at a rate of 0.25 per 140 meters and rounds that to the nearest 2 decimals.
    fare_meter_addition = round((distance_m/140)*0.25, 2)
    #Calculates total fare cost
    fare_cost = BASE_FARE + fare_meter_addition
    #prints how much the inputted distance would cost in fare.
    print(f"${fare_cost}")

fare_calculator(1)