def direction(facing=None, turn=None):
    """Function receives the direction that user is facing (one of the 8 directions: N, NE, E, SE, S, SW, W, NW)
    and a certain degree to turn (a multiple of 45, between -1080 and 1080)
    and returns the direction that user face after the turn."""

    direct = {"N", "NE", "E", "SE", "S", "SW", "W", "NW"}
    if facing is None:
        print("Please enter name of the direction that you are facing")
    if turn is None:
        print("Please enter value of the degree to turn")
    elif facing not in direct:
        print("Please enter correct name of the direction that you are facing")
    elif not type(turn) is int or turn%45 != 0 or turn > 1080 or turn < -1080:
        print("Value of the degree to turn should be integer, that is a multiple of 45 and between -1080 and 1080")
    else:
        depend = {"N": 360, "NE": 45, "E": 90, "SE": 135, "S": 180, "SW": 225, "W": 270, "NW": 315}
        facing = depend[facing]
        orientation = (facing - 360) + ((turn / 360) - (turn // 360)) * 360
        if orientation <= 0:
            orientation += 360
        answer = {360: "N", 45: "NE", 90: "E", 135: "SE", 180: "S", 225: "SW", 270: "W", 315: "NW"}
        result = answer[orientation]
        # print(result)
        return result

# direction("N", 5)






