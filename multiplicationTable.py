def multiplicationTable(nb: int | None = None) -> None:
    if nb is None:
        nb = int(input("Enter a number: "))

    i=1
    while i <= 10:
        print(f"{nb} * {i} = {nb * i}")
        i +=1
