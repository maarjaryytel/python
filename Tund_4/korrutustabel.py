for kordus in range(1,11):

    from random import randint
    esimeneNumber= randint (0, 10)
    teineNumber= randint (0, 10)

    print("Arvuta: ", esimeneNumber,"*", teineNumber)
    vastus=int(input("Kirjuta oma vastus: "))

    if vastus == esimeneNumber * teineNumber:
        print("Õige vastus!")
        
    else:
        print("Vale vastus!")

    