# Create topic folders
mkdir -p arrays two-pointers sliding-window strings

# Move files to topic folders
mv "128. Longest Consecutive Sequence.py" arrays/
mv "15. 3Sum.py" two-pointers/
mv "167. Two Sum II - Input Array Is Sorted.py" two-pointers/
mv "238. Product of Array Except Self.py" arrays/
mv "36. Valid Sudoku.py" arrays/
mv "424. Longest Repeating Character Replacement.py" sliding-window/
mv "49. Group Anagrams.py" strings/
mv "567. Permutation in String.py" sliding-window/
mv "76. Minimum Window Substring.py" sliding-window/

# Add README.md to each folder
for d in arrays two-pointers sliding-window strings; do
    touch "$d/README.md"
done