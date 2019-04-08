# [is installed, is damaged, can be installed]

save = open("save1.txt", 'r+')

# cbi = "Can be installed"


def cbi(part):
    if not(part == "block") and (block[2] == 1):
        if part == "headGasket" and headGasket[2] == 0:
            headGasket[1] = 1
            print(headGasket)
    if part == "block" and block[1] == 2:
        block[1] = 1


temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
airFilter = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
alternator = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
block = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
brakeLining = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
camshaft = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
camshaftGear = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
carburetor = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
clutchCoverPlate = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
clutchDisc = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
clutchPressurePlate = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
crankShaft = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
crankshaftPulley = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
cylinderHead = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
dashboard = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
discBrake_1 = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
discBrake_2 = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
distributor = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
driveGear = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
drumBrake_1 = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
drumBrake_2 = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
electrics = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
enginePlate = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
exhaustMuffler = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
flywheel = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
fuelPump = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
fuelStrainer = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
fuelTank = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
gearLinkage = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
fuelTankPipe = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
gearStick = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
transmission = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
halfShaft_1 = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
halfShaft_2 = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
headGasket = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
headers = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
mainBearing_1 = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
mainBearing_2 = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
mainBearing_3 = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
oilFilter = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
oilPan = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
piston_1 = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
piston_2 = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
piston_3 = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
piston_4 = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
rockerCover = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
rockerShaft = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
spindle_1 = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
spindle_2 = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
starter = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
steeringColumn = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
steeringRack = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
steeringRods = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
wheel = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
strut_1 = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
strut_2 = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
subFrame = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
timingChain = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
timingCover = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
trailArms = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
waterPump = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
waterPumpPulley = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
wishbone_1 = temp

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = [temp1, temp2, temp3]
wishbone_2 = temp

temp = ''

