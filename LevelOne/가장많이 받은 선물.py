def solution(friends, gifts):
    from collections import defaultdict

    # Initialize dictionaries to track gifts given and received
    give_count = defaultdict(lambda: defaultdict(int))
    received_count = {friend: 0 for friend in friends}
    gift_index = {friend: 0 for friend in friends}

    # Record the number of gifts given between friends
    for gift in gifts:
        giver, receiver = gift.split()
        give_count[giver][receiver] += 1

    # Calculate the gift index for each friend
    for giver in give_count:
        for receiver in give_count[giver]:
            gift_index[giver] += give_count[giver][receiver]
            gift_index[receiver] -= give_count[giver][receiver]

    # Determine who will receive gifts next month
    for giver in friends:
        for receiver in friends:
            if giver != receiver:
                if give_count[giver][receiver] > give_count[receiver][giver]:
                    received_count[receiver] += 1
                elif give_count[giver][receiver] < give_count[receiver][giver]:
                    received_count[giver] += 1
                elif give_count[giver][receiver] == give_count[receiver][giver]:
                    if gift_index[giver] > gift_index[receiver]:
                        received_count[receiver] += 1
                    elif gift_index[giver] < gift_index[receiver]:
                        received_count[giver] += 1

    # Find the maximum number of gifts received by any friend
    return max(received_count.values())

# Test cases
friends1 = ["muzi", "ryan", "frodo", "neo"]
gifts1 = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
print(solution(friends1, gifts1))  # Expected output: 2

friends2 = ["joy", "brad", "alessandro", "conan", "david"]
gifts2 = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
print(solution(friends2, gifts2))  # Expected output: 4

friends3 = ["a", "b", "c"]
gifts3 = ["a b", "b a", "c a", "a c", "a c", "c a"]
print(solution(friends3, gifts3))  # Expected output: 0
