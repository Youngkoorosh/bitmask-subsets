# bitmask-subsets

Generates all subsets of `{1, 2, ..., n}` using bitmasking.

## 📌 Description

This script prints every possible subset of the set `{1, 2, ..., n}`.  
It uses bitmasking to efficiently enumerate all combinations without recursion.

Example for `n = 3`:

```bash
{}
{1}
{2}
{1, 2}
{3}
{1, 3}
{2, 3}
{1, 2, 3}
```

## 🧠 How It Works

- Each integer `mask` from `0` to `2ⁿ - 1` represents a subset.
- The `i`-th bit in `mask` determines whether element `i + 1` is included.
- Output is formatted as `{a, b, c}` with minimal spacing.

## 🚀 Usage

```bash
python bitmask_subsets.py
```
Then enter a positive integer n when prompted.

# 🛠 Example
Input:
4

Output:
{}
{1}
{2}
{1, 2}
{3}
{1, 3}
...
{1, 2, 3, 4}

# 📁 File Structure
bitmask_subsets.py   # Main script
README.md            # Project description

# 🧪 Notes

* No external libraries required.

* Works for any reasonable n (e.g. n ≤ 20).

* Output is sorted by subset size and binary mask order.

### Feel free to fork, modify, or integrate into your own combinatorics toolkit.

### Let me know if you want a version with input validation or command-line arguments.
