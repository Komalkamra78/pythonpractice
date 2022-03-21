for i in range(2,4):
    with open (f"multiplication table of {i}" ,"w") as f:
        for j in range(1,11):
            f.write(f"{i} x {j} = {i*j}")
            if j!=10:
             f.write("\n")