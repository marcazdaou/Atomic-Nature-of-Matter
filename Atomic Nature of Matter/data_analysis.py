import math
import stdio


# Entry point.
def main():
    # Initialize ETA, RHO, T, and R to appropriate values.
    ETA = 9.135e-4
    RHO = 5e-7
    T = 297.0
    R = 8.31457
    n = 0
    METERS_PER_PIXEL = 1.75e-7
    while not (stdio.isEmpty()):  # as long as it is not empty
        displacements = stdio.readAllFloats()  # standard input
        # Calculate var as the sum of the
        # squares of the n displacements read from standard input
        var = (sum(map(lambda r: (METERS_PER_PIXEL * r) ** 2, displacements)))
        var = var / (2 * len(displacements))  # Divide var by 2 * n.
        n += 1
        k = (6 * math.pi * var * ETA * (RHO / T))  # 6 * math.pi * var * ETA * RHO / T.
        N_A = R / k  # Estimate Avogadro’s constant as R / k.
        # Write to standard output the two constants in scientific notation  and
        # separated by a space.
        stdio.write('%e' % k)
        stdio.write(" ")
        stdio.write('%e' % N_A)
        stdio.writeln()


if __name__ == '__main__':
    main()