gameOn = 1
while gameOn == 1:
    contents = ''
    command = input("Input Command: ")
    temp = command.split(' ')
    if len(temp) >= 2:
        contents = temp[1]
        temp.pop()
        command = ''.join(temp)
        temp = contents[0]
        print(command)

    if command == "help":
        print("You have entererd command \"help\"")
        print()
        print("Current commands are:")
        print("install (part) | Installs a part")
        print("uninstall | uninstalls part")
        print("part_list | Lists all parts and their status")
        print("")
    elif command == "part_list":
        print("a value of 1 = yes. a value of 2 = no [part is installed, is damaged, can be installed] | \n"
              "airFilter = ", airFilter, "\n" 
              "alternator = ", alternator, "\n" 
              "block = ", block, "\n" 
              "brakeLining = ", brakeLining, "\n" 
              "camshaft = ", camshaft, "\n" 
              "camshaftGear = ", camshaftGear, "\n"    
              "carburetor = ", carburetor, "\n" 
              "clutchCoverPlate = ", clutchCoverPlate, "\n" 
              "clutchDisc = ", clutchDisc, "\n" 
              "clutchPressurePlate = ", clutchPressurePlate, "\n" 
              "crankShaft = ", crankShaft, "\n" 
              "crankshaftPulley ", crankshaftPulley, "\n" 
              "clutchPressurePlate = ", cylinderHead, "\n" 
              "dashboard = ", dashboard, "\n" 
              "discBrake_1 = ", discBrake_1, "\n" 
              "discBrake_2 = ", discBrake_2, "\n" 
              "discBrake_2 = ", distributor, "\n" 
              "driveGear = ", driveGear, "\n" 
              "drumBrake_1 ", drumBrake_1, "\n" 
              "drumBrake_2 = ", drumBrake_2, "\n" 
              "electrics = ", electrics, "\n" 
              "enginePlate = ", enginePlate, "\n" 
              "exhaustMuffler = ", exhaustMuffler, "\n" 
              "flywheel = ", flywheel, "\n" 
              "fuelPump = ", fuelPump, "\n" 
              "fuelStrainer = ", fuelStrainer, "\n" 
              "fuelTank = ", fuelTank, "\n" 
              "gearLinkage = ", gearLinkage, "\n" 
              "fuelTankPipe = ", fuelTankPipe, "\n" 
              "gearStick = ", gearStick, "\n" 
              "transmission = ", transmission, "\n" 
              "halfShaft_1 = ", halfShaft_1, "\n" 
              "halfShaft_2 = ", halfShaft_2, "\n" 
              "headGasket = ", headGasket, "\n" 
              "headers = ", headers, "\n" 
              "mainBearing_1 = ", mainBearing_1, "\n" 
              "mainBearing_2 = ", mainBearing_2, "\n" 
              "mainBearing_3 = ", mainBearing_3, "\n" 
              "oilFilter = ", oilFilter, "\n" 
              "oilPan = ", oilPan, "\n" 
              "piston_1 = ", piston_1, "\n" 
              "piston_2 = ", piston_2, "\n" 
              "piston_3 = ", piston_3, "\n" 
              "piston_4 = ", piston_4, "\n" 
              "rockerCover = ", rockerCover, "\n" 
              "rockerShaft = ", rockerShaft, "\n" 
              "spindle_1 = ", spindle_1, "\n" 
              "spindle_2 = ", spindle_2, "\n" 
              "starter = ", starter, "\n" 
              "steeringColumn = ", steeringColumn, "\n" 
              "steeringRack = ", steeringRack, "\n" 
              "steeringRods = ", steeringRods, "\n" 
              "wheel = ", wheel, "\n" 
              "strut_1 = ", strut_1, "\n" 
              "strut_2 = ", strut_2, "\n" 
              "subFrame = ", subFrame, "\n" 
              "timingChain = ", timingChain, "\n" 
              "timingCover = ", timingCover, "\n" 
              "trailArms = ", trailArms, "\n" 
              "waterPump = ", waterPump, "\n" 
              "waterPumpPulley = ", waterPumpPulley, "\n" 
              "wishbone_1 = ", wishbone_1, "\n" 
              "wishbone_2 = ", wishbone_2, "\n")
    if command == 'install':
        if contents == "airFilter":
            cbi(contents)
        elif contents == "alternator":
            cbi(contents)
        elif contents == "block":
            cbi(contents)
        elif contents == "brakeLining":
            cbi(contents)
        elif contents == "camshaft":
            cbi(contents)
        elif contents == "camshaftGear":
            cbi(contents)
        elif contents == "carburetor":
            cbi(contents)
        elif contents == "clutchCoverPlate":
            cbi(contents)
        elif contents == "clutchDisc":
            cbi(contents)
        elif contents == "clutchPressurePlate":
            cbi(contents)
        elif contents == "crankShaft":
            cbi(contents)
        elif contents == "crankshaftPulley":
            cbi(contents)
        elif contents == "clutchPressurePlate":
            cbi(contents)
        elif contents == "dashboard":
            cbi(contents)
        elif contents == "discBrake_1":
            cbi(contents)
        elif contents == "discBrake_2":
            cbi(contents)
        elif contents == "driveGear":
            cbi(contents)
        elif contents == "drumBrake_1":
            cbi(contents)
        elif contents == "drumBrake_2":
            cbi(contents)
        elif contents == "electrics":
            cbi(contents)
        elif contents == "enginePlate":
            cbi(contents)
        elif contents == "exhaustMuffler":
            cbi(contents)
        elif contents == "flywheel":
            cbi(contents)
        elif contents == "fuelPump":
            cbi(contents)
        elif contents == "fuelStrainer":
            cbi(contents)
        elif contents == "fuelTank":
            cbi(contents)
        elif contents == "gearLinkage":
            cbi(contents)
        elif contents == "gearStick":
            cbi(contents)
        elif contents == "transmission":
            cbi(contents)
        elif contents == "halfShaft_1":
            cbi(contents)
        elif contents == "halfShaft_2":
            cbi(contents)
        elif contents == "headGasket":
            cbi(contents)
        elif contents == "headers":
            cbi(contents)
        elif contents == "mainBearing_1":
            cbi(contents)
        elif contents == "mainBearing_2":
            cbi(contents)
        elif contents == "mainBearing_3":
            cbi(contents)
        elif contents == "oilFilter":
            cbi(contents)
        elif contents == "oilPan":
            cbi(contents)
        elif contents == "piston_1":
            cbi(contents)
        elif contents == "piston_2":
            cbi(contents)
        elif contents == "piston_3":
            cbi(contents)
        elif contents == "piston_4":
            cbi(contents)
        elif contents == "rockerCover":
            cbi(contents)
        elif contents == "rockerShaft":
            cbi(contents)
        elif contents == "spindle_1":
            cbi(contents)
        elif contents == "spindle_2":
            cbi(contents)
        elif contents == "starter":
            cbi(contents)
        elif contents == "steeringColumn":
            cbi(contents)
        elif contents == "steeringRack":
            cbi(contents)
        elif contents == "steeringRods":
            cbi(contents)
        elif contents == "wheel":
            cbi(contents)
        elif contents == "strut_1":
            cbi(contents)
        elif contents == "strut_2":
            cbi(contents)
        elif contents == "subFrame":
            cbi(contents)
        elif contents == "timingChain":
            cbi(contents)
        elif contents == "timingCover":
            cbi(contents)
        elif contents == "trailArms":
            cbi(contents)
        elif contents == "waterPump":
            cbi(contents)
        elif contents == "waterPumpPulley":
            cbi(contents)
        elif contents == "wishbone_1":
            cbi(contents)
        elif contents == "wishbone_2":
            cbi(contents)
        else:
            print("Incorrect part")
    elif command == save:
        print()


    else:
        print("Incorrect command")
        print()
