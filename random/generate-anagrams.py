def generate_permutations(s: str) -> list:
    for x in s:
        for y in s:
            for z in s:
                if x != y and y != z and x != z:
                    print(x + y + z)


generate_permutations("abc")