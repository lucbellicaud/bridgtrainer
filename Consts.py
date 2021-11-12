SUITS = 'S H D C'.split()
BID_SUITS = 'C D H S N'.split()
LEVELS = '2 3 4 5 6 7 8 9 T J Q K A'.split()
CONTRACTS = [1,2,3,4,5,6,7]
PBN_TO_LIN_VUL = {'None' : "0", "NS" : "N", "EW" : "E", "All" : "B"}
LIN_DEALER_DICT = {'S' : str(1),'W' : str(2), 'N' : str(3), 'E' : str(4)}
LIN_TO_PBN_DEALER = {"1" : "S", "2" : "W", "3" : "N", "4" : "E"}
LIN_TO_PBN_VUL = {'O' : "None","N" : "NS","E" : "EW","B" : "All"}