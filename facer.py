MOD = 1000000007

def count_distinct_numbers(N):
    # Convert hexadecimal number to list of digits
    digits = list(N)
    n = len(digits)

    # Initialize a set to keep track of distinct numbers
    distinct_numbers = set()

    # Generate all subsequences of the given number
    for i in range(1, 1 << n):
        subseq = []
        for j in range(n):
            if i & (1 << j):
                subseq.append(digits[j])

        # Sort the subsequence and convert it to a number
        subseq.sort()
        num = int("".join(subseq), 16)

        # Add the number to the set of distinct numbers
        distinct_numbers.add(num)

    # Return the count of distinct numbers modulo 10^9+7
    return len(distinct_numbers) % MOD

# Sample input
N =input()

# Count the distinct numbers that can be made from N
count = count_distinct_numbers(N)

# Print the count of distinct numbers and the distinct numbers themselves
print(count)
distinct_numbers = set()
digits = list(N)
n = len(digits)
for i in range(1, 1 << n):
    subseq = []
    for j in range(n):
        if i & (1 << j):
            subseq.append(digits[j])
    subseq.sort()
    num = int("".join(subseq), 16)
    distinct_numbers.add(num)
print(distinct_numbers)
