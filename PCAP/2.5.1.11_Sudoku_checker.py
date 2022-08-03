# PCAP preparation
# ===================
# 📆 2022-07-05 10:36:04

sudoku_in = '''295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672'''

# sudoku_in = '''195743862
# 431865927
# 876192543
# 387459216
# 612387495
# 549216738
# 763524189
# 928671354
# 254938671'''


# 1. Read original data and store them into list of rows
def read_and_store(data_string):
    acc = []
    ds = data_string.split('\n')
    for r in ds:
        tmp = []
        for c in r:
            tmp.append(int(c))
        acc.append(tmp)
    return acc

# 2. For transposing 2D list - I need this for columns checking
def list_transpose(my_list):
    acc_t =[]
    for i in range(len(my_list)):
        tmp = []
        for r in my_list:
            tmp.append(r[i])
        acc_t.append(tmp)
    return acc_t

# 3. Define matrix slices of 3x3
def get_sub_lists(my_l, dim_l, dim_s):
    acc_s = []
    for row in range(0,dim_l,dim_s):
        for col in range(0,dim_l,dim_s):
            tmp = []
            for r in range(row,row+dim_s):
                for c in range(col, col+dim_s):
                    if my_l[r][c]:
                        tmp.append(my_l[r][c])
            acc_s.append(tmp)
    return acc_s

# 4. Checking the sum of rows or columns
# ---------------------------------------------------
# This one is universal for rows, columns and slices

def check_sum(my_list, my_dim):
    cn = 0
    cs = sum(range(my_dim+1))

    for r in my_list:
        if len(r) == my_dim and sum(r) == sum(set(r)) == cs :
            cn += 1
    if len(my_list) == cn:
        return True

res = read_and_store(sudoku_in)
grid = list(zip(*res))

# Checking
# ------------------
# for r in res:
    # print(r)
# print('\n\n')
# for g in grid:
    # print(g)
# exit()
# ------------------

# MAIN FUNCTION
def check_sudoku(sudoku_list, p=0):
    # Read original data into list of rows
    res = read_and_store(sudoku_list)
    if p:
        print('Original data')
        for o in res:
            print(o)

    # Transpose the list of rows into list of columns
    res_c = list_transpose(res)
    if p:
        print('\nTransposed data')
        for c in res_c:
            print(c)

    # Get Sub lists into one line of list
    sub_l = get_sub_lists(res,9,3)
    if p:
        print('\nSlices')
        for s in sub_l:
            print(s)

    # REPORTING PART
    #--------------------------------------------------------------
    ok_cn = 0
    # Check if sums of rows and columns are OK
    if check_sum(res,9) + check_sum(res_c,9):
        print('\n✔ Rows and columns are OK')
        ok_cn += 1
    if check_sum(sub_l,9):
        print('✔ Slices are OK, too')
        ok_cn += 1
    else:
        print('❌ but not sublists')
        ok_cn -= 1

    if ok_cn:
        print('👍 SUDOKU APPROVED!\n')

check_sudoku(sudoku_in,1)
