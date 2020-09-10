import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import random

m = 1  # numar perioade
n = 100  # numar unde
# cosarg = []
# sinarg = []
an = []
bn = []
listaunde = []


def dreptunghi(f, T, N):  # f - frecventa, N - nr samples, T - baza timp
    t = np.linspace(0, T, N)
    g = signal.square(2 * np.pi * f * t)  # semnal patrat
    P = 1 / f  # perioada
    dt = P / N  # incementul dt
    fdreptunghi = [g, f, dt, N, t]  # t - timp discret, g - valoare la timpul t, P- perioada, dt-increment valori
    return fdreptunghi

# TODO
# import de fisier audio in piton si transpunerea lui in forma unei matrici
# FERESTRUIRE NEBUNIE WINDOWING


def coef(s, f, dt, N):  # s-semnal, f - frecventa, dt-increment valori, N-numar samples
    for w in range(0, n):
        cosarg = []
        sinarg = []
        unda = []
        for y in range(0, N * m):
            cos = np.cos(2 * np.pi * f * w * dt * y)
            sin = np.sin(2 * np.pi * f * w * dt * y)
            cosarg.append(cos)
            sinarg.append(sin)

        a = (np.sum([i * j for i, j in zip(s, cosarg)])) / N
        b = (np.sum([i * j for i, j in zip(s, sinarg)])) / N

        if w == 0:
            ...
        else:
            a = a * 2
            b = b * 2

        an.append(a)
        bn.append(b)

        for argument in range(0, N * m):
            element = a * cosarg[argument] + b * sinarg[argument]
            unda.append(element)

        listaunde.append(unda)

    list_sum = np.zeros(len(listaunde[1]))
    for i in listaunde:
        list_sum += i
    list_sum = list_sum.tolist()
    print("listsum = ", list_sum)
    print(an)
    print(bn)
    return listaunde, list_sum


def graficeStatice(g, t, listaunde, list_sum, n):

    lista_culori = ["black", "dimgray", "gray", "silver", "lightcoral", "indianred", "brown", "firebrick",
                    "darkred", "red", "salmon", "tomato", "peru", "darkorange", "tan", "wheat", "goldenrod",
                    "darkgoldenrod", "gold", "yellow", "yellowgreen", "greenyellow", "lawngreen", "palegreen",
                    "forestgreen", "limegreen", "darkgreen", "green", "lime", "olive", "orange", "seagreen",
                    "mediumspringgreen", "aquamarine", "turquoise", "lightseagreen", "teal", "darkcyan", "cyan",
                    "darkturquoise", "powderblue", "deepskyblue", "skyblue", "lightskyblue", "steelblue",
                    "dodgerblue", "lightsteelblue", "royalblue", "midnightblue", "blue", "slateblue", "indigo",
                    "darkslateblue", "mediumslateblue", "blueviolet", "darkviolet", "plum", "violet", "fuchsia",
                    "magenta", "purple", "deeppink", "hotpink", "palevioletred", "crimson", "pink", "orchid"]

    f = signal.resample(g, 100000)
    xnew = np.linspace(0, 1, 100000, endpoint=False)

    # vector = []
    #
    # for i in range(len(f)):
    #     vector.append(f[i])

    plt.figure()
    plt.title("Semnal original")
    plt.plot(t, g, "g-", label="original")
    plt.axis("tight")
    plt.legend()

    # plt.figure(2)
    # plt.title("Semnal resampled")
    # plt.plot(t, g, "g-", xnew, f, ".-")
    # plt.legend(["data", "resampled"], loc="best")

    plt.figure()
    plt.title("Primele 5 unde")
    plt.plot(listaunde[0], 'lime')
    plt.plot(listaunde[1], 'cyan')
    plt.plot(listaunde[2], 'red')
    plt.plot(listaunde[3], 'violet')
    plt.plot(listaunde[4], 'black')

    # plt.figure()
    # for i in range(n):
    #     plt.subplot()
    #     plt.plot(listaunde[i], color = random.choice(lista_culori))
    # plt.plot(list_sum)

    # plt.figure()
    # plt.subplot(611)
    # plt.plot(listaunde[0])
    # plt.subplot(612)
    # plt.plot(listaunde[1])
    # plt.subplot(613)
    # plt.plot(listaunde[2])
    # plt.subplot(614)
    # plt.plot(listaunde[3])
    # plt.subplot(615)
    # plt.plot(listaunde[4])
    # plt.subplot(616)
    # plt.plot(list_sum)

    plt.figure()
    plt.subplot(611, title="Componentele armonice")
    for i in range(n):
        plt.plot(listaunde[i], color = random.choice(lista_culori))
    plt.subplot(613, title="Semnal si suma a compoentelor armonice")
    plt.plot(list_sum, "darkviolet",  g, "green")
    plt.subplot(615, title="Unda aleasa")
    plt.plot(listaunde[1], "green")

    # plt.legend(["original", "fourier"], loc="best")

    # plot seria fourier de i si timp
    plt.show()


fdreptunghi = dreptunghi(100, 100, 1000)

coefi = coef(fdreptunghi[0], fdreptunghi[1], fdreptunghi[2],
             fdreptunghi[3])  # rulati functia coef cu parametrii ei si obtineti cele doua siruri, an/bn

graficeStatice(fdreptunghi[0], fdreptunghi[4], coefi[0], coefi[1], n)
