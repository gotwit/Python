# Longest substring without repeating characters

# O(n) Time | O(1) Space
def longestSubstring(string, outStringLen=False):
    start_idx, running_start_idx = 0, 0
    end_idx, running_end_idx = 0, 0
    len_sub = 0
    d = {}

    for k, v in enumerate(string):
        # print(k, v)
        end_idx = k

        if v in d:
            start_idx = max(start_idx, d[v])
        else:
            running_start_idx = start_idx
            running_end_idx = end_idx
            print(f"start_idx: {running_start_idx}, end_idx: {running_end_idx}\n")

        len_sub = max(len_sub, (end_idx - start_idx))
        d[v] = k

    # keys_list = list(d.keys())
    # values_list = sorted(list(d.values()))


    # print(f"keys_list: {keys_list}\n")
    # print(f"values_list: {values_list}\n")
    # keys_list[values_list.index(i)]

    # return len_sub if outStringLen else [string[i] for i in range(running_start_idx+1, running_end_idx + 1)]
    # running_start_idx = running_start_idx+1 if running_start_idx > 0 else running_start_idx
    return len_sub if outStringLen else [string[i] for i in range(running_start_idx, running_end_idx + 1)]

# Sample input: "abcbbcbad"
# string = #"pwwkew" #"bbbbb" #"abcabcbb" #

n = int(input("Enter test runs: "))

for i in range(0, 4):
    string = str(input("Please enter text: "))
    result = longestSubstring(string)
    print(f"Solution #1 - Longest substring: {result}")

