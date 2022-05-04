import os

def init_():
    print()
    print("Wellcome to the Conversions!")
    print()
    print("1 - To convert distance.")
    print("2 - To convert temperature.")
    print("3 - To convert energy.")
    print("4 - To convert weight")
    print("5 - To convert area")
    print("6 - To convert volume")
    print("7 - To convert money [Coming soon]")
    print("___________________________________________________________")
    
def init_meters():
    print()
    print("1: Km")
    print("2: m")
    print("3: cm")
    print("4: mm")
    print("5: mi")
    print("6: ft")
    print("7: in")
    print()

def init_temp():
    print()
    print("1: K")
    print("2: °C")
    print("3: °F")
    print()

def init_energy():
    print()
    print("1: J")
    print("2: eV")
    print("3: Kcal")
    print("4: KWh")
    print()

def init_weight():
    print()
    print("1: ton")
    print("2: Kg")
    print("3: g")
    print("4: mg")
    print("5: μg")
    print("6: lbs")
    print()

def init_area():
    print()
    print("1: Km^2")
    print("2: m^2")
    print("3: cm^2")
    print("4: mm^2")
    print()

def init_volume():
    print()
    print("1: m^3")
    print("2: dm^3")
    print("3: cm^3")
    print("4: mm^3")
    print("5: l")
    print("6: ml")
    print()

def print_(x):
    print()
    print(x)
    print("___________________________________________________________")

condition = True

