def rat_count_house(r,unit,house):

    current_food = 0 

    target_food = r * unit
     
    house_visited = 0 

    for i in house:
        if current_food < target_food:
            current_food += i
            house_visited += 1

            if current_food >= target_food:
                return house_visited
        
    return house_visited

print(rat_count_house(5,3,[10, 10, 10]))




