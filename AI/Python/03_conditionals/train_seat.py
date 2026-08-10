seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - no AC, beds available")
    case "ac":
        print("AC - Air conditioned, comfy ride")
    case "luxury":
        print("Luxury - Premium seats with meals")
    case "general":
        print("General - Cheapest option, no reservation")
    case _:
        print("Invalid seat type")