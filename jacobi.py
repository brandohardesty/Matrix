xk = [0,0,0]

iterations = 100
for i in range(iterations):
    xk1 = [0,0,0]
    xk1[0] = (1/3)*(5-2*xk[1])
    xk1[1]=(-1/5)*(18+xk[0]+2*xk[2])
    xk1[2]=(1/8)*(-7+2*xk[0]-xk[1])

    Ax = [0,0,0]

    Ax[0] = 3*xk1[0]+2*xk1[1]
    Ax[1] = -xk1[0]-5*xk1[1]-2*xk1[2]
    Ax[2] = -2*xk1[0] + xk1[1]+8*xk1[2]

    rE = [0,0,0]
    rE_norm = 0

    rE[0] = 5-Ax[0]
    rE[1] = 18 -Ax[1]
    rE[2] = -7-Ax[2]

    for j in range(3):
        xk[j] = xk1[j]
        rE_norm = max(rE_norm,abs(rE[j]))
    print(i,xk1,rE_norm)