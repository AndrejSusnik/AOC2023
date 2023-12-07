from functools import cmp_to_key


def is_full_house(vals: dict[str, int]) -> bool:
    return max(vals.values()) == 3 and len(vals.values()) == 2


def listify_hand(hand: str) -> list[int]:
    return list(map(lambda x: 10 if x == 'T' else
                              1 if x == 'J' else
                              12 if x == 'Q' else
                              13 if x == 'K' else
                              14 if x == 'A' else int(x), [*hand]))


def swap_jokers(hand: dict[str, int]) -> str:
    hand_c = hand.copy()
    if len(hand_c.keys()) == 1:
        return hand_c
    if 'J' in hand_c.keys():
        hand_c[max(filter(lambda x: x[0] != 'J', hand_c.items()), key=lambda x: x[1])[0]] += hand_c['J']
        del hand_c['J']

    return hand_c


def compare(item1: list[str, str, dict[str, int]], item2: list[str, str, dict[str, int]]) -> int:
    vals1 = swap_jokers(item1[2])
    vals2 = swap_jokers(item2[2])

    if max(vals1.values()) > max(vals2.values()):
        return 1
    elif max(vals1.values()) == max(vals2.values()):
        if is_full_house(vals1) and not is_full_house(vals2):
            return 1
        elif is_full_house(vals2) and not is_full_house(vals1):
            return -1

        if len(vals1.values()) < len(vals2.values()):
            return 1
        elif len(vals1.values()) > len(vals2.values()):
            return -1

        for i, j in zip(item1[0], item2[0]):
            if i > j:
                return 1
            elif j > i:
                return -1

    return -1

if __name__ == "__main__":
    f = [(listify_hand(hand[0]), hand[1], {i: hand[0].count(i) for i in set(hand[0])}) for hand in list(map(str.split, open('input').readlines()))]
    
    for i, elm in enumerate(sorted(f, key=cmp_to_key(compare))):
        print(i, elm)
    print(sum([(i + 1) * int(elm[1]) for i, elm in enumerate(sorted(f, key=cmp_to_key(compare)))]))

