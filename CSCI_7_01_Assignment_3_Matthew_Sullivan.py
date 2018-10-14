import math

replay = "y"
while (replay == "y"):
    capacity_limit = 500
    fixed_cost = 2500
    minimum_capacity = abs(int(input("\n\t1 of 3 - Enter the minimum number of passengers: ")))
    maximum_capacity = abs(int(input("\t2 of 3 - Enter the maximum number of passengers: ")))
    proposed_ticket_price = float(input("\t3 of 3 - Enter the Ticket Price: "))

    while minimum_capacity >= capacity_limit or maximum_capacity > capacity_limit or minimum_capacity >= maximum_capacity:
        if minimum_capacity >= capacity_limit:
            minimum_capacity = abs(int(input("\n\tPlease re-enter a minimum number of passengers less than 500 and less than your maximum number of passengers: ")))
        elif maximum_capacity > capacity_limit:
            maximum_capacity = abs(int(input("\n\tPlease re-enter a maximum number of passengers less than 500 but greater than your minimum number of passengers: ")))
        elif minimum_capacity >= maximum_capacity:
            minimum_capacity = abs(int(input("\n\tPlease re-enter a minimum number of passengers less than your maximum number of passengers: ")))
            maximum_capacity = abs(int(input("\n\tPlease re-enter a maximum number of passengers greater than your minimum number of passengers: ")))
        elif minimum_capacity >= capacity_limit and minimum_capacity >= maximum_capacity:
            minimum_capacity = abs(int(input("\n\tPlease re-enter a minimum number of passengers less than 500 and your maximum number of passengers: ")))
            maximum_capacity = abs(int(input("\n\tPlease re-enter a maximum number of passengers greater than your minimum number of passengers and less than or equal to 500: ")))
        elif maximum_capacity > capacity_limit and minimum_capacity >= maximum_capacity:
            minimum_capacity = abs(int(input("\n\tPlease re-enter a minimum number of passengers less than 500 and your maximum number of passengers: ")))
            maximum_capacity = abs(int(input("\n\tPlease re-enter a maximum number of passengers greater than your minimum number of passengers and less than or equal to 500: ")))

    while proposed_ticket_price < 0:
        proposed_ticket_price = float(input("\tPlease re-enter your proposed ticket price: "))


    print("\n\tPassenger Run from %d to %d with an initial ticket price of $%.2f with a fixed cost of $%.2f. \n\tDiscount per ticket of $0.50 for each group of 10 baove the starting count of %d passengers."% (minimum_capacity, maximum_capacity, proposed_ticket_price, fixed_cost, minimum_capacity))
    print("\n\t{:<14s}{:^20s}{:^15s}{:^19s}{:>14s}".format('Number of\n\tPassengers', 'Ticket Price', 'Gross', 'Fixed Cost', 'Profit'))
    dash = '-' * 78
    print('\t%s'% dash)

    max_profit = math.inf * -1

    for count in range(minimum_capacity, maximum_capacity + 10, 10):
        people_number = count

        ticket_cost = proposed_ticket_price - (((people_number - minimum_capacity)/10) * .5)
        gross_revenue = ticket_cost * people_number
        profit = (people_number * ticket_cost) - fixed_cost

        if max_profit < profit:
            max_profit = profit
            best_ticket_price = ticket_cost
            best_people_number = people_number


        print("\n\t{:<14d}${:<20.2f}${:<15.2f}${:<19.2f}${:<14.2f}".format(people_number, ticket_cost, gross_revenue, fixed_cost, profit))

    print("\n\tMaximum Profit:\t$%.2f"% max_profit)
    print("\tMaximum Profit Ticket Price:\t$%.2f"% best_ticket_price)
    print("\tMaximum Profit Number of Passengers:\t%d"% best_people_number)

    replay = str(input("\n\tWould you like to run another contract(Y/N): "))
    replay = replay.lower()
exit()
