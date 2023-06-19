BDDmin_options = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]
BDDhour_options = {'08:30': 1, '09:00': 2, '09:30': 3, '10:00': 4, '10:30': 5, '11:00': 6, '11:30': 7, '12:00': 8, \
                '12:30': 9, '13:00': 10, '13:30': 11, '14:00': 12, '14:30': 13, '15:00': 14, '15:30': 15, '16:00': 16, \
                '16:30': 17, '17:00': 18, '17:30': 19, '18:00': 20, '18:30': 21, '19:00': 22, '19:30': 23, '20:00': 24, \
                '20:30': 25, '21:00': 26, '21:30': 27, '22:00': 28, '22:30': 29, '23:00': 30}

BDDdictypes = {3146:(0, "Place Standard"), 3147:(1, "Prise Electrique"), 3148:(2, "Ordinateur"), 3149:(3, "Travail en groupe"), 3150:(4, "Accès PMR"), 3161:(15, "Visite Express")}
BDDjour = {0:"Aujourd'hui", 1:"Demain"}

def BDDminToHour(minu):
    """Given an integer min returns a string hour"""
    if int(minu/60) != 0 :
        return f"{int(minu/60)}h{(str(minu%60)+'0')[:2]}"
    else :
        return f"{minu}min"
    
def BDDhourToMin(ho):
    """Given a string "1h30" returns the integer 90 for instance"""
    H = ho.split("h")
    if len(H) > 1 :
        return int(H[0])*60 + int(H[1])
    else :
        return int(H[0][:-3])

BDDK1 = [{'number': 2, 'x': 10, 'y': 633, 'w': 630, 'h' : 70}, \
      {'number': 3, 'x': 648, 'y': 633, 'w': 491, 'h' : 70}, \
      {'number': 4, 'x': 306, 'y': 543, 'w': 146, 'h' : 165}, \
{'number': 6001, 'x': 48, 'y': 519, 'key_pressed': 'right'}, \
{'number': 6002, 'x': 80, 'y': 517, 'key_pressed': 'right'}, \
{'number': 6003, 'x': 153, 'y': 518, 'key_pressed': 'right'}, \
{'number': 6004, 'x': 184, 'y': 518, 'key_pressed': 'right'}, \
{'number': 6021, 'x': 281, 'y': 211, 'key_pressed': 'left'}, \
{'number': 6022, 'x': 281, 'y': 249, 'key_pressed': 'left'}, \
{'number': 6023, 'x': 281, 'y': 284, 'key_pressed': 'left'}, \
{'number': 6024, 'x': 280, 'y': 324, 'key_pressed': 'left'}, \
{'number': 6025, 'x': 311, 'y': 324, 'key_pressed': 'left'}, \
{'number': 6026, 'x': 311, 'y': 288, 'key_pressed': 'left'}, \
{'number': 6027, 'x': 310, 'y': 250, 'key_pressed': 'left'}, \
{'number': 6028, 'x': 311, 'y': 213, 'key_pressed': 'left'}, \
{'number': 6029, 'x': 443, 'y': 237, 'key_pressed': 'right'}, \
{'number': 6030, 'x': 408, 'y': 236, 'key_pressed': 'right'}, \
{'number': 6031, 'x': 378, 'y': 243, 'key_pressed': 'left'}, \
{'number': 6032, 'x': 377, 'y': 279, 'key_pressed': 'left'}, \
{'number': 6033, 'x': 408, 'y': 279, 'key_pressed': 'right'}, \
{'number': 6034, 'x': 443, 'y': 279, 'key_pressed': 'right'}, \
{'number': 6035, 'x': 483, 'y': 279, 'key_pressed': 'left'}, \
{'number': 6036, 'x': 483, 'y': 243, 'key_pressed': 'left'}, \
{'number': 6037, 'x': 558, 'y': 208, 'key_pressed': 'left'}, \
{'number': 6038, 'x': 557, 'y': 245, 'key_pressed': 'left'}, \
{'number': 6039, 'x': 557, 'y': 283, 'key_pressed': 'left'}, \
{'number': 6040, 'x': 556, 'y': 320, 'key_pressed': 'left'}, \
{'number': 6041, 'x': 586, 'y': 320, 'key_pressed': 'left'}, \
{'number': 6042, 'x': 587, 'y': 283, 'key_pressed': 'left'}, \
{'number': 6043, 'x': 587, 'y': 245, 'key_pressed': 'left'}, \
{'number': 6044, 'x': 587, 'y': 209, 'key_pressed': 'left'}, \
{'number': 6045, 'x': 650, 'y': 209, 'key_pressed': 'left'}, \
{'number': 6046, 'x': 650, 'y': 246, 'key_pressed': 'left'}, \
{'number': 6047, 'x': 650, 'y': 282, 'key_pressed': 'left'}, \
{'number': 6048, 'x': 651, 'y': 319, 'key_pressed': 'left'}, \
{'number': 6049, 'x': 680, 'y': 319, 'key_pressed': 'left'}, \
{'number': 6050, 'x': 680, 'y': 283, 'key_pressed': 'left'}, \
{'number': 6051, 'x': 680, 'y': 246, 'key_pressed': 'left'}, \
{'number': 6052, 'x': 680, 'y': 209, 'key_pressed': 'left'}, \
{'number': 6053, 'x': 787, 'y': 320, 'key_pressed': 'right'}, \
{'number': 6054, 'x': 752, 'y': 321, 'key_pressed': 'right'}, \
{'number': 6055, 'x': 752, 'y': 351, 'key_pressed': 'right'}, \
{'number': 6056, 'x': 786, 'y': 351, 'key_pressed': 'right'}, \
{'number': 6073, 'x': 1229, 'y': 297, 'key_pressed': 'right'}, \
{'number': 6074, 'x': 1192, 'y': 298, 'key_pressed': 'right'}, \
{'number': 6075, 'x': 1193, 'y': 266, 'key_pressed': 'left'}, \
{'number': 6076, 'x': 1193, 'y': 229, 'key_pressed': 'left'}, \
{'number': 6077, 'x': 1193, 'y': 193, 'key_pressed': 'right'}, \
{'number': 6078, 'x': 1228, 'y': 192, 'key_pressed': 'right'}, \
{'number': 6079, 'x': 1238, 'y': 230, 'key_pressed': 'left'}, \
{'number': 6080, 'x': 1238, 'y': 267, 'key_pressed': 'left'}, \
{'number': 6081, 'x': 1373, 'y': 263, 'key_pressed': 'right'}, \
{'number': 6082, 'x': 1338, 'y': 263, 'key_pressed': 'right'}, \
{'number': 6083, 'x': 1307, 'y': 263, 'key_pressed': 'left'}, \
{'number': 6084, 'x': 1308, 'y': 227, 'key_pressed': 'left'}, \
{'number': 6085, 'x': 1338, 'y': 220, 'key_pressed': 'right'}, \
{'number': 6086, 'x': 1372, 'y': 219, 'key_pressed': 'right'}, \
{'number': 6087, 'x': 1414, 'y': 227, 'key_pressed': 'left'}, \
{'number': 6088, 'x': 1413, 'y': 261, 'key_pressed': 'left'}, \
{'number': 6089, 'x': 1398, 'y': 479, 'key_pressed': 'right'}, \
{'number': 6090, 'x': 1362, 'y': 480, 'key_pressed': 'right'}, \
{'number': 6005, 'x': 158, 'y': 427, 'key_pressed': 'right'}, \
{'number': 6006, 'x': 191, 'y': 425, 'key_pressed': 'right'}, \
{'number': 6007, 'x': 159, 'y': 400, 'key_pressed': 'right'}, \
{'number': 6008, 'x': 193, 'y': 399, 'key_pressed': 'right'}, \
{'number': 6009, 'x': 32, 'y': 426, 'key_pressed': 'right'}, \
{'number': 6010, 'x': 65, 'y': 424, 'key_pressed': 'right'}, \
{'number': 6011, 'x': 31, 'y': 396, 'key_pressed': 'right'}, \
{'number': 6012, 'x': 65, 'y': 396, 'key_pressed': 'right'}, \
{'number': 6013, 'x': 31, 'y': 270, 'key_pressed': 'right'}, \
{'number': 6014, 'x': 65, 'y': 270, 'key_pressed': 'right'}, \
{'number': 6015, 'x': 30, 'y': 241, 'key_pressed': 'right'}, \
{'number': 6016, 'x': 66, 'y': 241, 'key_pressed': 'right'}, \
{'number': 6017, 'x': 169, 'y': 240, 'key_pressed': 'right'}, \
{'number': 6018, 'x': 205, 'y': 241, 'key_pressed': 'right'}, \
{'number': 6019, 'x': 168, 'y': 211, 'key_pressed': 'right'}, \
{'number': 6020, 'x': 203, 'y': 211, 'key_pressed': 'right'}, \
{'number': 6057, 'x': 705, 'y': 523, 'key_pressed': 'left'}, \
{'number': 6058, 'x': 706, 'y': 558, 'key_pressed': 'left'}, \
{'number': 6059, 'x': 736, 'y': 557, 'key_pressed': 'left'}, \
{'number': 6060, 'x': 736, 'y': 522, 'key_pressed': 'left'}, \
{'number': 6061, 'x': 892, 'y': 562, 'key_pressed': 'right'}, \
{'number': 6062, 'x': 926, 'y': 560, 'key_pressed': 'right'}, \
{'number': 6063, 'x': 891, 'y': 532, 'key_pressed': 'right'}, \
{'number': 6064, 'x': 927, 'y': 532, 'key_pressed': 'right'}, \
{'number': 6065, 'x': 966, 'y': 247, 'key_pressed': 'left'}, \
{'number': 6066, 'x': 966, 'y': 211, 'key_pressed': 'left'}, \
{'number': 6067, 'x': 997, 'y': 227, 'key_pressed': 'left'}, \
{'number': 6068, 'x': 996, 'y': 261, 'key_pressed': 'left'}, \
{'number': 6069, 'x': 1075, 'y': 212, 'key_pressed': 'left'}, \
{'number': 6070, 'x': 1074, 'y': 247, 'key_pressed': 'left'}, \
{'number': 6071, 'x': 1105, 'y': 246, 'key_pressed': 'left'}, \
{'number': 6072, 'x': 1105, 'y': 211, 'key_pressed': 'left'}, \
{'number': 6151, 'x': 967, 'y': 286, 'key_pressed': 'left'}, \
{'number': 6152, 'x': 967, 'y': 321, 'key_pressed': 'left'}, \
{'number': 6153, 'x': 967, 'y': 360, 'key_pressed': 'left'}, \
{'number': 6154, 'x': 967, 'y': 396, 'key_pressed': 'left'}, \
{'number': 6155, 'x': 997, 'y': 334, 'key_pressed': 'left'}, \
{'number': 6156, 'x': 997, 'y': 299, 'key_pressed': 'left'}, \
{'number': 6157, 'x': 1075, 'y': 285, 'key_pressed': 'left'}, \
{'number': 6158, 'x': 1075, 'y': 322, 'key_pressed': 'left'}, \
{'number': 6159, 'x': 1106, 'y': 321, 'key_pressed': 'left'}, \
{'number': 6160, 'x': 1105, 'y': 286, 'key_pressed': 'left'}]

