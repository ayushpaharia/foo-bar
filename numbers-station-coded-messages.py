def answer(l, t):
    # your code here
    l_len = len(l)
    if l[0] == t:
        return [0, 0]
    if l_len == 1:
        return [-1, -1]
    head_i = 0
    tail_i = 1
    head = l[head_i]
    tail = l[tail_i]
    num_sum = head + tail
    while True:
        if num_sum == t:
            return [head_i, tail_i]
        if num_sum < t:
            tail_i += 1
            if tail_i > l_len-1:
                return [-1, -1]
            tail = l[tail_i]
            num_sum += tail
        else:
            num_sum -= head
            head_i += 1
            head = l[head_i]
