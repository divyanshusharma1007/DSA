import logging
import sys


logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
    stream=sys.stdout,
)

logger = logging.getLogger(__name__)

size = 5

logger.info("Printing %s x %s star pattern using different approaches", size, size)
print()

# Approach 1: Simple loop with string multiplication
logger.info("Approach 1: Simple loop with string multiplication")
for _ in range(size):
    print("*" * size)

print()

# Approach 2: join with a list
logger.info("Approach 2: join with a list")
print("\n".join(["*" * size] * size))

print()

# Approach 3: join with a generator
logger.info("Approach 3: join with a generator")
print("\n".join("*" * size for _ in range(size)))

print()

# Approach 4: repeat the full row string
logger.info("Approach 4: repeat the full row string")
print((("*" * size) + "\n") * size, end="")

print()

# Approach 5: direct multiline string
logger.info("Approach 5: direct multiline string")
print("""*****
*****
*****
*****
*****""")

print()

# Approach 6: original nested-loop method
logger.info("Approach 6: original nested-loop method")
for i in range(size):
    for j in range(size):
        print("*", end="")
    print()

print()
logger.info("Completed printing all approaches")
