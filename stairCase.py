def printstaircase(stairs_count=0,symbol='#',default_value=1):
    n = stairs_count
    while stairs_count >= default_value:
        print(' ' * n, symbol * default_value)
        default_value=default_value+1
        n = n-1

height_of_staircase=int(input('Enter how many lines you want to print : '))
printstaircase(height_of_staircase)
