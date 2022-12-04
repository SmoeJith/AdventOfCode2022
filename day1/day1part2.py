# Nicely Formatted
print(
    sum(
        sorted([
            sum([
                int(snack) for snack in elf.split()
            ]) for elf in open('input.txt', 'r').read().split('\n\n')]
        )[-3:]
    )
)

# One Liner
print(sum(sorted([sum([int(snack) for snack in elf.split()]) for elf in open('input.txt', 'r').read().split('\n\n')])[-3:]))