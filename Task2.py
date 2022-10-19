#Author: Roy Afaryan 
#Assignment: Project 1
#Completed 9/19/2022

#Task 2

def fraction(num, den):
    value = num/den
    return value


count = 1
while count:
    checker = input("Would you like calculate x? (y or n): ")
    if checker == "Yes" or checker == "yes" or checker == "Y" or checker == "y":
        pass
    elif checker == "No" or checker == "no" or checker == "N" or checker == "n":
        break
    else:
        print("Please enter valid input.")
        continue
    
    while count:
        typeofInput = input("Type '1' for numerical input. Type '2' for fractional input. ")
        if typeofInput == "1":
            x = float(input("Please enter numerical value for x: "))
            break
        elif typeofInput == "2":
            fractionInput = input("Please enter fractional value for x (for π use 'pi') (ie. pi/3): ")
            num, den = fractionInput.split("/")
            if num == "pi":
                num = math.pi
            if den == "pi":
                den = math.pi
            num, den = float(num), float(den)
            x = fraction(num, den)
            break
        else:
            print("Please enter '1' or '2'.")
            continue
        
    mathSin = math.sin(x)
    taylorSin = 0
    n = 0

    for i in range(20):
        taylorSin += ((-1)**i)*(x**(2*i+1))/math.factorial(2*i+1)
        print("Intermediate Result:", taylorSin)
        n+=1
            
        if abs(taylorSin - mathSin) <= 0.000001:
            print("The Final Iteration:", taylorSin)
            print("The math.sin() function call:", mathSin)
            print("The number of iterations:", n)
            break

'''
Test Run #1
Would you like calculate x? (y or n): Yes
Type '1' for numerical input. Type '2' for fractional input. 2
Please enter fractional value for x (for π use 'pi') (ie. pi/3): pi/3
Intermediate Result: 1.0471975511965976
Intermediate Result: 0.8558007815651173
Intermediate Result: 0.8662952837868347
Intermediate Result: 0.8660212716563725
Intermediate Result: 0.8660254450997811
The Final Iteration: 0.8660254450997811
The math.sin() function call: 0.8660254037844386
The number of iterations: 5

Test Run #2
Would you like calculate x? (y or n): y
Type '1' for numerical input. Type '2' for fractional input. 2
Please enter fractional value for x (for π use 'pi') (ie. pi/3): pi/6
Intermediate Result: 0.5235987755982988
Intermediate Result: 0.49967417939436376
Intermediate Result: 0.5000021325887924
Intermediate Result: 0.4999999918690232
The Final Iteration: 0.4999999918690232
The math.sin() function call: 0.49999999999999994
The number of iterations: 4

Test Run #3
Would you like calculate x? (y or n): y
Type '1' for numerical input. Type '2' for fractional input. 1
Please enter numerical value for x: 0.112
Intermediate Result: 0.112
Intermediate Result: 0.11176584533333334
The Final Iteration: 0.11176584533333334
The math.sin() function call: 0.11176599215128519
The number of iterations: 2

Test Run #4
Would you like calculate x? (y or n): y
Type '1' for numerical input. Type '2' for fractional input. 2
Please enter fractional value for x (for π use 'pi') (ie. pi/3): pi/1
Intermediate Result: 3.141592653589793
Intermediate Result: -2.0261201264601763
Intermediate Result: 0.5240439134171688
Intermediate Result: -0.07522061590362306
Intermediate Result: 0.006925270707505135
Intermediate Result: -0.00044516023820921277
Intermediate Result: 2.1142567558399565e-05
Intermediate Result: -7.727858894306387e-07
The Final Iteration: -7.727858894306387e-07
The math.sin() function call: 1.2246467991473532e-16
The number of iterations: 8

Test Run #5
Would you like calculate x? (y or n): y
Type '1' for numerical input. Type '2' for fractional input. 2   
Please enter fractional value for x (for π use 'pi') (ie. pi/3): pi/2
Intermediate Result: 1.5707963267948966
Intermediate Result: 0.9248322292886504
Intermediate Result: 1.0045248555348174
Intermediate Result: 0.9998431013994987
Intermediate Result: 1.0000035425842861
Intermediate Result: 0.999999943741051
The Final Iteration: 0.999999943741051
The math.sin() function call: 1.0
The number of iterations: 6

Test Run #6
Would you like calculate x? (y or n): y
Type '1' for numerical input. Type '2' for fractional input. 1
Please enter numerical value for x: 1.0484721
Intermediate Result: 1.0484721
Intermediate Result: 0.8563756298683096
Intermediate Result: 0.8669341522659172
Intermediate Result: 0.8666577970844261
Intermediate Result: 0.8666620164666798
The Final Iteration: 0.8666620164666798
The math.sin() function call: 0.8666619745955373
The number of iterations: 5

Test Run #7
Would you like calculate x? (y or n): y
Type '1' for numerical input. Type '2' for fractional input. 2
Please enter fractional value for x (for π use 'pi') (ie. pi/3): pi/5
Intermediate Result: 0.6283185307179586
Intermediate Result: 0.5869768284775588
Intermediate Result: 0.5877928809703196
Intermediate Result: 0.5877852103843443
The Final Iteration: 0.5877852103843443
The math.sin() function call: 0.5877852522924731
The number of iterations: 4
'''