while condition:
    init_()
    print()
    kind = input("What do you want to convert? ")
    print("___________________________________________________________")
    kind = kind.lower()
    if kind == "stop":
        quit()
    else:
        try:
            kind_= int(kind)
            if kind_ == 1:
                init_meters()
                in_data = input("Which is the Unit of measurement you want to convert? ")
                in_data = in_data.lower()
                if in_data == "stop":
                    break
                out_data = input("Okay... Do you want to convert it to? ")
                out_data = out_data.lower()
                if out_data == "stop":
                    break
                else:
                    iin_data = int(in_data)
                    iout_data = int(out_data)
                    if iin_data == 1:
                        iin = input("Enter the value of it in Km: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        iin = float(iin)
                        if iout_data == 1:
                            print_("Oops! You are trying to convert Km to Km.")
                        elif iout_data == 2: # Km to m
                            x = iin*1000
                            print_("%f Km is equal to %f m." % (iin, x))
                        elif iout_data == 3: # Km to cm
                            x = iin*100000
                            print_("%f Km is equal to %f cm." % (iin, x))
                        elif iout_data == 4: # Km to mm
                            x = iin*1000000
                            print_("%f Km is equal to %f mm." % (iin, x))
                        elif iout_data == 5: # Km to mi
                            x = iin*0.621371
                            print_("%f Km is equal to %f mi." % (iin, x))
                        elif iout_data == 6: # Km to ft
                            x = iin*3280.84
                            print_("%f Km is equal to %f ft." % (iin, x))
                        elif iout_data == 7: # Km to in 
                            x = iin*39370.08
                            print_("%f Km is equal to %f in." % (iin, x))  
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 2:
                        iin = input("Enter the value of it in m: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        iin = float(iin)
                        if iout_data == 1: # m to Km
                            x = iin/1000
                            print_("%f m is equal to %f Km." % (iin, x))
                        elif iout_data == 2: # m to m
                            print_("Oops! You are trying to convert m to m.")
                        elif iout_data == 3: # m to cm
                            x = iin*100
                            print_("%f m is equal to %f cm." % (iin, x))
                        elif iout_data == 4: # m to mm
                            x = iin*1000
                            print_("%d m is equal to %d mm." % (iin, x))
                        elif iout_data == 5: # m to mi
                            x = iin*0.000621371
                            print_("%d m is equal to %d mi." % (iin, x))
                        elif iout_data == 6: # m to ft
                            x = iin*3.28084
                            print_("%d m is equal to %d ft." % (iin, x))
                        elif iout_data == 7: # m to in
                            x = iin*39.3701
                            print_("%d m is equal to %d in." % (iin, x))
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 3:
                        iin = input("Enter the value of it in cm: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        iin = float(iin)
                        if iout_data == 1: # cm to Km
                            x = iin/100000
                            print_("%f cm is equal to %f Km." % (iin, x))
                        elif iout_data == 2: # cm to m
                            x = iin/100
                            print_("%f cm is equal to %f m." % (iin, x))
                        elif iout_data == 3: # cm to cm
                            print("Oops! You are trying to convert cm to cm.")
                        elif iout_data == 4: # cm to mm
                            x = iin*10
                            print_("%f cm is equal to %f mm." % (iin, x))
                        elif iout_data == 5: # cm to mi
                            x = iin*0.00000621371
                            print_("%f cm is equal to %f mi." % (iin, x))
                        elif iout_data == 6: # cm to ft
                            x = iin*0.0328084
                            print_("%f cm is equal to %f ft." % (iin, x))
                        elif iout_data == 7: # cm to in
                            x = iin*0,393701
                            print_("%f cm is equal to %f in." % (iin, x))
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 4:
                        iin = input("Enter the value of it in mm: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        iin = float(iin)
                        if iout_data == 1: # mm to Km
                            x = iin/1000000
                            print_("%f mm is equal to %f Km." % (iin, x))
                        elif iout_data == 2: # mm to m
                            x = iin/1000
                            print_("%f mm is equal to %f m." % (iin, x))
                        elif iout_data == 3: # mm to cm
                            x = iin/10
                            print_("%f mm is equal to %f cm." % (iin, x))
                        elif iout_data == 4: # mm to mm
                            print("Oops!")
                        elif iout_data == 5: # mm to mi
                            x = iin*0.000000621371
                            print_("%f mm is equal to %f mi." % (iin, x))
                        elif iout_data == 6: # mm to ft
                            x = iin*0.00328084
                            print_("%f mm is equal to %f ft." % (iin, x))
                        elif iout_data == 7: # mm to in
                            x = iin*0.0393701
                            print_("%f mm is equal to %f in." % (iin, x))
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 5:
                        iin = input("Enter the value of it in mi: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1: # mi to Km
                            print("okay")
                        elif iout_data == 2: # mi to m
                            print("okay")
                        elif iout_data == 3: # mi to cm
                            print("okay")
                        elif iout_data == 4: # mi to mm
                            print("okay")
                        elif iout_data == 5: # mi to mi
                            print("Oops!")
                        elif iout_data == 6: # mi to ft
                            print("okay")
                        elif iout_data == 7: # mi to in
                            print("okay")
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 6:
                        iin = input("Enter the value of it in ft: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1: # ft to Km
                            print("okay")
                        elif iout_data == 2: # ft to m
                            print("okay")
                        elif iout_data == 3: # ft to cm
                            print("okay")
                        elif iout_data == 4: # ft to mm
                            print("okay")
                        elif iout_data == 5: # ft to mi
                            print("okay")
                        elif iout_data == 6: # ft to ft
                            print("Oops!")
                        elif iout_data == 7: # ft to in
                            print("okay")
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 7:
                        iin = input("Enter the value of it in in: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1: # in to Km
                            print("okay")
                        elif iout_data == 2: # in to m
                            print("okay")
                        elif iout_data == 3: # in to cm
                            print("okay")
                        elif iout_data == 4: # in to mm
                            print("okay")
                        elif iout_data == 5: # in to mi
                            print("okay")
                        elif iout_data == 6: # in to ft
                            print("okay")
                        elif iout_data == 7: # in to in
                            print("Oops!")
                        else:
                            print("Enter a valid data!")
            elif kind_ == 2:
                init_temp()
                in_data = input("Which is the Unit of measurement you want to convert? ")
                in_data = in_data.lower()
                if in_data == "stop":
                    break
                out_data = input("Okay... Do you want to convert it to? ")
                out_data = out_data.lower()
                if out_data == "stop":
                    break
                else:
                    iin_data = int(in_data)
                    iout_data = int(out_data)
                    if iin_data == 1:
                        iin = input("Enter the value of it in K: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1:
                            print("Oops!")
                        elif iout_data == 2:
                            print("okay")
                        elif iout_data == 3:
                            print("okay") 
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 2:
                        iin = input("Enter the value of it in °C: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1:
                            print("Okay")
                        elif iout_data == 2:
                            print("Oops!")
                        elif iout_data == 3:
                            print("okay")
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 3:
                        iin = input("Enter the value of it in °F: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1:
                            print("okay")
                        elif iout_data == 2:
                            print("okay")
                        elif iout_data == 3:
                            print("Oops!")
                        else:
                            print("Enter a valid data!")
            elif kind_ == 3:
                init_energy()
                in_data = input("Which is the Unit of measurement you want to convert? ")
                in_data = in_data.lower()
                if in_data == "stop":
                    break
                out_data = input("Okay... Do you want to convert it to? ")
                out_data = out_data.lower()
                if out_data == "stop":
                    break
                else:
                    iin_data = int(in_data)
                    iout_data = int(out_data)
                    if iin_data == 1:
                        iin = input("Enter the value of it in J: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1:
                            print("Oops!")
                        elif iout_data == 2:
                            print("okay")
                        elif iout_data == 3:
                            print("okay")
                        elif iout_data == 4:
                            print("okay")  
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 2:
                        iin = input("Enter the value of it in eV: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1:
                            print("Okay")
                        elif iout_data == 2:
                            print("Oops!")
                        elif iout_data == 3:
                            print("okay")
                        elif iout_data == 4:
                            print("okay")
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 3:
                        iin = input("Enter the value of it in Kcal: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1:
                            print("okay")
                        elif iout_data == 2:
                            print("okay")
                        elif iout_data == 3:
                            print("Oops!")
                        elif iout_data == 4:
                            print("okay")
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 4:
                        iin = input("Enter the value of it in KWh: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1:
                            print("okay")
                        elif iout_data == 2:
                            print("okay")
                        elif iout_data == 3:
                            print("okay")
                        elif iout_data == 4:
                            print("Oops!")
                        else:
                            print("Enter a valid data!")
            elif kind_ == 4:
                init_weight()
                in_data = input("Which is the Unit of measurement you want to convert? ")
                in_data = in_data.lower()
                if in_data == "stop":
                    break
                out_data = input("Okay... Do you want to convert it to? ")
                out_data = out_data.lower()
                if out_data == "stop":
                    break
                else:
                    iin_data = int(in_data)
                    iout_data = int(out_data)
                    if iin_data == 1:
                        iin = input("Enter the value of it in ton: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1:
                            print("Oops!")
                        elif iout_data == 2:
                            print("okay")
                        elif iout_data == 3:
                            print("okay")
                        elif iout_data == 4:
                            print("okay")
                        elif iout_data == 5:
                            print("okay")
                        elif iout_data == 6:
                            print("okay")  
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 2:
                        iin = input("Enter the value of it in Kg: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1:
                            print("Okay")
                        elif iout_data == 2:
                            print("Oops!")
                        elif iout_data == 3:
                            print("okay")
                        elif iout_data == 4:
                            print("okay")
                        elif iout_data == 5:
                            print("okay")
                        elif iout_data == 6:
                            print("okay")
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 3:
                        iin = input("Enter the value of it in g: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1:
                            print("okay")
                        elif iout_data == 2:
                            print("okay")
                        elif iout_data == 3:
                            print("Oops!")
                        elif iout_data == 4:
                            print("okay")
                        elif iout_data == 5:
                            print("okay")
                        elif iout_data == 6:
                            print("okay")
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 4:
                        iin = input("Enter the value of it in mg: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1:
                            print("okay")
                        elif iout_data == 2:
                            print("okay")
                        elif iout_data == 3:
                            print("okay")
                        elif iout_data == 4:
                            print("Oops!")
                        elif iout_data == 5:
                            print("okay")
                        elif iout_data == 6:
                            print("okay")
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 5:
                        iin = input("Enter the value of it in μg: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1:
                            print("okay")
                        elif iout_data == 2:
                            print("okay")
                        elif iout_data == 3:
                            print("okay")
                        elif iout_data == 4:
                            print("okay")
                        elif iout_data == 5:
                            print("Oops!")
                        elif iout_data == 6:
                            print("okay")
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 6:
                        iin = input("Enter the value of it in lbs: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1:
                            print("okay")
                        elif iout_data == 2:
                            print("okay")
                        elif iout_data == 3:
                            print("okay")
                        elif iout_data == 4:
                            print("okay")
                        elif iout_data == 5:
                            print("okay")
                        elif iout_data == 6:
                            print("Oops!")
                        else:
                            print("Enter a valid data!")
            elif kind_ == 5:
                init_area()
                in_data = input("Which is the Unit of measurement you want to convert? ")
                in_data = in_data.lower()
                if in_data == "stop":
                    break
                out_data = input("Okay... Do you want to convert it to? ")
                out_data = out_data.lower()
                if out_data == "stop":
                    break
                else:
                    iin_data = int(in_data)
                    iout_data = int(out_data)
                    if iin_data == 1:
                        iin = input("Enter the value of it in Km^2: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1:
                            print("Oops!")
                        elif iout_data == 2:
                            print("okay")
                        elif iout_data == 3:
                            print("okay")
                        elif iout_data == 4:
                            print("okay")  
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 2:
                        iin = input("Enter the value of it in m^2: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1:
                            print("Okay")
                        elif iout_data == 2:
                            print("Oops!")
                        elif iout_data == 3:
                            print("okay")
                        elif iout_data == 4:
                            print("okay")
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 3:
                        iin = input("Enter the value of it in cm^2: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1:
                            print("okay")
                        elif iout_data == 2:
                            print("okay")
                        elif iout_data == 3:
                            print("Oops!")
                        elif iout_data == 4:
                            print("okay")
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 4:
                        iin = input("Enter the value of it in mm^2: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1:
                            print("okay")
                        elif iout_data == 2:
                            print("okay")
                        elif iout_data == 3:
                            print("okay")
                        elif iout_data == 4:
                            print("Oops!")
                        else:
                            print("Enter a valid data!")
            elif kind_ == 6:
                init_volume()
                in_data = input("Which is the Unit of measurement you want to convert? ")
                in_data = in_data.lower()
                if in_data == "stop":
                    break
                out_data = input("Okay... Do you want to convert it to? ")
                out_data = out_data.lower()
                if out_data == "stop":
                    break
                else:
                    iin_data = int(in_data)
                    iout_data = int(out_data)
                    if iin_data == 1:
                        iin = input("Enter the value of it in m^3: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1:
                            print("Oops!")
                        elif iout_data == 2:
                            print("okay")
                        elif iout_data == 3:
                            print("okay")
                        elif iout_data == 4:
                            print("okay")
                        elif iout_data == 5:
                            print("okay")
                        elif iout_data == 6:
                            print("okay")
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 2:
                        iin = input("Enter the value of it in dm^3: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1:
                            print("Okay")
                        elif iout_data == 2:
                            print("Oops!")
                        elif iout_data == 3:
                            print("okay")
                        elif iout_data == 4:
                            print("okay")
                        elif iout_data == 5:
                            print("okay")
                        elif iout_data == 6:
                            print("okay")
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 3:
                        iin = input("Enter the value of it in cm^3: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1:
                            print("okay")
                        elif iout_data == 2:
                            print("okay")
                        elif iout_data == 3:
                            print("Oops!")
                        elif iout_data == 4:
                            print("okay")
                        elif iout_data == 5:
                            print("okay")
                        elif iout_data == 6:
                            print("okay")
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 4:
                        iin = input("Enter the value of it in mm^3: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1:
                            print("okay")
                        elif iout_data == 2:
                            print("okay")
                        elif iout_data == 3:
                            print("okay")
                        elif iout_data == 4:
                            print("Oops!")
                        elif iout_data == 5:
                            print("okay")
                        elif iout_data == 6:
                            print("okay")
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 5:
                        iin = input("Enter the value of it in l: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1:
                            print("okay")
                        elif iout_data == 2:
                            print("okay")
                        elif iout_data == 3:
                            print("okay")
                        elif iout_data == 4:
                            print("okay")
                        elif iout_data == 5:
                            print("Oops!")
                        elif iout_data == 6:
                            print("okay")
                        else:
                            print("Enter a valid data!")
                    elif iin_data == 6:
                        iin = input("Enter the value of it in ml: ")
                        iin = iin.lower()
                        if iin == "stop":
                            break
                        if iout_data == 1:
                            print("okay")
                        elif iout_data == 2:
                            print("okay")
                        elif iout_data == 3:
                            print("okay")
                        elif iout_data == 4:
                            print("okay")
                        elif iout_data == 5:
                            print("okay")
                        elif iout_data == 6:
                            print("Oops!")
                        else:
                            print("Enter a valid data!")
            elif kind_ == 7:
                print_("Wait patiently... Coming soon!")
            else:
                print_("Please, enter a valid case.")
            print()
            cont = input("[Y/N] Do you want to excute the Conversions again? ")
            cont = cont.lower()
            if cont == "y":
                condition = True
                os.system("clear")
            else:
                condition = False
                print_("Thank you for using Conversions!")
        except:
            print_("Invalid data!")
