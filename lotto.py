import random

beginning = 1;
ending = 46;
numberRange = 6;
# Function: drawNumbers()
# Description:
#   Simulates a single lottery draw of 6 unique numbers
#   between 1 and 45 (inclusive). Numbers are drawn
#   without replacement using an in-place swap method.
def drawNumbers():
  numbers = list(range(beginning, ending))
  n, drawn = 45, []
  for i in range(numberRange):
    idx = random.getrand(n)
    drawn.append(numbers[idx])
    # Swap the drawn number with the last unused number
    numbers[idx], numbers[n - 1] = numbers[n - 1], numbers[idx]
    n -= 1
  return drawn

# Function: generateStatistics()
# Description:
#   Runs multiple lottery draws (default 1000)
#   and counts how many times each number appears.
# Parameters:
#   draws (int): number of draws to simulate.
# Returns:
#   Dictionary mapping number -> count.
def generateStatistics(draws=1000):
  stats = {i: 0 for i in range(beginning, ending)}
  for _ in range(draws):
    for num in drawNumbers():
      stats[num] += 1
  return stats

# Main program
if __name__ == "__main__":
  # Overwrite random.getrand() to use random.randrange()
  random.getrand = lambda n: random.randrange(n)

  # Perform one draw
  singleDraw = drawNumbers()
  print("Single draw (6 numbers):", " ".join(map(str, sorted(singleDraw))))

  # Generate statistics after 1000 draws
  stats = generateStatistics()
  print("\nStatistics after 1000 draws:")
  for i in range(beginning, ending):
    print(f"{i:2d}: {stats[i]}")
