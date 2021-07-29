def main():
    #write your code below this line
    count = 0
    sum = 0

    while True:
        number = int(input("Give a number:"))

        if number == 0:
            break
        
        count = count + 1
        sum = sum + number
    
    print("Number of numbers: " + str(count))
    print("Sum of the numbers: " + str(sum))

if __name__ == '__main__':
    main()