BDDK2 = [
{'number': 6263, 'x': 193, 'y': 300, 'key_pressed': 'left'}, \
{'number': 6264, 'x': 193, 'y': 281, 'key_pressed': 'left'}, \
{'number': 6265, 'x': 193, 'y': 263, 'key_pressed': 'left'}, \
{'number': 6266, 'x': 194, 'y': 244, 'key_pressed': 'left'}, \
{'number': 6283, 'x': 180, 'y': 75, 'key_pressed': 'left'}, \
{'number': 6284, 'x': 180, 'y': 57, 'key_pressed': 'left'}, \
{'number': 6285, 'x': 198, 'y': 76, 'key_pressed': 'left'}, \
{'number': 6286, 'x': 199, 'y': 58, 'key_pressed': 'left'}, \
{'number': 6323, 'x': 493, 'y': 142, 'key_pressed': 'right'}, \
{'number': 6324, 'x': 514, 'y': 143, 'key_pressed': 'right'}, \
{'number': 6327, 'x': 280, 'y': 161, 'key_pressed': 'right'}, \
{'number': 6328, 'x': 301, 'y': 161, 'key_pressed': 'right'}, \
{'number': 6329, 'x': 322, 'y': 161, 'key_pressed': 'right'}, \
{'number': 6330, 'x': 340, 'y': 161, 'key_pressed': 'right'}, \
{'number': 6331, 'x': 280, 'y': 176, 'key_pressed': 'right'}, \
{'number': 6332, 'x': 301, 'y': 177, 'key_pressed': 'right'}, \
{'number': 6333, 'x': 322, 'y': 177, 'key_pressed': 'right'}, \
{'number': 6334, 'x': 340, 'y': 177, 'key_pressed': 'right'}, \
{'number': 6335, 'x': 300, 'y': 252, 'key_pressed': 'left'}, \
{'number': 6336, 'x': 302, 'y': 235, 'key_pressed': 'left'}, \
{'number': 6337, 'x': 301, 'y': 215, 'key_pressed': 'right'}, \
{'number': 6338, 'x': 321, 'y': 215, 'key_pressed': 'right'}, \
{'number': 6339, 'x': 327, 'y': 253, 'key_pressed': 'left'}, \
{'number': 6340, 'x': 326, 'y': 236, 'key_pressed': 'left'}, \
{'number': 6341, 'x': 301, 'y': 269, 'key_pressed': 'right'}, \
{'number': 6342, 'x': 320, 'y': 268, 'key_pressed': 'right'}, \
{'number': 6343, 'x': 282, 'y': 308, 'key_pressed': 'right'}, \
{'number': 6344, 'x': 300, 'y': 309, 'key_pressed': 'right'}, \
{'number': 6345, 'x': 321, 'y': 308, 'key_pressed': 'right'}, \
{'number': 6346, 'x': 342, 'y': 308, 'key_pressed': 'right'}, \
{'number': 6347, 'x': 280, 'y': 324, 'key_pressed': 'right'}, \
{'number': 6348, 'x': 304, 'y': 323, 'key_pressed': 'right'}, \
{'number': 6349, 'x': 323, 'y': 325, 'key_pressed': 'right'}, \
{'number': 6350, 'x': 341, 'y': 323, 'key_pressed': 'right'}, \
{'number': 6351, 'x': 285, 'y': 382, 'key_pressed': 'left'}, \
{'number': 6352, 'x': 283, 'y': 362, 'key_pressed': 'left'}, \
{'number': 6353, 'x': 301, 'y': 359, 'key_pressed': 'right'}, \
{'number': 6354, 'x': 321, 'y': 359, 'key_pressed': 'right'}, \
{'number': 6355, 'x': 343, 'y': 382, 'key_pressed': 'left'}, \
{'number': 6356, 'x': 343, 'y': 364, 'key_pressed': 'left'}, \
{'number': 6357, 'x': 300, 'y': 381, 'key_pressed': 'right'}, \
{'number': 6358, 'x': 317, 'y': 382, 'key_pressed': 'right'}, \
{'number': 6359, 'x': 301, 'y': 424, 'key_pressed': 'right'}, \
{'number': 6360, 'x': 322, 'y': 424, 'key_pressed': 'right'}, \
{'number': 6377, 'x': 494, 'y': 277, 'key_pressed': 'right'}, \
{'number': 6378, 'x': 512, 'y': 277, 'key_pressed': 'right'}, \
{'number': 6379, 'x': 494, 'y': 292, 'key_pressed': 'right'}, \
{'number': 6380, 'x': 515, 'y': 292, 'key_pressed': 'right'}, \
{'number': 6251, 'x': 173, 'y': 559, 'key_pressed': 'right'}, \
{'number': 6252, 'x': 194, 'y': 559, 'key_pressed': 'right'}, \
{'number': 6253, 'x': 174, 'y': 544, 'key_pressed': 'right'}, \
{'number': 6254, 'x': 193, 'y': 544, 'key_pressed': 'right'}, \
{'number': 6255, 'x': 173, 'y': 457, 'key_pressed': 'right'}, \
{'number': 6256, 'x': 194, 'y': 457, 'key_pressed': 'right'}, \
{'number': 6257, 'x': 173, 'y': 442, 'key_pressed': 'right'}, \
{'number': 6258, 'x': 193, 'y': 441, 'key_pressed': 'right'}, \
{'number': 6259, 'x': 172, 'y': 357, 'key_pressed': 'right'}, \
{'number': 6260, 'x': 193, 'y': 357, 'key_pressed': 'right'}, \
{'number': 6261, 'x': 174, 'y': 342, 'key_pressed': 'right'}, \
{'number': 6262, 'x': 194, 'y': 342, 'key_pressed': 'right'}, \
{'number': 6279, 'x': 108, 'y': 75, 'key_pressed': 'left'}, \
{'number': 6280, 'x': 108, 'y': 55, 'key_pressed': 'left'}, \
{'number': 6281, 'x': 124, 'y': 76, 'key_pressed': 'left'}, \
{'number': 6282, 'x': 125, 'y': 56, 'key_pressed': 'left'}, \
{'number': 6288, 'x': 252, 'y': 60, 'key_pressed': 'left'}, \
{'number': 6289, 'x': 268, 'y': 78, 'key_pressed': 'left'}, \
{'number': 6290, 'x': 269, 'y': 59, 'key_pressed': 'left'}, \
{'number': 6291, 'x': 333, 'y': 57, 'key_pressed': 'right'}, \
{'number': 6292, 'x': 355, 'y': 55, 'key_pressed': 'right'}, \
{'number': 6293, 'x': 375, 'y': 57, 'key_pressed': 'right'}, \
{'number': 6294, 'x': 397, 'y': 57, 'key_pressed': 'right'}, \
{'number': 6295, 'x': 333, 'y': 72, 'key_pressed': 'right'}, \
{'number': 6296, 'x': 353, 'y': 72, 'key_pressed': 'right'}, \
{'number': 6297, 'x': 376, 'y': 72, 'key_pressed': 'right'}, \
{'number': 6298, 'x': 393, 'y': 71, 'key_pressed': 'right'}, \
{'number': 6299, 'x': 473, 'y': 56, 'key_pressed': 'right'}, \
{'number': 6300, 'x': 492, 'y': 55, 'key_pressed': 'right'}, \
{'number': 6301, 'x': 515, 'y': 56, 'key_pressed': 'right'}, \
{'number': 6302, 'x': 536, 'y': 56, 'key_pressed': 'right'}, \
{'number': 6303, 'x': 474, 'y': 73, 'key_pressed': 'right'}, \
{'number': 6304, 'x': 494, 'y': 71, 'key_pressed': 'right'}, \
{'number': 6305, 'x': 515, 'y': 71, 'key_pressed': 'right'}, \
{'number': 6306, 'x': 537, 'y': 71, 'key_pressed': 'right'}, \
{'number': 6307, 'x': 332, 'y': 95, 'key_pressed': 'right'}, \
{'number': 6308, 'x': 354, 'y': 96, 'key_pressed': 'right'}, \
{'number': 6309, 'x': 375, 'y': 95, 'key_pressed': 'right'}, \
{'number': 6310, 'x': 393, 'y': 96, 'key_pressed': 'right'}, \
{'number': 6311, 'x': 331, 'y': 110, 'key_pressed': 'right'}, \
{'number': 6312, 'x': 354, 'y': 111, 'key_pressed': 'right'}, \
{'number': 6313, 'x': 374, 'y': 110, 'key_pressed': 'right'}, \
{'number': 6314, 'x': 394, 'y': 112, 'key_pressed': 'right'}, \
{'number': 6315, 'x': 472, 'y': 97, 'key_pressed': 'right'}, \
{'number': 6316, 'x': 493, 'y': 96, 'key_pressed': 'right'}, \
{'number': 6317, 'x': 514, 'y': 96, 'key_pressed': 'right'}, \
{'number': 6318, 'x': 535, 'y': 96, 'key_pressed': 'right'}, \
{'number': 6319, 'x': 472, 'y': 110, 'key_pressed': 'right'}, \
{'number': 6320, 'x': 492, 'y': 111, 'key_pressed': 'right'}, \
{'number': 6321, 'x': 515, 'y': 111, 'key_pressed': 'right'}, \
{'number': 6322, 'x': 534, 'y': 112, 'key_pressed': 'right'}, \
{'number': 6325, 'x': 413, 'y': 142, 'key_pressed': 'right'}, \
{'number': 6326, 'x': 435, 'y': 142, 'key_pressed': 'right'}, \
{'number': 6361, 'x': 409, 'y': 473, 'key_pressed': 'left'}, \
{'number': 6362, 'x': 408, 'y': 458, 'key_pressed': 'left'}, \
{'number': 6363, 'x': 425, 'y': 473, 'key_pressed': 'left'}, \
{'number': 6364, 'x': 425, 'y': 456, 'key_pressed': 'left'}, \
{'number': 6365, 'x': 408, 'y': 425, 'key_pressed': 'left'}, \
{'number': 6366, 'x': 408, 'y': 404, 'key_pressed': 'left'}, \
{'number': 6367, 'x': 407, 'y': 385, 'key_pressed': 'left'}, \
{'number': 6368, 'x': 407, 'y': 367, 'key_pressed': 'left'}, \
{'number': 6369, 'x': 408, 'y': 348, 'key_pressed': 'left'}, \
{'number': 6371, 'x': 425, 'y': 347, 'key_pressed': 'left'}, \
{'number': 6372, 'x': 425, 'y': 328, 'key_pressed': 'left'}, \
{'number': 6373, 'x': 425, 'y': 386, 'key_pressed': 'left'}, \
{'number': 6374, 'x': 425, 'y': 367, 'key_pressed': 'left'}, \
{'number': 6375, 'x': 424, 'y': 424, 'key_pressed': 'left'}, \
{'number': 6376, 'x': 425, 'y': 405, 'key_pressed': 'left'}, \
{'number': 6381, 'x': 498, 'y': 386, 'key_pressed': 'left'}, \
{'number': 6382, 'x': 499, 'y': 368, 'key_pressed': 'left'}, \
{'number': 6383, 'x': 500, 'y': 348, 'key_pressed': 'left'}, \
{'number': 6384, 'x': 499, 'y': 330, 'key_pressed': 'left'}, \
{'number': 6385, 'x': 516, 'y': 348, 'key_pressed': 'left'}, \
{'number': 6386, 'x': 517, 'y': 331, 'key_pressed': 'left'}, \
{'number': 6387, 'x': 517, 'y': 387, 'key_pressed': 'left'}, \
{'number': 6388, 'x': 517, 'y': 367, 'key_pressed': 'left'}, \
{'number': 6389, 'x': 499, 'y': 551, 'key_pressed': 'left'}, \
{'number': 6390, 'x': 499, 'y': 533, 'key_pressed': 'left'}, \
{'number': 6391, 'x': 499, 'y': 512, 'key_pressed': 'left'}, \
{'number': 6392, 'x': 499, 'y': 496, 'key_pressed': 'left'}, \
{'number': 6393, 'x': 499, 'y': 472, 'key_pressed': 'left'}, \
{'number': 6394, 'x': 499, 'y': 457, 'key_pressed': 'left'}, \
{'number': 6395, 'x': 516, 'y': 473, 'key_pressed': 'left'}, \
{'number': 6396, 'x': 516, 'y': 457, 'key_pressed': 'left'}, \
{'number': 6397, 'x': 516, 'y': 513, 'key_pressed': 'left'}, \
{'number': 6398, 'x': 516, 'y': 493, 'key_pressed': 'left'}, \
{'number': 6399, 'x': 516, 'y': 551, 'key_pressed': 'left'}, \
{'number': 6400, 'x': 517, 'y': 532, 'key_pressed': 'left'}, \
{'number': 6287, 'x': 252, 'y': 77, 'key_pressed': 'left'}, \
{'number': 6201, 'x': 408, 'y': 638, 'key_pressed': 'left'}, \
{'number': 6202, 'x': 408, 'y': 619, 'key_pressed': 'left'}, \
{'number': 6203, 'x': 425, 'y': 637, 'key_pressed': 'left'}, \
{'number': 6204, 'x': 425, 'y': 619, 'key_pressed': 'left'}, \
{'number': 6205, 'x': 425, 'y': 599, 'key_pressed': 'left'}, \
{'number': 6206, 'x': 424, 'y': 578, 'key_pressed': 'left'}, \
{'number': 6207, 'x': 408, 'y': 553, 'key_pressed': 'left'}, \
{'number': 6208, 'x': 408, 'y': 534, 'key_pressed': 'left'}, \
{'number': 6209, 'x': 407, 'y': 512, 'key_pressed': 'left'}, \
{'number': 6210, 'x': 407, 'y': 496, 'key_pressed': 'left'}, \
{'number': 6211, 'x': 424, 'y': 512, 'key_pressed': 'left'}, \
{'number': 6212, 'x': 425, 'y': 493, 'key_pressed': 'left'}, \
{'number': 6213, 'x': 425, 'y': 550, 'key_pressed': 'left'}, \
{'number': 6214, 'x': 424, 'y': 529, 'key_pressed': 'left'}, \
{'number': 6215, 'x': 498, 'y': 638, 'key_pressed': 'left'}, \
{'number': 6216, 'x': 498, 'y': 617, 'key_pressed': 'left'}, \
{'number': 6217, 'x': 499, 'y': 599, 'key_pressed': 'left'}, \
{'number': 6218, 'x': 498, 'y': 579, 'key_pressed': 'left'}, \
{'number': 6219, 'x': 515, 'y': 598, 'key_pressed': 'left'}, \
{'number': 6220, 'x': 514, 'y': 578, 'key_pressed': 'left'}, \
{'number': 6221, 'x': 514, 'y': 637, 'key_pressed': 'left'}, \
{'number': 6222, 'x': 514, 'y': 619, 'key_pressed': 'left'}, \
{'number': 6267, 'x': 94, 'y': 221, 'key_pressed': 'left'}, \
{'number': 6268, 'x': 95, 'y': 204, 'key_pressed': 'left'}, \
{'number': 6269, 'x': 79, 'y': 221, 'key_pressed': 'left'}, \
{'number': 6270, 'x': 79, 'y': 204, 'key_pressed': 'left'}, \
{'number': 6271, 'x': 62, 'y': 175, 'key_pressed': 'right'}, \
{'number': 6272, 'x': 83, 'y': 175, 'key_pressed': 'right'}, \
{'number': 6273, 'x': 63, 'y': 159, 'key_pressed': 'right'}, \
{'number': 6274, 'x': 83, 'y': 159, 'key_pressed': 'right'}, \
{'number': 6275, 'x': 124, 'y': 175, 'key_pressed': 'right'}, \
{'number': 6276, 'x': 143, 'y': 174, 'key_pressed': 'right'}, \
{'number': 6277, 'x': 123, 'y': 160, 'key_pressed': 'right'}, \
{'number': 6278, 'x': 144, 'y': 159, 'key_pressed': 'right'}, \
{'number': 6370, 'x': 407, 'y': 326, 'key_pressed': 'left'}]

