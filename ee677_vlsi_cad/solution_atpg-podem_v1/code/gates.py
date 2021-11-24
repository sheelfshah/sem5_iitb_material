from copy import deepcopy as dcopy
""" todos:
    change func names of these funcs, and correspondingly in other dependencies
    change code inside funcs
"""

def NAND2(out, in1, in2, g):
    if g == 0:
        if out == -5:
            return [out, in1, in2]
        if out == 0:
            return [out, 1, 1]
        if out == 1:
            if in1 == 1:
                return [out, in1, 0]
            if in2 == 1:
                return [out, 0, in2]
            if in1 == 0:
                return [out, in1, in2]
            if in2 == 0:
                return [out, in1, in2]
        return [out, 0, 0]
    if in1 == -5 and in2 == -5:
        return [-5, in1, in2]
    if abs(in1 * in2) > 1:
        return [-5, in1, in2]
    return [int(not(in1 * in2)), in1, in2]

def NOT(out, in1, g):
    if g == 0:
        if out == -5:
            return [out, -5]
        return [out, int(not(out))]
    if in1 == -5:
        return [-5, in1]
    return [int(not(in1)), in1]

def AND(out, in1, in2, g):
    if g == 0:
        if out == -5:
            return [out, in1, in2]
        if out == 1:
            return [out, 1, 1]
        if out == 0:
            if in1 == 1:
                return [out, in1, 0]
            if in2 == 1:
                return [out, 0, in2]
            if in1 == 0:
                return [out, in1, in2]
            if in2 == 0:
                return [out, in1, in2]
        return [out, 0, 0]
    if in1 == -5 and in2 == -5:
        return [-5, in1, in2]
    if abs(in1 * in2) > 1:
        return [-5, in1, in2]
    return [in1 * in2, in1, in2]

def NAND4(out, in1, in2, in3, in4, g):
    if g == 0:
        if out == -5:
            return [out, -5, -5, -5, -5]
        if out == 0:
            return [out, 1, 1, 1, 1]
        return [out, 0, in2, in3, in4]
    if abs(in1 * in2 * in3 * in4) > 1:
        return [-5, in1, in2, in3, in4]
    return [int(not(in1 * in2 * in3 * in4)), in1, in2, in3, in4]

def update_row(value, row):
    updated_row = dcopy(row)
    if value == -5: 
        print('Value of V is not allowed')
        return updated_row
    gate = int(row[1])
    if gate == 1:
        updated_row[2:] =  NOT(value, row[3], 0)
    elif gate == 3:
        updated_row[2:] =  AND(value, row[3], row[4], 0)
    elif gate == 5:
        updated_row[2:] =  NAND2(value, row[3], row[4], 0)
    elif gate == 8:
        updated_row[2:] =  NAND4(value, row[3], row[4], row[5], row[6], 0)
    return updated_row

def update_row_imply(row_imply):
    updated_row = dcopy(row_imply)
    gate = int(row_imply[1]);
    if gate == 1:
        updated_row[2:] = NOT(updated_row[2], row_imply[3], 1)
    elif gate == 3:
        updated_row[2:] = AND(updated_row[2], row_imply[3], row_imply[4], 1)
    elif gate == 5:
        updated_row[2:] = NAND2(updated_row[2],row_imply[3], row_imply[4], 1) 
    elif gate == 8:
        updated_row[2:] = NAND4(updated_row[2], row_imply[3], row_imply[4],
            row_imply[5], row_imply[6], 1)
    return updated_row