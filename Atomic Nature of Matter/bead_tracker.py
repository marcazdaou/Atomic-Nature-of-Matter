import math
import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Entry point
def main():
    P = int(sys.argv[1])  # Accept command-line arguments pixels (int)
    # tau (float)
    # delta (float)
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    files = sys.argv[4:]
    # constructing BlobFinder object from fame sys.argv[4]

    prevBeads = BlobFinder(Picture(files[0]), tau).getBeads(P)

    # get a list of beads named prevBeads
    for i in range(1, len(files)):

        currBeads = prevBeads  # Set prevBeads to currBeads

        prevBeads = BlobFinder(Picture(files[i]), tau).getBeads(P)

        for currbead in currBeads:  # For each bead currBead in currBeads,

            dist = min(currbead.distanceTo(other) for other in prevBeads)
# find a bead prevBead from prevBeads not further than delta and closest to
# currBead

            if dist <= delta:
                # if such a bead is found, write its distance to currBead.
                stdio.writef('%.4f\n', dist)
        stdio.writeln()  # Write a newline character.


if __name__ == '__main__':
    main()