### Retournement de Louis Pasteur ###
def update(d, d_new):
    """update qui ne fonctionne pas par effet de bord"""
    d_output = d
    for k in d_new:
        d_output[k] = d_new[k]
    return d_output

BDDK2 = [update(k, {'x' : 602-k['x']-16, 'y' : 804-k['y']+16}) if k['key_pressed'] == 'left' else update(k, {'x' : 602-k['x']-23, 'y' : 804-k['y']+11}) for k in BDDK2]
###                               ###

BDDK2.append({'number': 1, 'x': 30, 'y': 188, 'w': 577, 'h' : 119})
BDDK2.append({'number': 3, 'x': 720, 'y': 1158, 'w': 112, 'h' : 155})

BDDK3 = [{'number': 1, 'x': 251, 'y': 54, 'w': 515, 'h' : 50}, \
      {'number': 2, 'x': 29, 'y': 1005, 'w': 60, 'h' : 324}, \
{'number': 6513, 'x': 89, 'y': 726, 'key_pressed': 'left'}, \
{'number': 6514, 'x': 89, 'y': 705, 'key_pressed': 'left'}, \
{'number': 6515, 'x': 106, 'y': 726, 'key_pressed': 'left'}, \
{'number': 6516, 'x': 106, 'y': 705, 'key_pressed': 'left'}, \
{'number': 6549, 'x': 471, 'y': 692, 'key_pressed': 'right'}, \
{'number': 6550, 'x': 493, 'y': 692, 'key_pressed': 'right'}, \
{'number': 6551, 'x': 472, 'y': 664, 'key_pressed': 'right'}, \
{'number': 6552, 'x': 493, 'y': 664, 'key_pressed': 'right'}, \
{'number': 6561, 'x': 182, 'y': 529, 'key_pressed': 'right'}, \
{'number': 6562, 'x': 202, 'y': 528, 'key_pressed': 'right'}, \
{'number': 6563, 'x': 183, 'y': 512, 'key_pressed': 'right'}, \
{'number': 6564, 'x': 203, 'y': 512, 'key_pressed': 'right'}, \
{'number': 6569, 'x': 216, 'y': 467, 'key_pressed': 'left'}, \
{'number': 6570, 'x': 215, 'y': 447, 'key_pressed': 'left'}, \
{'number': 6571, 'x': 199, 'y': 466, 'key_pressed': 'left'}, \
{'number': 6572, 'x': 199, 'y': 446, 'key_pressed': 'left'}, \
{'number': 6517, 'x': 188, 'y': 717, 'key_pressed': 'left'}, \
{'number': 6518, 'x': 188, 'y': 700, 'key_pressed': 'left'}, \
{'number': 6519, 'x': 187, 'y': 676, 'key_pressed': 'left'}, \
{'number': 6520, 'x': 187, 'y': 656, 'key_pressed': 'left'}, \
{'number': 6521, 'x': 204, 'y': 676, 'key_pressed': 'left'}, \
{'number': 6522, 'x': 204, 'y': 656, 'key_pressed': 'left'}, \
{'number': 6523, 'x': 204, 'y': 718, 'key_pressed': 'left'}, \
{'number': 6524, 'x': 204, 'y': 699, 'key_pressed': 'left'}, \
{'number': 6525, 'x': 281, 'y': 700, 'key_pressed': 'left'}, \
{'number': 6526, 'x': 280, 'y': 681, 'key_pressed': 'left'}, \
{'number': 6527, 'x': 280, 'y': 660, 'key_pressed': 'left'}, \
{'number': 6528, 'x': 280, 'y': 639, 'key_pressed': 'left'}, \
{'number': 6529, 'x': 297, 'y': 660, 'key_pressed': 'left'}, \
{'number': 6530, 'x': 297, 'y': 641, 'key_pressed': 'left'}, \
{'number': 6531, 'x': 296, 'y': 701, 'key_pressed': 'left'}, \
{'number': 6532, 'x': 297, 'y': 678, 'key_pressed': 'left'}, \
{'number': 6533, 'x': 346, 'y': 707, 'key_pressed': 'left'}, \
{'number': 6534, 'x': 346, 'y': 686, 'key_pressed': 'left'}, \
{'number': 6535, 'x': 345, 'y': 665, 'key_pressed': 'left'}, \
{'number': 6536, 'x': 345, 'y': 645, 'key_pressed': 'left'}, \
{'number': 6537, 'x': 363, 'y': 664, 'key_pressed': 'left'}, \
{'number': 6538, 'x': 363, 'y': 645, 'key_pressed': 'left'}, \
{'number': 6539, 'x': 363, 'y': 706, 'key_pressed': 'left'}, \
{'number': 6540, 'x': 362, 'y': 686, 'key_pressed': 'left'}, \
{'number': 6541, 'x': 416, 'y': 704, 'key_pressed': 'left'}, \
{'number': 6542, 'x': 416, 'y': 684, 'key_pressed': 'left'}, \
{'number': 6543, 'x': 417, 'y': 662, 'key_pressed': 'left'}, \
{'number': 6544, 'x': 417, 'y': 641, 'key_pressed': 'left'}, \
{'number': 6545, 'x': 434, 'y': 662, 'key_pressed': 'left'}, \
{'number': 6546, 'x': 434, 'y': 641, 'key_pressed': 'left'}, \
{'number': 6547, 'x': 434, 'y': 705, 'key_pressed': 'left'}, \
{'number': 6548, 'x': 434, 'y': 682, 'key_pressed': 'left'}, \
{'number': 6553, 'x': 460, 'y': 587, 'key_pressed': 'left'}, \
{'number': 6555, 'x': 444, 'y': 587, 'key_pressed': 'left'}, \
{'number': 6556, 'x': 443, 'y': 565, 'key_pressed': 'left'}, \
{'number': 6557, 'x': 291, 'y': 563, 'key_pressed': 'right'}, \
{'number': 6558, 'x': 312, 'y': 563, 'key_pressed': 'right'}, \
{'number': 6559, 'x': 291, 'y': 545, 'key_pressed': 'right'}, \
{'number': 6560, 'x': 312, 'y': 546, 'key_pressed': 'right'}, \
{'number': 6565, 'x': 293, 'y': 513, 'key_pressed': 'right'}, \
{'number': 6566, 'x': 312, 'y': 513, 'key_pressed': 'right'}, \
{'number': 6567, 'x': 290, 'y': 474, 'key_pressed': 'right'}, \
{'number': 6568, 'x': 310, 'y': 473, 'key_pressed': 'right'}, \
{'number': 6573, 'x': 183, 'y': 402, 'key_pressed': 'right'}, \
{'number': 6574, 'x': 204, 'y': 401, 'key_pressed': 'right'}, \
{'number': 6575, 'x': 226, 'y': 400, 'key_pressed': 'right'}, \
{'number': 6576, 'x': 246, 'y': 400, 'key_pressed': 'right'}, \
{'number': 6577, 'x': 226, 'y': 384, 'key_pressed': 'right'}, \
{'number': 6578, 'x': 245, 'y': 383, 'key_pressed': 'right'}, \
{'number': 6579, 'x': 184, 'y': 383, 'key_pressed': 'right'}, \
{'number': 6580, 'x': 203, 'y': 383, 'key_pressed': 'right'}, \
{'number': 6581, 'x': 184, 'y': 348, 'key_pressed': 'right'}, \
{'number': 6582, 'x': 204, 'y': 347, 'key_pressed': 'right'}, \
{'number': 6583, 'x': 226, 'y': 347, 'key_pressed': 'right'}, \
{'number': 6584, 'x': 244, 'y': 347, 'key_pressed': 'right'}, \
{'number': 6585, 'x': 225, 'y': 331, 'key_pressed': 'right'}, \
{'number': 6586, 'x': 246, 'y': 330, 'key_pressed': 'right'}, \
{'number': 6587, 'x': 184, 'y': 330, 'key_pressed': 'right'}, \
{'number': 6588, 'x': 203, 'y': 329, 'key_pressed': 'right'}, \
{'number': 6589, 'x': 185, 'y': 290, 'key_pressed': 'right'}, \
{'number': 6590, 'x': 204, 'y': 290, 'key_pressed': 'right'}, \
{'number': 6591, 'x': 225, 'y': 289, 'key_pressed': 'right'}, \
{'number': 6592, 'x': 245, 'y': 290, 'key_pressed': 'right'}, \
{'number': 6593, 'x': 226, 'y': 272, 'key_pressed': 'right'}, \
{'number': 6594, 'x': 245, 'y': 272, 'key_pressed': 'right'}, \
{'number': 6595, 'x': 184, 'y': 272, 'key_pressed': 'right'}, \
{'number': 6596, 'x': 203, 'y': 273, 'key_pressed': 'right'}, \
{'number': 6597, 'x': 185, 'y': 242, 'key_pressed': 'right'}, \
{'number': 6598, 'x': 203, 'y': 242, 'key_pressed': 'right'}, \
{'number': 6599, 'x': 226, 'y': 242, 'key_pressed': 'right'}, \
{'number': 6600, 'x': 245, 'y': 242, 'key_pressed': 'right'}, \
{'number': 6601, 'x': 226, 'y': 225, 'key_pressed': 'right'}, \
{'number': 6602, 'x': 245, 'y': 226, 'key_pressed': 'right'}, \
{'number': 6603, 'x': 185, 'y': 226, 'key_pressed': 'right'}, \
{'number': 6604, 'x': 202, 'y': 225, 'key_pressed': 'right'}, \
{'number': 6605, 'x': 211, 'y': 171, 'key_pressed': 'right'}, \
{'number': 6606, 'x': 230, 'y': 171, 'key_pressed': 'right'}, \
{'number': 6607, 'x': 210, 'y': 154, 'key_pressed': 'right'}, \
{'number': 6608, 'x': 229, 'y': 154, 'key_pressed': 'right'}, \
{'number': 6609, 'x': 183, 'y': 98, 'key_pressed': 'right'}, \
{'number': 6610, 'x': 201, 'y': 98, 'key_pressed': 'right'}, \
{'number': 6611, 'x': 223, 'y': 98, 'key_pressed': 'right'}, \
{'number': 6612, 'x': 242, 'y': 99, 'key_pressed': 'right'}, \
{'number': 6613, 'x': 224, 'y': 81, 'key_pressed': 'right'}, \
{'number': 6614, 'x': 243, 'y': 82, 'key_pressed': 'right'}, \
{'number': 6615, 'x': 183, 'y': 81, 'key_pressed': 'right'}, \
{'number': 6616, 'x': 202, 'y': 81, 'key_pressed': 'right'}, \
{'number': 6617, 'x': 389, 'y': 111, 'key_pressed': 'right'}, \
{'number': 6618, 'x': 408, 'y': 110, 'key_pressed': 'right'}, \
{'number': 6619, 'x': 389, 'y': 147, 'key_pressed': 'right'}, \
{'number': 6620, 'x': 410, 'y': 147, 'key_pressed': 'right'}, \
{'number': 6621, 'x': 390, 'y': 183, 'key_pressed': 'right'}, \
{'number': 6622, 'x': 409, 'y': 183, 'key_pressed': 'right'}, \
{'number': 6623, 'x': 389, 'y': 219, 'key_pressed': 'right'}, \
{'number': 6624, 'x': 408, 'y': 220, 'key_pressed': 'right'}, \
{'number': 6625, 'x': 390, 'y': 257, 'key_pressed': 'right'}, \
{'number': 6626, 'x': 408, 'y': 257, 'key_pressed': 'right'}, \
{'number': 6627, 'x': 389, 'y': 293, 'key_pressed': 'right'}, \
{'number': 6628, 'x': 408, 'y': 293, 'key_pressed': 'right'}, \
{'number': 6629, 'x': 390, 'y': 332, 'key_pressed': 'right'}, \
{'number': 6630, 'x': 408, 'y': 332, 'key_pressed': 'right'}, \
{'number': 6631, 'x': 506, 'y': 365, 'key_pressed': 'right'}, \
{'number': 6632, 'x': 526, 'y': 365, 'key_pressed': 'right'}, \
{'number': 6633, 'x': 508, 'y': 382, 'key_pressed': 'right'}, \
{'number': 6634, 'x': 526, 'y': 382, 'key_pressed': 'right'}, \
{'number': 6635, 'x': 507, 'y': 413, 'key_pressed': 'right'}, \
{'number': 6636, 'x': 526, 'y': 413, 'key_pressed': 'right'}, \
{'number': 6554, 'x': 461, 'y': 569, 'key_pressed': 'left'}, \
{'number': 6501, 'x': 135, 'y': 579, 'key_pressed': 'right'}, \
{'number': 6502, 'x': 154, 'y': 579, 'key_pressed': 'right'}, \
{'number': 6503, 'x': 135, 'y': 563, 'key_pressed': 'right'}, \
{'number': 6504, 'x': 154, 'y': 564, 'key_pressed': 'right'}, \
{'number': 6505, 'x': 97, 'y': 541, 'key_pressed': 'left'}, \
{'number': 6506, 'x': 97, 'y': 520, 'key_pressed': 'left'}, \
{'number': 6507, 'x': 79, 'y': 542, 'key_pressed': 'left'}, \
{'number': 6508, 'x': 80, 'y': 521, 'key_pressed': 'left'}, \
{'number': 6509, 'x': 69, 'y': 567, 'key_pressed': 'right'}, \
{'number': 6510, 'x': 88, 'y': 568, 'key_pressed': 'right'}, \
{'number': 6511, 'x': 68, 'y': 584, 'key_pressed': 'right'}, \
{'number': 6512, 'x': 87, 'y': 585, 'key_pressed': 'right'}]

