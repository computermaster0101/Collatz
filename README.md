# Number Patterns in Collatz Conjecture

## Introduction

The Collatz conjecture is a famous unsolved mathematical problem that explores the behavior of sequences generated by applying specific rules to positive integers. In this README, we discuss some interesting patterns related to the Collatz conjecture.

## The Collatz Conjecture
The Collatz Conjecture, also known as the 3n+1 conjecture, is an unsolved mathematical problem that revolves around a simple rule applied to positive integers. Starting with any positive integer n:

If n is even, divide it by 2 (n/2).
If n is odd, multiply it by 3 and add 1 (3n+1).
Repeat these steps with the resulting number. The conjecture posits that, regardless of the initial positive integer chosen, this process will eventually reach the number 1, and from there, it will cycle through the sequence 4, 2, 1, 4, 2, 1, and so on indefinitely.

While the Collatz Conjecture is easy to understand and has been tested for vast numbers, it remains unproven whether this sequence indeed always reaches 1 for every positive integer or if there are exceptions. This unsolved problem continues to intrigue mathematicians and computer scientists.


### Key Observations

1. Any two odd numbers, when multiplied, will result in an odd number.
2. Any even number can be divided by 2 repeatedly until it becomes odd.
3. Any odd number, when increased or decreased by 1, will become even.

### Another Perspective: Odds Only
While exploring the Collatz Conjecture, it's fascinating to note that every number, when passed through the Conjecture's logic, eventually becomes even. Similarly, any even number can be repeatedly divided by 2 until it becomes an odd number. This observation opens up a different angle of analysis: what happens when we focus exclusively on odd numbers within the Collatz sequence?

### The "exposeOdds.py" Script
In pursuit of this perspective, I've created the "exposeOdds.py" script, which you can find in this repository. This script is designed to extract and analyze the behavior of odd numbers in the Collatz sequence, offering a unique insight into their progression and patterns.

### Why Examine Odd Numbers?
Simplicity: By narrowing our focus to odd numbers, we simplify the Collatz Conjecture's sequence while still maintaining its core characteristics.

Potential Insights: Examining odd numbers exclusively may reveal hidden patterns, cycles, or behaviors that are not immediately evident when considering the entire sequence.

Reduced Complexity: This approach reduces the number of points for review, potentially making it easier to identify and analyze specific trends.

### How to Use the "exposeOdds.py" Script
To explore the behavior of odd numbers within the Collatz Conjecture using the `exposeOdds.py` script, follow these steps:

1. **Input Options**: You have two options for input:

   - **Single Number**: Enter a single positive odd number (e.g., 7).
   - **Number Range**: Enter a range of numbers in the format "start, end" (e.g., 1, 10) to analyze the Collatz Conjecture for all odd numbers within the specified range.

2. **Run the Script**: Open a terminal or command prompt, navigate to the script's directory, and execute the script by running:

   ```shell
   python exposeOdds.py
   ```
3. Review the Output: The script will generate and display Collatz sequences for the odd numbers you specified, providing insights into their behavior.

By following these steps, you can effectively utilize the exposeOdds.py script to investigate the behavior of odd numbers within the Collatz Conjecture, whether you're analyzing a single number or a range of numbers.

#### Positive Odd Numbers

- When a positive odd number is increased by 1, the output of the pattern will eventually reach an odd number or 1 when repeatedly divided by 2.

#### Negative Odd Numbers

- When a negative odd number is increased by 1, the output of the pattern has the potential to end in a different prime number.

#### Positive Odd Numbers (Decreased by 1)

- When a positive odd number is decreased by 1, the output of the pattern has the potential to end in a different prime number.

#### Negative Odd Numbers (Increased by 1)

- When a negative odd number is increased by 1, the output of the pattern will eventually reach an odd number or 1 when repeatedly divided by 2.

## Conclusions

Following these rules, we can make the following conclusions:

- Any positive number, when passed through the "x3p1" function (Collatz conjecture with increased by 1), will eventually reach 1.

- Any negative number, when passed through the "x3m1" function (Collatz conjecture with decreased by 1), will eventually reach 1.

## Open Questions

- Can the final prime number in the pattern for positive numbers passed through the "x3m1" function be determined without performing the iterative function?
- Can the final prime number in the pattern for negative numbers passed through the "x3p1" function be determined without performing the iterative function?

### Note

The final prime number in the pattern for positive numbers passed through the "x3m1" function cannot be determined without performing the iterative function. The Collatz conjecture, which includes the "x3m1" function, is an unsolved mathematical problem, and it is not known whether every sequence eventually reaches the number 1 (and therefore, ends in a prime number) for all positive integers.

Similarly, the final prime number in the pattern for negative numbers passed through the "x3p1" function also cannot be determined without performing the iterative function. The Collatz conjecture applies to both positive and negative integers, and it is still an open question whether the "x3p1" function always leads to the number 1 (ending in a prime number) for all negative integers.

To date, extensive computational searches have been conducted, and the Collatz conjecture has been verified for an extremely large range of integers, but a general proof or disproof remains elusive for both positive and negative integers.
