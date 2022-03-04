
import matplotlib.pyplot as plt
import pt1

if __name__ == "__main__":
    pt1.init()
    pt1.cvar.u = 1.0
    t_i = range(1000)
    y_i = []
    for t in t_i:
        pt1.step()
        y_i.append(pt1.cvar.y)
    plt.plot(t_i, y_i, '*')
    plt.show()
