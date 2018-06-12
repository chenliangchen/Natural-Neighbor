import random as rnd

dim = 2     # Dimensão inicial
nDM = 2     # Numero de atributos a serem gerados
nDS = 200   # Numero de datasets a serem gerados 
nEX = 1000  # Numero de instancias por dataset

print("Generating 200 exponential datasets with 1000 instances each one:")
for n in range(nDS):
    n += 1
    with open("tests/exp2/datasets/EDD/" + str(n) + ".csv", "a") as fl:
        h = []
        for d in range(dim):
            d += 1
            h.append("attr" + str(d))
        fl.write(str(h)[1:-1].replace("\'", "") + "\n")
        for _ in range(nEX):
            ls = []
            for _ in range(dim):
                ls.append(round(rnd.random()*rnd.random(), 4))
            fl.write(str(ls)[1:-1] + "\n")
        fl.close()
    if(dim % nDM == 0):
        dim = 1
    dim += 1
    if(n % 10 == 0):
        print(str(n) + " exponential datasets were generated")