BDDniv5LOIRE = [{'number': 5, 'x': 77, 'y': 277, 'w': 20, 'h' : 254}, \
             {'number': 5, 'x': 93, 'y': 710, 'w': 219, 'h' : 28}, \
             {'number': 1, 'x': 191, 'y': 794, 'w': 118, 'h' : 81}, \
{'number': 5117, 'x': 425, 'y': 508, 'key_pressed': 'right'}, \
{'number': 5118, 'x': 449, 'y': 509, 'key_pressed': 'right'}, \
{'number': 5119, 'x': 373, 'y': 508, 'key_pressed': 'right'}, \
{'number': 5120, 'x': 397, 'y': 509, 'key_pressed': 'right'}, \
{'number': 5121, 'x': 320, 'y': 508, 'key_pressed': 'right'}, \
{'number': 5122, 'x': 343, 'y': 509, 'key_pressed': 'right'}, \
{'number': 5123, 'x': 319, 'y': 486, 'key_pressed': 'right'}, \
{'number': 5124, 'x': 344, 'y': 486, 'key_pressed': 'right'}, \
{'number': 5125, 'x': 373, 'y': 485, 'key_pressed': 'right'}, \
{'number': 5126, 'x': 396, 'y': 486, 'key_pressed': 'right'}, \
{'number': 5127, 'x': 425, 'y': 486, 'key_pressed': 'right'}, \
{'number': 5128, 'x': 450, 'y': 486, 'key_pressed': 'right'}, \
{'number': 5129, 'x': 425, 'y': 463, 'key_pressed': 'right'}, \
{'number': 5130, 'x': 449, 'y': 463, 'key_pressed': 'right'}, \
{'number': 5131, 'x': 373, 'y': 464, 'key_pressed': 'right'}, \
{'number': 5132, 'x': 396, 'y': 463, 'key_pressed': 'right'}, \
{'number': 5133, 'x': 319, 'y': 464, 'key_pressed': 'right'}, \
{'number': 5134, 'x': 344, 'y': 464, 'key_pressed': 'right'}, \
{'number': 5135, 'x': 320, 'y': 441, 'key_pressed': 'right'}, \
{'number': 5136, 'x': 344, 'y': 440, 'key_pressed': 'right'}, \
{'number': 5137, 'x': 373, 'y': 439, 'key_pressed': 'right'}, \
{'number': 5138, 'x': 396, 'y': 441, 'key_pressed': 'right'}, \
{'number': 5139, 'x': 426, 'y': 441, 'key_pressed': 'right'}, \
{'number': 5140, 'x': 449, 'y': 441, 'key_pressed': 'right'}, \
{'number': 5141, 'x': 359, 'y': 331, 'key_pressed': 'left'}, \
{'number': 5142, 'x': 359, 'y': 309, 'key_pressed': 'left'}, \
{'number': 5143, 'x': 359, 'y': 352, 'key_pressed': 'left'}, \
{'number': 5144, 'x': 358, 'y': 374, 'key_pressed': 'left'}, \
{'number': 5145, 'x': 359, 'y': 415, 'key_pressed': 'left'}, \
{'number': 5146, 'x': 358, 'y': 394, 'key_pressed': 'left'}, \
{'number': 5147, 'x': 392, 'y': 415, 'key_pressed': 'left'}, \
{'number': 5148, 'x': 393, 'y': 394, 'key_pressed': 'left'}, \
{'number': 5149, 'x': 392, 'y': 373, 'key_pressed': 'left'}, \
{'number': 5150, 'x': 392, 'y': 352, 'key_pressed': 'left'}, \
{'number': 5151, 'x': 393, 'y': 331, 'key_pressed': 'left'}, \
{'number': 5152, 'x': 392, 'y': 311, 'key_pressed': 'left'}, \
{'number': 5153, 'x': 437, 'y': 310, 'key_pressed': 'left'}, \
{'number': 5154, 'x': 437, 'y': 291, 'key_pressed': 'left'}, \
{'number': 5155, 'x': 437, 'y': 349, 'key_pressed': 'left'}, \
{'number': 5156, 'x': 437, 'y': 371, 'key_pressed': 'left'}, \
{'number': 5157, 'x': 437, 'y': 413, 'key_pressed': 'left'}, \
{'number': 5158, 'x': 437, 'y': 391, 'key_pressed': 'left'}, \
{'number': 5159, 'x': 470, 'y': 411, 'key_pressed': 'left'}, \
{'number': 5160, 'x': 471, 'y': 391, 'key_pressed': 'left'}, \
{'number': 5161, 'x': 470, 'y': 359, 'key_pressed': 'left'}, \
{'number': 5163, 'x': 471, 'y': 311, 'key_pressed': 'left'}, \
{'number': 5164, 'x': 469, 'y': 291, 'key_pressed': 'left'}, \
{'number': 5167, 'x': 251, 'y': 148, 'key_pressed': 'right'}, \
{'number': 5168, 'x': 276, 'y': 147, 'key_pressed': 'right'}, \
{'number': 5169, 'x': 310, 'y': 148, 'key_pressed': 'right'}, \
{'number': 5170, 'x': 335, 'y': 148, 'key_pressed': 'right'}, \
{'number': 5171, 'x': 370, 'y': 148, 'key_pressed': 'right'}, \
{'number': 5172, 'x': 396, 'y': 148, 'key_pressed': 'right'}, \
{'number': 5173, 'x': 431, 'y': 148, 'key_pressed': 'right'}, \
{'number': 5174, 'x': 456, 'y': 147, 'key_pressed': 'right'}, \
{'number': 5175, 'x': 430, 'y': 124, 'key_pressed': 'right'}, \
{'number': 5176, 'x': 455, 'y': 123, 'key_pressed': 'right'}, \
{'number': 5177, 'x': 370, 'y': 123, 'key_pressed': 'right'}, \
{'number': 5178, 'x': 395, 'y': 123, 'key_pressed': 'right'}, \
{'number': 5179, 'x': 311, 'y': 124, 'key_pressed': 'right'}, \
{'number': 5180, 'x': 336, 'y': 124, 'key_pressed': 'right'}, \
{'number': 5181, 'x': 251, 'y': 124, 'key_pressed': 'right'}, \
{'number': 5182, 'x': 278, 'y': 124, 'key_pressed': 'right'}, \
{'number': 5183, 'x': 252, 'y': 96, 'key_pressed': 'right'}, \
{'number': 5184, 'x': 276, 'y': 97, 'key_pressed': 'right'}, \
{'number': 5185, 'x': 311, 'y': 96, 'key_pressed': 'right'}, \
{'number': 5186, 'x': 336, 'y': 97, 'key_pressed': 'right'}, \
{'number': 5187, 'x': 372, 'y': 96, 'key_pressed': 'right'}, \
{'number': 5188, 'x': 396, 'y': 97, 'key_pressed': 'right'}, \
{'number': 5189, 'x': 432, 'y': 96, 'key_pressed': 'right'}, \
{'number': 5190, 'x': 457, 'y': 97, 'key_pressed': 'right'}, \
{'number': 5191, 'x': 431, 'y': 71, 'key_pressed': 'right'}, \
{'number': 5192, 'x': 457, 'y': 72, 'key_pressed': 'right'}, \
{'number': 5193, 'x': 370, 'y': 71, 'key_pressed': 'right'}, \
{'number': 5194, 'x': 396, 'y': 72, 'key_pressed': 'right'}, \
{'number': 5195, 'x': 312, 'y': 71, 'key_pressed': 'right'}, \
{'number': 5196, 'x': 338, 'y': 71, 'key_pressed': 'right'}, \
{'number': 5197, 'x': 251, 'y': 71, 'key_pressed': 'right'}, \
{'number': 5198, 'x': 277, 'y': 72, 'key_pressed': 'right'}, \
{'number': 5162, 'x': 470, 'y': 339, 'key_pressed': 'left'}, \
{'number': 5101, 'x': 200, 'y': 546, 'key_pressed': 'left'},  \
{'number': 5102, 'x': 200, 'y': 569, 'key_pressed': 'left'},  \
{'number': 5104, 'x': 219, 'y': 545, 'key_pressed': 'left'},  \
{'number': 5105, 'x': 385, 'y': 615, 'key_pressed': 'right'},  \
{'number': 5106, 'x': 410, 'y': 614, 'key_pressed': 'right'},  \
{'number': 5107, 'x': 435, 'y': 614, 'key_pressed': 'right'},  \
{'number': 5108, 'x': 460, 'y': 615, 'key_pressed': 'right'},  \
{'number': 5109, 'x': 458, 'y': 595, 'key_pressed': 'right'},  \
{'number': 5110, 'x': 435, 'y': 594, 'key_pressed': 'right'},  \
{'number': 5111, 'x': 409, 'y': 595, 'key_pressed': 'right'},  \
{'number': 5112, 'x': 385, 'y': 595, 'key_pressed': 'right'},  \
{'number': 5113, 'x': 426, 'y': 552, 'key_pressed': 'right'},  \
{'number': 5114, 'x': 452, 'y': 552, 'key_pressed': 'right'},  \
{'number': 5115, 'x': 462, 'y': 532, 'key_pressed': 'right'},  \
{'number': 5116, 'x': 438, 'y': 533, 'key_pressed': 'right'},  \
{'number': 5165, 'x': 377, 'y': 192, 'key_pressed': 'right'},  \
{'number': 5166, 'x': 402, 'y': 192, 'key_pressed': 'right'},  \
{'number': 5199, 'x': 213, 'y': 102, 'key_pressed': 'left'},  \
{'number': 5103, 'x': 219, 'y': 569, 'key_pressed': 'left'},  \
{'number': 5200, 'x': 213, 'y': 77, 'key_pressed': 'left'},  \
{'number': 5201, 'x': 193, 'y': 77, 'key_pressed': 'left'},  \
{'number': 5202, 'x': 192, 'y': 102, 'key_pressed': 'left'},  \
{'number': 5203, 'x': 161, 'y': 102, 'key_pressed': 'left'},  \
{'number': 5204, 'x': 161, 'y': 77, 'key_pressed': 'left'},  \
{'number': 5205, 'x': 142, 'y': 84, 'key_pressed': 'left'},  \
{'number': 5206, 'x': 142, 'y': 107, 'key_pressed': 'left'},  \
{'number': 5207, 'x': 102, 'y': 87, 'key_pressed': 'left'},  \
{'number': 5208, 'x': 102, 'y': 64, 'key_pressed': 'left'}, \
{'number': 5001, 'x': 324, 'y': 614, 'key_pressed': 'right'},  \
{'number': 5002, 'x': 350, 'y': 614, 'key_pressed': 'right'},  \
{'number': 5003, 'x': 347, 'y': 595, 'key_pressed': 'right'},  \
{'number': 5004, 'x': 325, 'y': 594, 'key_pressed': 'right'},  \
{'number': 5005, 'x': 370, 'y': 553, 'key_pressed': 'right'},  \
{'number': 5006, 'x': 395, 'y': 553, 'key_pressed': 'right'},  \
{'number': 5007, 'x': 398, 'y': 533, 'key_pressed': 'right'},  \
{'number': 5008, 'x': 374, 'y': 533, 'key_pressed': 'right'},  \
{'number': 5009, 'x': 349, 'y': 533, 'key_pressed': 'right'},  \
{'number': 5010, 'x': 325, 'y': 534, 'key_pressed': 'right'},  \
{'number': 5011, 'x': 347, 'y': 229, 'key_pressed': 'left'},  \
{'number': 5012, 'x': 347, 'y': 254, 'key_pressed': 'left'}]

