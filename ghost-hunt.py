"""
Kiran Adhikari
2020-11-07
"""
location_name = "house"

def main():
    read_motion("ravensnest")
    read_emf("ravensnest")
    read_temp("ravensnest")
    generate_report("ghost_report", read_motion, read_emf, read_temp)

# This function is used to detect movment at a given location within the house
def read_motion(location_name):
    motion_detected = []
    with open (location_name + ".motion.txt", "r") as f:
        for line in f:
            line = line.strip('\n')
            line = line.split(',')
            if line[2] == 'detected':
                motion_detected.append(line)
        return (motion_detected)

# This function is used to read the EMF level from a given room/location within the house
def read_emf(location_name):
    emf_detected = []
    with open (location_name + ".emf.txt","r") as f:
        total = 0
        count = 0
        average = 0
        for line in f:
            line = line.strip('\n')
            
            if not line.isdigit():
                total = 0
                count = 0
                if average >= 3:
                    emf_detected.append(line)   
            else:
                count += 1
                total += int(line)
                average = total/count
        return (emf_detected)

# Calling helper function that checks valid temperatures 
def is_valid_temp(val):
    val = val.split(',')
    return val[0].isdigit()
# this function reads the temperature in a given room to check for freezing temperatures where the 'ghost' is most likely to be found
def read_temp(location_name):
    count = 0
    freezing_temp_detected = []
    with open(location_name + ".temp.txt", "r") as f:
        for line in f:
            if is_valid_temp(line) and line < 0:
                count += 1
                if count >= 5:
                    freezing_temp_detected.append(line)
            elif not is_valid_temp(line) or line >= 0:
                count = 0
        return(freezing_temp_detected)

# helper function used to return the report after an investigation is done and checks if any entities were present in any of the rooms
def generate_report(location, motion, emf, temp):
    motion_detected = ["breakroom", "kitchen", "gameroom", "closet"]
    emf_detected = ["kitchen", "gameroom"]
    freezing_temp_detected = ["gameroom"]
    with open(location_name + ".ravensnest.txt", "w") as f:
        if "kitchen" in emf_detected and "kitchen" in motion_detected:
            return("Oni in gameroom")
        elif "gameroom" in motion_detected and "gameroom" in freezing_temp_detected:
            return("Banshee in gameroom")
        elif "gameroom" in motion_detected and "gameroom" in freezing_temp_detected and "gameroom" in emf_detected:
            return("Poltergeist in gameroom")
        elif "gameroom" in emf_detected and "gameoroom"  in freezing_temp_detected:
            return("Phantom in gameroom")

if __name__ == "__main__":
    main()