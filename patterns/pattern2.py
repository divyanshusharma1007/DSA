import logging
import sys


logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
    stream=sys.stdout,
)

logger = logging.getLogger(__name__)

n = 5
nums = "".join(str(num) for num in range(1, n + 1))

logger.info("Pattern 2: increasing number triangle")
logger.info("State reminder: n=%s, each row i prints numbers from 1 to i", n)
print()

# Approach 1: nested for loops
logger.info("Approach 1: nested for loops")
for i in range(1, n + 1):
    row = ""
    # logger.info("Start row: i=%s, j will run from 1 to %s", i, i)

    for j in range(1, i + 1):
        row += str(j)
        # logger.info("Inner state: i=%s, j=%s, row_so_far=%s", i, j, row)

    print(row)
    # logger.info("Completed row: i=%s, printed_row=%s", i, row)

print()

# Approach 2: string slicing
logger.info("Approach 2: string slicing")
logger.info("Base string state: nums=%s; each row is nums[:i]", nums)
for i in range(1, n + 1):
    row = nums[:i]
    # logger.info("Slice state: i=%s, nums[:%s]=%s", i, i, row)
    print(row)

print()

# Approach 3: while loops
logger.info("Approach 3: while loops")
i = 1

while i <= n:
    j = 1
    row = ""
    # logger.info("Outer while state: i=%s, reset j=%s", i, j)

    while j <= i:
        row += str(j)
        # logger.info("Inner while state: i=%s, j=%s, row_so_far=%s", i, j, row)
        j += 1

    print(row)
    # logger.info("Completed row: i=%s, printed_row=%s, next_i=%s", i, row, i + 1)
    i += 1

print()

# Approach 4: one print statement
logger.info("Approach 4: one print statement")
rows = []

for i in range(1, n + 1):
    row = "".join(str(j) for j in range(1, i + 1))
    rows.append(row)
    # logger.info("Generated row state: i=%s, row=%s, rows_so_far=%s", i, row, rows)

print("\n".join(rows))

print()

# Approach 5: print unpacking
logger.info("Approach 5: print unpacking")
for i in range(1, n + 1):
    values = list(range(1, i + 1))
    # logger.info("Unpacking state: i=%s, values=%s, sep=''", i, values)
    print(*values, sep="")

print()
logger.info("Completed printing Pattern 2 with all approaches")