BDDniv5ERDRE = [{'number': 4, 'x': 480, 'y': 212, 'w': 105, 'h' : 210}, \
             {'number': 1, 'x': 395, 'y': 785, 'w': 84, 'h' : 84}, \
{'number': 5301, 'x': 413, 'y': 71, 'key_pressed': 'left'},  \
{'number': 5302, 'x': 413, 'y': 46, 'key_pressed': 'left'},  \
{'number': 5303, 'x': 392, 'y': 71, 'key_pressed': 'left'},  \
{'number': 5304, 'x': 392, 'y': 48, 'key_pressed': 'left'},  \
{'number': 5305, 'x': 364, 'y': 71, 'key_pressed': 'left'},  \
{'number': 5306, 'x': 363, 'y': 47, 'key_pressed': 'left'},  \
{'number': 5307, 'x': 343, 'y': 48, 'key_pressed': 'left'},  \
{'number': 5308, 'x': 344, 'y': 71, 'key_pressed': 'left'},  \
{'number': 5309, 'x': 306, 'y': 47, 'key_pressed': 'right'},  \
{'number': 5310, 'x': 283, 'y': 46, 'key_pressed': 'right'},  \
{'number': 5311, 'x': 283, 'y': 66, 'key_pressed': 'right'},  \
{'number': 5312, 'x': 308, 'y': 67, 'key_pressed': 'right'},  \
{'number': 5313, 'x': 253, 'y': 46, 'key_pressed': 'right'},  \
{'number': 5314, 'x': 229, 'y': 46, 'key_pressed': 'right'},  \
{'number': 5315, 'x': 228, 'y': 66, 'key_pressed': 'right'},  \
{'number': 5316, 'x': 252, 'y': 66, 'key_pressed': 'right'},  \
{'number': 5317, 'x': 203, 'y': 83, 'key_pressed': 'left'},  \
{'number': 5318, 'x': 203, 'y': 58, 'key_pressed': 'left'},  \
{'number': 5329, 'x': 329, 'y': 262, 'key_pressed': 'right'},  \
{'number': 5330, 'x': 304, 'y': 263, 'key_pressed': 'right'},  \
{'number': 5331, 'x': 305, 'y': 291, 'key_pressed': 'right'},  \
{'number': 5332, 'x': 329, 'y': 290, 'key_pressed': 'right'},  \
{'number': 5333, 'x': 329, 'y': 317, 'key_pressed': 'right'},  \
{'number': 5334, 'x': 304, 'y': 317, 'key_pressed': 'right'},  \
{'number': 5335, 'x': 329, 'y': 343, 'key_pressed': 'right'},  \
{'number': 5336, 'x': 304, 'y': 343, 'key_pressed': 'right'},  \
{'number': 5337, 'x': 329, 'y': 372, 'key_pressed': 'right'},  \
{'number': 5338, 'x': 305, 'y': 371, 'key_pressed': 'right'},  \
{'number': 5339, 'x': 329, 'y': 399, 'key_pressed': 'right'},  \
{'number': 5340, 'x': 305, 'y': 400, 'key_pressed': 'right'},  \
{'number': 5341, 'x': 330, 'y': 429, 'key_pressed': 'right'},  \
{'number': 5342, 'x': 304, 'y': 429, 'key_pressed': 'right'},  \
{'number': 5343, 'x': 330, 'y': 459, 'key_pressed': 'right'},  \
{'number': 5344, 'x': 304, 'y': 458, 'key_pressed': 'right'},  \
{'number': 5345, 'x': 329, 'y': 483, 'key_pressed': 'right'},  \
{'number': 5346, 'x': 305, 'y': 484, 'key_pressed': 'right'},  \
{'number': 5347, 'x': 329, 'y': 509, 'key_pressed': 'right'},  \
{'number': 5348, 'x': 304, 'y': 508, 'key_pressed': 'right'},  \
{'number': 5349, 'x': 159, 'y': 360, 'key_pressed': 'right'},  \
{'number': 5350, 'x': 134, 'y': 361, 'key_pressed': 'right'},  \
{'number': 5351, 'x': 159, 'y': 380, 'key_pressed': 'right'},  \
{'number': 5352, 'x': 135, 'y': 381, 'key_pressed': 'right'},  \
{'number': 5353, 'x': 159, 'y': 417, 'key_pressed': 'right'},  \
{'number': 5354, 'x': 134, 'y': 417, 'key_pressed': 'right'},  \
{'number': 5355, 'x': 135, 'y': 437, 'key_pressed': 'right'},  \
{'number': 5356, 'x': 159, 'y': 436, 'key_pressed': 'right'},  \
{'number': 5357, 'x': 160, 'y': 494, 'key_pressed': 'right'},  \
{'number': 5358, 'x': 136, 'y': 495, 'key_pressed': 'right'},  \
{'number': 5359, 'x': 136, 'y': 514, 'key_pressed': 'right'},  \
{'number': 5360, 'x': 158, 'y': 514, 'key_pressed': 'right'},  \
{'number': 5361, 'x': 158, 'y': 545, 'key_pressed': 'right'},  \
{'number': 5362, 'x': 135, 'y': 545, 'key_pressed': 'right'},  \
{'number': 5363, 'x': 134, 'y': 566, 'key_pressed': 'right'},  \
{'number': 5364, 'x': 158, 'y': 567, 'key_pressed': 'right'}, \
{'number': 5319, 'x': 151, 'y': 55, 'key_pressed': 'right'},  \
{'number': 5320, 'x': 175, 'y': 56, 'key_pressed': 'right'},  \
{'number': 5321, 'x': 176, 'y': 36, 'key_pressed': 'right'},  \
{'number': 5322, 'x': 151, 'y': 36, 'key_pressed': 'right'},  \
{'number': 5323, 'x': 119, 'y': 47, 'key_pressed': 'right'},  \
{'number': 5324, 'x': 96, 'y': 47, 'key_pressed': 'right'},  \
{'number': 5325, 'x': 96, 'y': 66, 'key_pressed': 'right'},  \
{'number': 5326, 'x': 119, 'y': 66, 'key_pressed': 'right'},  \
{'number': 5327, 'x': 130, 'y': 92, 'key_pressed': 'right'},  \
{'number': 5328, 'x': 155, 'y': 92, 'key_pressed': 'right'},  \
{'number': 5401, 'x': 135, 'y': 639, 'key_pressed': 'right'},  \
{'number': 5402, 'x': 159, 'y': 639, 'key_pressed': 'right'}]

