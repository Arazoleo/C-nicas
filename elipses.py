import matplotlib.pyplot as plt
import numpy as np

def Elipse_Composer(a, b, center=(0, 0), angle=0, resolution=1000):
    
    
    
    
    t = np.linspace(0, 2*np.pi, resolution)
    x = center[0] + a * np.cos(t) * np.cos(angle) - b * np.sin(t) * np.sin(angle)
    y = center[1] + a * np.cos(t) * np.sin(angle) + b * np.sin(t) * np.cos(angle)

    plt.figure(figsize=(10, 8))

    plt.plot(x, y, label='Elipse')

   
    vertices_horizontal = [(center[0] + a * np.cos(angle), center[1] + a * np.sin(angle)),
                           (center[0] - a * np.cos(angle), center[1] - a * np.sin(angle))]
    plt.plot([vertices_horizontal[0][0], vertices_horizontal[1][0]], [vertices_horizontal[0][1], vertices_horizontal[1][1]], 'ro', label='Vértices Horizontais')

    vertices_vertical = [(center[0] - b * np.sin(angle), center[1] + b * np.cos(angle)),
                         (center[0] + b * np.sin(angle), center[1] - b * np.cos(angle))]
    plt.plot([vertices_vertical[0][0], vertices_vertical[1][0]], [vertices_vertical[0][1], vertices_vertical[1][1]], 'bo', label='Vértices Verticais')

    c = np.sqrt(abs(a**2 - b**2))
    if a < b:
        foco1 = (center[0], center[1] + c)
        foco2 = (center[0], center[1] - c)
        plt.plot(foco1[0], foco1[1], 'go', label='Foco 1 (Vertical)')
        plt.plot(foco2[0], foco2[1], 'yo', label='Foco 2 (Vertical)')
        plt.title('Elipse com Focos na Vertical')
    else:
        foco1 = (center[0] + c, center[1])
        foco2 = (center[0] - c, center[1])
        plt.plot(foco1[0], foco1[1], 'go', label='Foco 1 (Horizontal)')
        plt.plot(foco2[0], foco2[1], 'yo', label='Foco 2 (Horizontal)')
        plt.title('Elipse com Focos na Horizontal')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()

def main():

    a = float(input('Insira o valor de a: '))
    b = float(input('Insira o valor de b: '))
    x = float(input('Insira a coordenada x do centro: '))
    y = float(input('Insira a coordenada y do centro: '))

    center = (x, y)
    Elipse_Composer(a, b, center = center)


if __name__ == '__main__':
    main()