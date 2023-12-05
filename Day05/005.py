def check_seed_range(seed_range: tuple[int, int], mappings: list[tuple[int, int, int]]) -> list[tuple[int, int]]:
    unprocessed = [seed_range]
    processed = []
    for rang in unprocessed:
        for mapping in mappings:
            seed_start = rang[0]
            seed_end = rang[0] + rang[1]
            mapping_start = mapping[1]
            mapping_end = mapping[1] + mapping[2]

            if seed_start >= mapping_start and seed_end <= mapping_end:
                processed.append((mapping[0] + rang[0] - mapping[1], rang[1]))
                break
            elif seed_start > mapping_start and seed_start <= mapping_end:
                processed.append((mapping[0] + seed_start - mapping_start, mapping_end - seed_start + 1))
                unprocessed.append((seed_start + mapping_end - seed_start + 1, rang[1] - (mapping_end- seed_start + 1)))
                break
            elif seed_end >= mapping_start and seed_end < mapping_end:
                processed.append((mapping[0], seed_end - mapping_start + 1))
                unprocessed.append((seed_start, rang[1] - (seed_end - mapping_start + 1)))
                break
            elif seed_start < mapping_start and seed_end > mapping_end:
                processed.append((mapping[0], mapping[2]))
                unprocessed.append((seed_start, mapping_start - seed_start))
                unprocessed.append((mapping[1] + 1, seed_end - mapping_end))
                break
        else:
            processed.append(rang)

    return processed


def solve_day_5(seeds_ranges, maps):
    for m in maps:
        ranges = []
        for seeds_range in seeds_ranges:
            ranges += check_seed_range(seeds_range, m)
        seeds_ranges = ranges
    return min(ranges, key=lambda x: x[0])[0] - 1


if __name__ == '__main__':
    maps = list(map(lambda x: list(map(lambda y: y.split(), x.strip().split('\n')))[1:], open('input').read().split('\n\n')))
    seeds, *maps = maps
    maps = list(map(lambda x: list(map(lambda y: list(map(int, y)), x)), maps))

    seeds_ranges = [(int(value), 1) for value in seeds[0]]
    print(f'Part 1: {solve_day_5(seeds_ranges, maps) + 1}')

    seeds_ranges = [(start, number) for start, number in zip(*[iter(list(map(int, seeds[0])))] * 2)]
    print(f'Part 2: {solve_day_5(seeds_ranges, maps)}')
