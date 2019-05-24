import sys

PROP_PREFIX = "Propositions:"
ON_FLOOR = "f_"
EMPTY_PEG = "e_"
ABOVE_DISK = "_ab_"
SPACE_CHAR = " "
ACTIONS = "Actions:"
NAME = "Name:"
PRE = "pre:"
ADD = "add:"
DELETE = "delete:"
MOVE = "m_"



def create_domain_file(domain_file_name, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    domain_file = open(domain_file_name, 'w')  # use domain_file.write(str) to write to domain_file

    domain_file.write(PROP_PREFIX + "\n")

    # all prop where disk is on floor (not above disk)
    for d in disks:
        domain_file.write(ON_FLOOR + d + SPACE_CHAR)

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
        for j in range(i + 1, n_):
            domain_file.write(NAME + MOVE + disks[i] + ABOVE_DISK + disks[j] + SPACE_CHAR + "\n")


    domain_file.close()


def create_problem_file(problem_file_name_, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    problem_file = open(problem_file_name_, 'w')  # use problem_file.write(str) to write to problem_file
    "*** YOUR CODE HERE ***"



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
