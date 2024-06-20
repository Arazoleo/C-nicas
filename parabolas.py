import numpy as np
import matplotlib.pyplot as plt

def Parabola_Horizontal(a, h, k):

    y = np.linspace(k - 10, k + 10, 400)
    x = a * (y - k)**2 + h

    foco_hor = h + 1/(4 * a)
    diretriz_hor = a * (y - k)**2 + h
    
   
    plt.plot(x, y, label=f'$x = {a}(y - {k})^2 + {h}$')
    
    
   
    plt.scatter(h, k, color='red', zorder=5)
    plt.text(h, k, f'Vértice ({h}, {k})', fontsize=12, verticalalignment='bottom')
    
    plt.scatter(foco_hor, k, color = 'yellow', zorder = 5)
    plt.text(foco_hor, k, f'Foco({foco_hor:.2f}, {k})', fontsize = 12, verticalalignment = 'top')

    plt.axvline(diretriz_hor, color = 'green', linestyle = '--', linewidth = 1, label = f'Diretriz $x = {diretriz_hor:.2f}$')


    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.title('Gráfico da parábola horizontal (canônica)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.xlim(min(x) - 10, max(x) + 10)
    plt.ylim(k - 10, k + 10)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def Parabola_Vertical(a, h, k):
    x = np.linspace(h - 10, h + 10, 400)
    y = a * (x - h) ** 2 + k

    foco_ver = k + 1/(4 * a)
    diretriz_ver = k - 1/(4 * a)

    plt.plot(x, y, label = f'$y = {a}(x - {h})^2 + {k}$')

    plt.scatter(h, k, color = "blue", zorder = 5)
    plt.text(h, k, f'Vértice ({h}, {k})', fontsize = 13, verticalalignment = 'bottom')

    plt.scatter(h, foco_ver, color = 'yellow', zorder = 5)
    plt.text(h, foco_ver, f'Foco({h}, {foco_ver:.2f})', fontsize = 12, verticalalignment = 'top')

    plt.axhline(diretriz_ver, color = 'green', linestyle = '--', linewidth = 1, label = f'Diretriz $y = {diretriz_ver:.2f}$')
    


    plt.axhline(0, color = 'black', linewidth = 0.5)
    plt.axvline(0, color = 'black', linewidth = 0.5)
    plt.grid(color = "gray", linestyle = '--', linewidth = 0.5)
    plt.title('Gráfico da parábola vertical (canônica)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.ylim(min(y) - 10, max(y) + 10)
    plt.xlim(h - 10, h + 10)
    plt.gca().set_aspect('equal', adjustable = 'box')
    plt.show()



def main():
    a = float(input("Valor de a: "))
    h = float(input("Valor de h: "))
    k = float(input("Valor de k: "))

    op = int(input("1 - Parábola vertical (x²)\n2 - Parábola horizontal (y²)\n\nInsira o tipo de parábola: "))

    if op == 1:
      Parabola_Vertical(a, h, k)  
    elif op == 2:
      Parabola_Horizontal(a, h, k)
    else:
       print("Opção inválida. Tente novamente!")




if __name__ == "__main__":
    main();
