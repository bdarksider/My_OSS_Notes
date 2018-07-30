# Paste your code into this box
s = 'txlspgxemn'

longest_substring = ''
backup = ''
for i in range(len(s) - 1):
    if ord(s[i]) <= ord(s[i+1]):
        longest_substring += s[i]
    else:
        longest_substring += s[i]
        if len(backup) < len(longest_substring):
            backup = longest_substring
        longest_substring = ''

    if i == len(s) - 2 and s[i+1] > s[i]:
        longest_substring += s[i+1]


if len(longest_substring) == len(backup):
    print(backup)
elif len(longest_substring) > len(backup):
    print('Longest substring in alphabetical order is: ' + longest_substring)
else:
    print('Longest substring in alphabetical order is: ' + backup)