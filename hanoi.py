import sys

PROP_PREFIX = "Propositions:"
FREE_DISK = "f_"
ON_PEG = "_op_"
EMPTY_PEG = "e_"
ABOVE_DISK = "_ab_"
SPACE_CHAR = " "
ACTIONS = "Actions:"
NAME = "Name: "
PRE = "pre: "
ADD = "add: "
DELETE = "delete: "
MOVE = "m_"
FROM = "_f_"
TO_PEG = "_tp_"

INITIAL_STATE = "Initial state: "
GOAL_STATE = "Goal state: "



def create_domain_file(domain_file_name, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    domain_file = open(domain_file_name, 'w')  # use domain_file.write(str) to write to domain_file

    domain_file.write(PROP_PREFIX + "\n")

    # all props where disk is on top of peg's base
    for p in pegs:
        for d in disks:
            domain_file.write(d + ON_PEG + p + SPACE_CHAR)

    # all prop where disk is free (no disk above)
    for d in disks:
        domain_file.write(FREE_DISK + d + SPACE_CHAR)

    # all prop where peg is empty
    for p in pegs:
        domain_file.write(EMPTY_PEG + p + SPACE_CHAR)

    # all prop where disk is on top of disk
    for i in range(n_):
        for j in range(i + 1, n_):
            domain_file.write(disks[i] + ABOVE_DISK + disks[j] + SPACE_CHAR)

    domain_file.write("\n" + ACTIONS + "\n")

    # writing the move small disk to bigger disk action
    for i in range(n_):
        for j in range(i+1, n_):
            for k in range(i+1, n_):
                if k == j:
                    continue
                # action name
                domain_file.write(NAME + MOVE + disks[i] + FROM + disks[j] + ABOVE_DISK + disks[k] + "\n")
                # action pre
                domain_file.write(PRE + FREE_DISK + disks[i] + SPACE_CHAR)
                domain_file.write(FREE_DISK + disks[k] + SPACE_CHAR)
                domain_file.write(disks[i] + ABOVE_DISK + disks[j])
                domain_file.write("\n")
                # action add
                domain_file.write(ADD + FREE_DISK + disks[j] + SPACE_CHAR)
                domain_file.write(disks[i] + ABOVE_DISK + disks[k])
                domain_file.write("\n")
                # action delete
                domain_file.write(DELETE + FREE_DISK + disks[k] + SPACE_CHAR)
                domain_file.write("\n")

    # writing the move peg to peg action
    for i in range(m_):
        for j in range(m_):
            for k in range(n_):
                if i == j:
                    continue
                # action name
                domain_file.write(NAME + MOVE + disks[k] + FROM + pegs[i] + TO_PEG + pegs[j] + "\n")
                # action pre
                domain_file.write(PRE + FREE_DISK + disks[k] + SPACE_CHAR)
                domain_file.write(EMPTY_PEG + pegs[j] + SPACE_CHAR)
                domain_file.write(disks[k] + ON_PEG + pegs[i] + SPACE_CHAR)
                domain_file.write("\n")
                # action add
                domain_file.write(ADD + disks[k] + ON_PEG + pegs[j] + SPACE_CHAR)
                domain_file.write(EMPTY_PEG + pegs[i] + SPACE_CHAR)
                domain_file.write("\n")
                # action delete
                domain_file.write(DELETE + EMPTY_PEG + pegs[j] + SPACE_CHAR)
                domain_file.write(disks[k] + ON_PEG + pegs[i] + SPACE_CHAR)
                domain_file.write("\n")

    # move from peg's base to empty disk
    for p in pegs:
        for i in range(n_):
            for j in range(i+1, n_):
                # action name
                domain_file.write(NAME + MOVE + disks[i] + FROM + p + ABOVE_DISK + disks[j] + "\n")
                # action pre
                domain_file.write(PRE + FREE_DISK + disks[i] + SPACE_CHAR)
                domain_file.write(FREE_DISK + disks[j] + SPACE_CHAR)
                domain_file.write(disks[i] + ON_PEG + p + SPACE_CHAR)
                domain_file.write("\n")
                # action add
                domain_file.write(ADD + disks[i] + ABOVE_DISK + disks[j] + SPACE_CHAR)
                domain_file.write(EMPTY_PEG + p + SPACE_CHAR)
                domain_file.write("\n")
                # action delete
                domain_file.write(DELETE + FREE_DISK + disks[j] + SPACE_CHAR)
                domain_file.write(disks[i] + ON_PEG + p + SPACE_CHAR)
                domain_file.write("\n")

    # move from disk to empty peg
    for p in pegs:
        for i in range(n_):
            for j in range(i+1, n_):
                # action name
                domain_file.write(NAME + MOVE + disks[i] + FROM + disks[j] + TO_PEG + p + "\n")
                # action pre
                domain_file.write(PRE + FREE_DISK + disks[i] + SPACE_CHAR)
                domain_file.write(EMPTY_PEG + p + SPACE_CHAR)
                domain_file.write(disks[i] + ABOVE_DISK + disks[j] + SPACE_CHAR)
                domain_file.write("\n")
                # action add
                domain_file.write(ADD + FREE_DISK + disks[j] + SPACE_CHAR)
                domain_file.write(disks[i] + ON_PEG + p + SPACE_CHAR)
                domain_file.write("\n")
                # action delete
                domain_file.write(DELETE + disks[i] + ABOVE_DISK + disks[j] + SPACE_CHAR)
                domain_file.write(EMPTY_PEG + p + SPACE_CHAR)
                domain_file.write("\n")



    domain_file.close()


def create_problem_file(problem_file_name_, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    problem_file = open(problem_file_name_, 'w')  # use problem_file.write(str) to write to problem_file
    "*** YOUR CODE HERE ***"
    problem_file.write(INITIAL_STATE)
    problem_file.write(disks[-1] + ON_PEG + pegs[0] + SPACE_CHAR)
    problem_file.write(FREE_DISK + disks[0] + SPACE_CHAR)
    for i in range(n_ - 2, -1, -1):
        problem_file.write(disks[i] + ABOVE_DISK + disks[i + 1] + SPACE_CHAR)

    for j in range(1, m_):
        problem_file.write(EMPTY_PEG + pegs[j] + SPACE_CHAR)
    problem_file.write("\n")

    problem_file.write(GOAL_STATE)
    problem_file.write(disks[-1] + ON_PEG + pegs[-1] + SPACE_CHAR)
    for i in range(n_ - 2, -1, -1):
        problem_file.write(disks[i] + ABOVE_DISK + disks[i + 1] + SPACE_CHAR)

    problem_file.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: hanoi.py n m')
        sys.exit(2)

    n = int(float(sys.argv[1]))  # number of disks
    m = int(float(sys.argv[2]))  # number of pegs

    domain_file_name = 'hanoi_%s_%s_domain.txt' % (n, m)
    problem_file_name = 'hanoi_%s_%s_problem.txt' % (n, m)

    create_domain_file(domain_file_name, n, m)
    create_problem_file(problem_file_name, n, m)