#!# Les fonctions suivantes ne suivent pas les évolutions dans le temps de la structure de affluences

BDDtypes = {6001: 3146, 6002: 3146, 6003: 3146, 6004: 3146, 6021: 3146, 6022: 3146, 6023: 3146, 6024: 3146, 6025: 3146, 6026: 3146, \
         6027: 3146, 6028: 3146, 6029: 3146, 6030: 3146, 6031: 3146, 6032: 3146, 6033: 3146, 6034: 3146, 6035: 3146, 6036: 3146, \
         6037: 3146, 6038: 3146, 6039: 3146, 6040: 3146, 6041: 3146, 6042: 3146, 6043: 3146, 6044: 3146, 6045: 3146, 6046: 3146, \
         6047: 3146, 6048: 3146, 6049: 3146, 6051: 3146, 6052: 3146, 6053: 3146, 6054: 3146, 6055: 3146, 6056: 3146, 6074: 3146, \
         6075: 3146, 6076: 3146, 6077: 3146, 6078: 3146, 6079: 3146, 6081: 3146, 6082: 3146, 6083: 3146, 6084: 3146, 6086: 3146, \
         6087: 3146, 6088: 3146, 6089: 3146, 6090: 3146, 6513: 3146, 6514: 3146, 6515: 3146, 6516: 3146, 6549: 3146, 6550: 3146, \
         6551: 3146, 6552: 3146, 6561: 3146, 6562: 3146, 6563: 3146, 6564: 3146, 6569: 3146, 6570: 3146, 6571: 3146, 6572: 3146, \
         6263: 3146, 6264: 3146, 6265: 3146, 6266: 3146, 6283: 3146, 6284: 3146, 6285: 3146, 6286: 3146, 6323: 3146, 6324: 3146, \
         6327: 3146, 6328: 3146, 6329: 3146, 6330: 3146, 6331: 3146, 6332: 3146, 6334: 3146, 6335: 3146, 6336: 3146, 6337: 3146, \
         6338: 3146, 6339: 3146, 6340: 3146, 6341: 3146, 6342: 3146, 6343: 3146, 6344: 3146, 6345: 3146, 6346: 3146, 6347: 3146, \
         6348: 3146, 6349: 3146, 6350: 3146, 6353: 3146, 6354: 3146, 6356: 3146, 6357: 3146, 6358: 3146, 6359: 3146, 6360: 3146, \
         6377: 3146, 6378: 3146, 6380: 3146, 5117: 3146, 5118: 3146, 5119: 3146, 5120: 3146, 5121: 3146, 5122: 3146, 5123: 3146, \
         5124: 3146, 5125: 3146, 5126: 3146, 5127: 3146, 5128: 3146, 5129: 3146, 5130: 3146, 5131: 3146, 5132: 3146, 5133: 3146, \
         5134: 3146, 5135: 3146, 5136: 3146, 5137: 3146, 5138: 3146, 5139: 3146, 5140: 3146, 5141: 3146, 5142: 3146, 5143: 3146, \
         5144: 3146, 5145: 3146, 5146: 3146, 5147: 3146, 5148: 3146, 5149: 3146, 5150: 3146, 5151: 3146, 5152: 3146, 5153: 3146, \
         5154: 3146, 5155: 3146, 5156: 3146, 5157: 3146, 5158: 3146, 5159: 3146, 5160: 3146, 5161: 3146, 5162: 3146, 5163: 3146, \
         5164: 3146, 5166: 3146, 5167: 3146, 5168: 3146, 5169: 3146, 5170: 3146, 5171: 3146, 5172: 3146, 5173: 3146, 5174: 3146, \
         5175: 3146, 5176: 3146, 5177: 3146, 5178: 3146, 5179: 3146, 5180: 3146, 5181: 3146, 5182: 3146, 5183: 3146, 5184: 3146, \
         5185: 3146, 5186: 3146, 5187: 3146, 5188: 3146, 5189: 3146, 5190: 3146, 5191: 3146, 5192: 3146, 5193: 3146, 5194: 3146, \
         5195: 3146, 5196: 3146, 5197: 3146, 5198: 3146, 6050: 3146, 6073: 3146, 6080: 3146, 6085: 3146, 6333: 3146, 6351: 3146, \
         6352: 3146, 6355: 3146, 6379: 3146, 6005: 3147, 6006: 3147, 6007: 3147, 6008: 3147, 6009: 3147, 6010: 3147, 6011: 3147, \
         6012: 3147, 6013: 3147, 6014: 3147, 6015: 3147, 6016: 3147, 6017: 3147, 6018: 3147, 6019: 3147, 6020: 3147, 6057: 3147, \
         6058: 3147, 6059: 3147, 6060: 3147, 6061: 3147, 6062: 3147, 6063: 3147, 6064: 3147, 6065: 3147, 6066: 3147, 6068: 3147, \
         6069: 3147, 6070: 3147, 6071: 3147, 6072: 3147, 6517: 3147, 6518: 3147, 6519: 3147, 6520: 3147, 6521: 3147, 6522: 3147, \
         6523: 3147, 6524: 3147, 6525: 3147, 6526: 3147, 6527: 3147, 6528: 3147, 6529: 3147, 6530: 3147, 6531: 3147, 6532: 3147, \
         6533: 3147, 6534: 3147, 6535: 3147, 6537: 3147, 6538: 3147, 6540: 3147, 6541: 3147, 6542: 3147, 6543: 3147, 6545: 3147, \
         6546: 3147, 6547: 3147, 6548: 3147, 6553: 3147, 6554: 3147, 6555: 3147, 6556: 3147, 6557: 3147, 6558: 3147, 6559: 3147, \
         6560: 3147, 6565: 3147, 6567: 3147, 6568: 3147, 6573: 3147, 6574: 3147, 6575: 3147, 6576: 3147, 6577: 3147, 6578: 3147, \
         6579: 3147, 6580: 3147, 6581: 3147, 6582: 3147, 6583: 3147, 6584: 3147, 6585: 3147, 6586: 3147, 6588: 3147, 6589: 3147, \
         6591: 3147, 6592: 3147, 6594: 3147, 6595: 3147, 6596: 3147, 6597: 3147, 6598: 3147, 6599: 3147, 6600: 3147, 6601: 3147, \
         6602: 3147, 6603: 3147, 6604: 3147, 6605: 3147, 6606: 3147, 6607: 3147, 6608: 3147, 6609: 3147, 6610: 3147, 6611: 3147, \
         6612: 3147, 6613: 3147, 6615: 3147, 6616: 3147, 6617: 3147, 6618: 3147, 6619: 3147, 6620: 3147, 6621: 3147, 6622: 3147, \
         6623: 3147, 6624: 3147, 6625: 3147, 6626: 3147, 6627: 3147, 6628: 3147, 6629: 3147, 6630: 3147, 6631: 3147, 6632: 3147, \
         6633: 3147, 6634: 3147, 6635: 3147, 6636: 3147, 6251: 3147, 6253: 3147, 6254: 3147, 6256: 3147, 6257: 3147, 6258: 3147, \
         6259: 3147, 6260: 3147, 6261: 3147, 6262: 3147, 6279: 3147, 6280: 3147, 6281: 3147, 6282: 3147, 6289: 3147, 6290: 3147, \
         6291: 3147, 6292: 3147, 6293: 3147, 6296: 3147, 6297: 3147, 6298: 3147, 6299: 3147, 6300: 3147, 6301: 3147, 6302: 3147, \
         6303: 3147, 6304: 3147, 6305: 3147, 6307: 3147, 6308: 3147, 6309: 3147, 6310: 3147, 6311: 3147, 6312: 3147, 6313: 3147, \
         6314: 3147, 6315: 3147, 6316: 3147, 6317: 3147, 6318: 3147, 6319: 3147, 6320: 3147, 6321: 3147, 6322: 3147, 6325: 3147, \
         6361: 3147, 6363: 3147, 6364: 3147, 6365: 3147, 6366: 3147, 6367: 3147, 6368: 3147, 6369: 3147, 6371: 3147, 6372: 3147, \
         6373: 3147, 6376: 3147, 6381: 3147, 6382: 3147, 6383: 3147, 6384: 3147, 6385: 3147, 6386: 3147, 6387: 3147, 6389: 3147, \
         6391: 3147, 6392: 3147, 6393: 3147, 6394: 3147, 6395: 3147, 6396: 3147, 6397: 3147, 6398: 3147, 6399: 3147, 6400: 3147, \
         5301: 3147, 5302: 3147, 5303: 3147, 5304: 3147, 5305: 3147, 5306: 3147, 5307: 3147, 5308: 3147, 5309: 3147, 5310: 3147, \
         5311: 3147, 5312: 3147, 5313: 3147, 5314: 3147, 5315: 3147, 5316: 3147, 5317: 3147, 5318: 3147, 5329: 3147, 5330: 3147, \
         5331: 3147, 5332: 3147, 5333: 3147, 5334: 3147, 5335: 3147, 5336: 3147, 5337: 3147, 5338: 3147, 5339: 3147, 5340: 3147, \
         5341: 3147, 5342: 3147, 5343: 3147, 5344: 3147, 5345: 3147, 5346: 3147, 5347: 3147, 5348: 3147, 5349: 3147, 5350: 3147, \
         5351: 3147, 5352: 3147, 5353: 3147, 5354: 3147, 5355: 3147, 5356: 3147, 5357: 3147, 5358: 3147, 5359: 3147, 5360: 3147, \
         5361: 3147, 5362: 3147, 5363: 3147, 5364: 3147, 5101: 3147, 5102: 3147, 5104: 3147, 5105: 3147, 5106: 3147, 5107: 3147, \
         5108: 3147, 5109: 3147, 5110: 3147, 5111: 3147, 5112: 3147, 5113: 3147, 5114: 3147, 5115: 3147, 5116: 3147, 5165: 3147, \
         5199: 3147, 5200: 3147, 5201: 3147, 5202: 3147, 5203: 3147, 5204: 3147, 5205: 3147, 5206: 3147, 5207: 3147, 5208: 3147, \
         6067: 3147, 6536: 3147, 6539: 3147, 6544: 3147, 6566: 3147, 6587: 3147, 6590: 3147, 6593: 3147, 6614: 3147, 6252: 3147, \
         6255: 3147, 6287: 3147, 6288: 3147, 6294: 3147, 6295: 3147, 6306: 3147, 6326: 3147, 6362: 3147, 6374: 3147, 6375: 3147, \
         6388: 3147, 6390: 3147, 6151: 3148, 6152: 3148, 6153: 3148, 6154: 3148, 6155: 3148, 6156: 3148, 6157: 3148, 6158: 3148, \
         6159: 3148, 6160: 3148, 6202: 3148, 6203: 3148, 6204: 3148, 6205: 3148, 6206: 3148, 6207: 3148, 6208: 3148, 6209: 3148, \
         6210: 3148, 6211: 3148, 6212: 3148, 6213: 3148, 6214: 3148, 6215: 3148, 6216: 3148, 6217: 3148, 6218: 3148, 6219: 3148, \
         6220: 3148, 6221: 3148, 5401: 3148, 5402: 3148, 5001: 3148, 5002: 3148, 5003: 3148, 5004: 3148, 5005: 3148, 5006: 3148, \
         5007: 3148, 5008: 3148, 5009: 3148, 5010: 3148, 5011: 3148, 5012: 3148, 6201: 3148, 6222: 3148, 4101: 3149, 4102: 3149, \
         4103: 3149, 4104: 3149, 4105: 3149, 4106: 3149, 4107: 3149, 4108: 3149, 4001: 3149, 4002: 3149, 4003: 3149, 4005: 3149, \
         4006: 3149, 4007: 3149, 4008: 3149, 6501: 3149, 6502: 3149, 6503: 3149, 6504: 3149, 6505: 3149, 6506: 3149, 6507: 3149, \
         6508: 3149, 6509: 3149, 6511: 3149, 6512: 3149, 6267: 3149, 6268: 3149, 6269: 3149, 6270: 3149, 6271: 3149, 6272: 3149, \
         6273: 3149, 6274: 3149, 6275: 3149, 6276: 3149, 6277: 3149, 6278: 3149, 4004: 3149, 5319: 3149, 5320: 3149, 5321: 3149, \
         5322: 3149, 5323: 3149, 5324: 3149, 5325: 3149, 5326: 3149, 5327: 3149, 5328: 3149, 6510: 3149, \
         'Place sans numéro1': 3150, 6370: 3150, 5103: 3150}

def BDDnoID(pl):
        if pl <= 5012:
                if pl == 5001:
                        return 46610
                return pl-5002 + 48889
        elif pl <= 5208 :
                if pl == 5101:
                        return 46611
                return pl-5102+48900
        elif pl <= 5399:
                if pl == 5301:
                        return 46607
                return pl-5302 + 49007
        elif pl <= 5499:
                if pl == 5401:
                        return 46600
                return pl-5402 + 49070
        elif pl <= 6090:
                if pl == 6001:
                        return 46614
                return 49071+pl-6002
        elif pl <= 6160:
                if pl == 6151:
                        return 46608
                return 49160+pl-6152
        elif pl <= 6222:
                if pl == 6201:
                        return 46609
                return 49169+pl-6202
        elif pl <= 6400:
                if pl == 6251:
                        return 46613
                return 49190+pl-6252
        elif pl >= 6000:
                if pl == 6501:
                        return 46612
                return 49339+pl-6502


        return ()
