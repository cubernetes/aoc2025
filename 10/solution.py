import re

lines = open(0).read().splitlines()

def next_pivot(equations, index):
    new_equations = []
    offset = -1
    for offset in range(index):
        new_equations.append(equations[offset])
    equation_to_move = None
    while equation_to_move is None:
        pending_equations = []
        equation_to_move = None
        for i, eq in enumerate(equations[offset + 1:]):
            i += offset + 1
            if eq[0][index] != 0 and equation_to_move is None:
                equation_to_move = eq
            else:
                pending_equations.append(eq)
        if equation_to_move is not None:
            break
        index += 1
        if index >= len(eq[0]):
            break
    if equation_to_move is not None:
        new_equations.append(equation_to_move)
    new_equations.extend(pending_equations)

    # for eq in new_equations:
    #     if eq == equation_to_move:
    #         print(f'\033[31m{eq}\033[m')
    #     else:
    #         print(eq)
    # print()

    return new_equations

for i, line in enumerate(lines[:1]):
    # Make parsing easier
    line = re.sub(r'\((\d+)\)', r'(\1,)', line)

    _, *buttons, joltage_reqs = line.split()

    # Parse
    _ = _[1:-1]
    buttons = [eval(x) for x in buttons]
    joltage_reqs = list(map(int, joltage_reqs[1:-1].split(',')))

    # I know, could be solved using scipy or sympy and numpy and whatnot.
    # Or using real linear algebra.
    # But no, we do it by HAND!

    # Build system of linear equations
    equations = []
    for i, rhs in enumerate(joltage_reqs):
        equations.append([[0] * (len(buttons) + 1),[0] * (len(buttons) + 1)])
        for j, button in enumerate(buttons):
            if i in button:
                equations[-1][0][j] = 1
            else:
                equations[-1][0][j] = 0
        equations[-1][1][-1] = rhs

    # Gaussian eliminiation (-> row echelon form)
    pivot_offset = 0
    for i in range(len(equations)):
        if i < len(equations[i][0]):
            # Permute rows, s.t. we have a non-zero value at the pivot-index (starting at 0)
            equations = next_pivot(equations, i)
        else:
            break
        if equations[i][0][i + pivot_offset] == 0:
            # There might be a bug here!!!
            pivot_offset += 1
            while i + pivot_offset < len(equations[i][0]) and equations[i][0][i + pivot_offset] == 0: # Pivot is not perfectly 1-below and 1-right. Search further to the right
                pivot_offset += 1
            if i + pivot_offset >= len(equations[i][0]): # No more pivots!
                break
        pivot = i + pivot_offset

        # Isolate the respective variable by substracting all
        # trailing variables (and a potential constant) from the
        # lhs and the rhs. If i + 1 is too big, nothing will happen
        # (more constraints than there are variables/buttons).
        for offset, var in enumerate(equations[i][0][pivot + 1:]):
            equations[i][0][pivot + 1 + offset] = 0
            equations[i][1][pivot + 1 + offset] -= var # substract
            equations[i][1][pivot + 1 + offset] /= equations[i][0][pivot] if equations[i][0][pivot] != 0 else 1 # normalize, unless divisor is 0
        equations[i][0][pivot] = 1 if equations[i][0][pivot] != 0 else 0 # must be 1, unless it's already 0

        # Substract the row from all rows below
        for j in range(len(equations[i+1:])):
            j += i + 1
            multiplier = equations[j][0][pivot]
            for k in range(len(equations[j][1])):
                equations[j][1][k] -= equations[i][1][k] * multiplier
            equations[j][0][pivot] = 0

    # Determine border conditions that minimize each variable:
    border_conditions = []
    for eq in equations:
        border_conditions.append([0] * (len(buttons) + 1))
        for i, var in enumerate(eq[1]):
            border_conditions[-1][i] = -var
        border_conditions[-1][-1] *= -1

    # This might give something like this (header only for reference):
    #  x1 x2 x3 x4 x5 x6 rhs
    # [0, 1, 0, 1, 0, 0, 7]
    # [0, 0, 0, 0, 0, 1, 5]
    # [0, 0, 0, 1, 1, 0, 4]
    # [0, 0, 0, 0, 0, 1, 3]
    # Which represents this system:
    # x2 + x4 <= 7
    # x6 <= 5
    # x4 + x5 <= 4
    # x6 <= 3
    # We might use mixed integer linear programming to solve this system of linear inequalities

    # for b in border_conditions:
    #     print(b)

    for b in border_conditions:
        pretty = []
        for i, var in enumerate(b[:-1]):
            if var > 0:
                if var % 1 == 0:
                    var = round(var)
                if var == 1:
                    pretty.append(f' + x{i + 1}')
                else:
                    pretty.append(f' + {var}*x{i + 1}')
            elif var < 0:
                if var % 1 == 0:
                    var = round(var)
                if var == -1:
                    pretty.append(f' - x{i + 1}')
                else:
                    pretty.append(f' - {-var}*x{i + 1}')
        if b[-1] % 1 == 0:
            print(re.sub('^- ', '-', ''.join(pretty).removeprefix(' + ').removeprefix(' ') or '0') + ' <= ' + str(round(b[-1])))
        else:
            print(re.sub('^- ', '-', ''.join(pretty).removeprefix(' + ').removeprefix(' ') or '0') + ' <= ' + str(b[-1]))
    print()

    A = []
    x = []
    for b in border_conditions:
        A.append(b[:-1])
        x.append(b[-1])
    #print(A)
    #print(x)
    #print(solve_integer_milp_sum_min(A, x, fallback_ub=50))

    for eq in equations:
        print(eq)
    print()

