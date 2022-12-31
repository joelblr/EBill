
"""
    BESCOM
                    Fixed Charges per month

                                            2021			2022

    *	for first unit						₹ 85			₹ 100
    *	for every subsequent unit			₹ 95			₹ 110
            from 1KW to 50KW


                    Energy charges per month

                                2021			2022

    *	for   0-50  units		₹ 4.10			₹ 4.15
    *	for  51-100 Units		₹ 5.55			₹ 5.60
    *	for 101-200 units		₹ 7.10			₹ 7.15
    *	for abv 200 units		₹ 8.15			₹ 8.20

    *	Fuel Cost Adjustment Charges
    FAC Charges : ₹ 0.74 per unit.
"""


#######################################################
# XXX Class form
# UI to Store 12 months' data
# Calculate mean, highest, lowest, variance of data
# Display Graphs
#######################################################

class DisplayEBill :

    def __init__(self) :

        from datetime import datetime

        left, right = ">" * 45, "<" * 45

        date = datetime.now()
        day, month, year = 8, date.month, date.year

        print(f"\n{left}\n")
        print("ELECTRICITY BILL : BESCOM")
        print(f"{right}")

        print("\nBILL PERIOD        %d/%d/%d - %d/%d/%d" %
            (day, month-1, year, day, month, year))
        print("RDNG. DATE                     %d/%d/%d" % (day, month, year))
        print("%s" % left)

        print("\nCONSUMPTION (UNITS)\t\t  %.0f" % Charges.units)
        print("%s" % right)

        print("    FIXED  CHARGES (UNIT, RATE, AMT)\n")
        print("1KW\t\t100\t\t  100.00")
        print("1.25KW\t\t110\t\t  137.50")
        print("%s" % right)

        print("    ENERGY CHARGES (UNIT, RATE, AMT)\n")
        for i in range( len(Charges.unitsConsumed)) :
            print("%.0f\t\t%.2f\t\t  %.2f" %
            (Charges.unitsConsumed[i], Charges.unitRate[i], Charges.unitsConsumed[i]*Charges.unitRate[i]))
        print("%s" % right)

        print("    FAC CHARGES (UNIT, RATE, AMT)\n")
        print("%.0f\t\t%.2f\t\t  %.2f" % (Charges.units, Charges.facRate, Charges.facAmt))
        print("%s" % right)

        print("    ADDITIONAL CHARGES\n")
        print("TAX\t\t\t\t₹ %.2f" % Charges.taxAmt)
        print("BILL AMT\t\t\t₹ %.2f" % Charges.totalAmt)
        print("%s\n" % right)

        print("NET AMT DUE\t\t\t₹ %.0f.00" % Charges.totalAmt)

        if (day +14 < 31) :
            print("DUE DATE\t\t\t%d/%d/%d" % (day +14, month, year))
        else :
            print("DUE DATE\t\t\t%d/%d/%d" % (day -16, month +1, year))

        print("%s\n" % left)



class Charges :

    """ TODO : Object Variables for 12 Months. """
    units = 0
    taxAmt = facAmt = 0.00
    basicAmt = totalAmt = 0.00
    unitsConsumed = [0, 0, 0, 0]

    ''' Static Variables '''
    fixedRate = 100 + 137.50
    taxRate = 0.09
    facRate = 0.74
    unitRate = [4.15, 5.60, 7.15, 8.20]



class CalculateEBill :

    def getUnits(self) :
        Charges.units = int( input("ENTER NUMBER OF UNITS CONSUMED: "))

    def getFac(self) :
        Charges.facRate = float( input("ENTER FUEL COST ADJUSTMENT RATE (FAC): "))

    def calculateFixedAmt(self) :
        return Charges.fixedRate

    def calculateFAC(self) :
        Charges.facAmt = Charges.units * Charges.facRate
        return Charges.units * Charges.facRate

    def calculateTax(self) :
        Charges.taxAmt = Charges.taxRate * Charges.basicAmt
        return Charges.taxRate * Charges.basicAmt

    def calculateEnergyCharges(self) :

        if (Charges.units <= 50) :
            Charges.unitsConsumed[0] = Charges.units

        elif (Charges.units > 50 and Charges.units <= 100) :
            Charges.unitsConsumed[0] = 50
            Charges.unitsConsumed[1] = Charges.units - 50

        elif (Charges.units > 100 and Charges.units <= 200):
            Charges.unitsConsumed[0] = 50
            Charges.unitsConsumed[1] = 50
            Charges.unitsConsumed[2] = Charges.units - 100

        elif (Charges.units > 200) :
            Charges.unitsConsumed[0] = 50
            Charges.unitsConsumed[1] = 50
            Charges.unitsConsumed[2] = 100
            Charges.unitsConsumed[3] = Charges.units - 200

        for i in range(len(Charges.unitsConsumed)) :
            Charges.basicAmt += Charges.unitsConsumed[i] * Charges.unitRate[i]

        return Charges.basicAmt

    def calculateBillAmt(self) :
        return self.calculateFAC() + self.calculateEnergyCharges() + self.calculateTax() + self.calculateFixedAmt()



class Main :
    def __init__(self) :
        main = CalculateEBill()
        main.getUnits()
        main.getFac()
        Charges.totalAmt = main.calculateBillAmt()
        DisplayEBill()



if __name__ == "__main__" :
    from time import sleep
    Main()
    sleep(7)
