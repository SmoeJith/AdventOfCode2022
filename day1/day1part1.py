# Nicely Formatted
print(
    sorted([
            sum(
                [int(snack) for snack in elf.split()]
            ) for elf in open('input.txt', 'r').read().split('\n\n')
    ])[-1]
)

# One Liner
print(sorted([sum([int(snack) for snack in elf.split()]) for elf in open('input.txt', 'r').read().split('\n\n')])[-1])