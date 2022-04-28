def main():
    display_mainmenu()

    numarr = user_input()
    meantemp = calc_average_temperature(numarr)
    minmax = calc_min_max_temperature(numarr)

    print ("\nyour numbers are: ",numarr)
    print ("\nthe average of these numbers are: ", meantemp)
    print ("\nthe smallest and largest numbers are: ", minmax)


def display_mainmenu():
    print("\nWe learn new language now aka we get tortured by a snake aka c++ baddie")
    print ("Hi enter some numbers pls [use commas :P ]\n")

def user_input():
    numarr = input().split(",")
    numarr = [float(i) for i in numarr]
    return numarr

def calc_average_temperature(numarr):
    count = 0
    total = 0

    for i in numarr:
        count += 1

    for i in numarr:
        total += i
    averagetemp = total / count
    return averagetemp

def calc_min_max_temperature(numarr):
    largest = numarr[0]
    for i in numarr:
        if largest < i:
            largest = i

    largent = numarr[0]
    for i in numarr:
        if largent > i:
            largent = i

    minmax = [largent, largest]
    return minmax






if __name__ == "__main__":
    main()
