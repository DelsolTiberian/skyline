def calcul_skyline(T):
    if T > 1:
        T1 = [T[i] for i in range(len(T)//2)]
        T2 = [T[i] for i in range(len(T)//2, len(T))]

        T1 = calcul_skyline(T1)
        T2 = calcul_skyline(T2)

        return fusion_skyline(T1, T2)
    else:
        return [(T[0][0], T[0][1]), (T[0][2], 0)]


def fusion_skyline(T1, T2):
    rep = []
    ind1 = 0
    ind2 = 0
    #On initialise la liste reponse
    if T1[0][0] < T2[0][0]:
        rep.append(T1[0])
        ind1 += 1
    elif T1[0][0] == T2[0][0] and T1[0][1] > T2[0][1]: 
        rep.append(T1[0])
        ind1 += 1
    else:
        rep.append(T2[0])
        ind2 += 1

    while ind1 + ind2 != len(T1) + len(T2):
        if ind1 >= len(T1):
            rep.append(T2[ind2])
            ind2 += 1
        elif ind2 >= len(T2):
            rep.append(T1[ind1])
            ind1 += 1
        # Prend celui qui commence le plus tot entre les deux prochains
        elif T1[ind1][0] <= T2[ind2][0]:
            # Si la hauteur est plus haute que le precedent ou si il commence quand le precedent se finit et qu'il est plus grand que le prochain, le met tel quel
            if T1[ind1][1] >= rep[len(rep)-1][1] or T1[ind1][0] == T2[ind2][0]:
                if T1[ind1][0] == T2[ind2][0] and T1[ind1][1] > T2[ind2][1]:
                    rep.append(T1[ind1])
            # Si il se termine avant le debut de celui d'apres et qu'il est plus grand
            elif T1[ind1][1] > T2[ind2][1] and T1[ind1+1][0] > T2[ind2][0]:
                rep.append((T2[ind2][0], T1[ind1][1]))
            ind1 += 1
        else:
            if T2[ind2][1] >= rep[len(rep)-1][1]:
                rep.append(T2[ind2])
            elif T2[ind2][1] > T1[ind1][1] and T2[ind2+1][0] > T1[ind1][0]:
                rep.append((T1[ind1][0], T2[ind2][1]))
            ind2 += 1
    return rep


print(fusion_skyline([(0, 4), (5, 7), (7, 3), (10, 0)],[(1, 6), (5, 9), (8, 0)]))