import numpy as np
import matplotlib.pyplot as plt

def Construct_Hiperbole(a, b, x0, y0):
    c = np.sqrt(a**2 + b**2)
    
    if a > b:  # Hipérbole Horizontal
        x = np.linspace(x0 - 10 * a, x0 + 10 * a, 400)
        y_positive = []
        y_negative = []
        
        for x_val in x:
            if (x_val - x0)**2 / a**2 - 1 >= 0:
                y_val = b * np.sqrt((x_val - x0)**2 / a**2 - 1)
                y_positive.append(y_val + y0)
                y_negative.append(-y_val + y0)
            else:
                y_positive.append(np.nan)
                y_negative.append(np.nan)
        
        y_positive = np.array(y_positive)
        y_negative = np.array(y_negative)
        
        asymptote_y1 = y0 + (b / a) * (x - x0)
        asymptote_y2 = y0 - (b / a) * (x - x0)
        
        plt.plot(x, y_positive, 'b', label='Hipérbole')
        plt.plot(x, y_negative, 'b')
        plt.plot(x, asymptote_y1, 'r--', label='Assíntota')
        plt.plot(x, asymptote_y2, 'r--')
        plt.plot([x0 + a, x0 - a], [y0, y0], 'go', label='Vértices')
        plt.plot([x0 + c, x0 - c], [y0, y0], 'ro', label='Focos')
        
    else:  # Hipérbole Vertical
        y = np.linspace(y0 - 10 * b, y0 + 10 * b, 400)
        x_positive = []
        x_negative = []
        
        for y_val in y:
            if (y_val - y0)**2 / b**2 - 1 >= 0:
                x_val = a * np.sqrt((y_val - y0)**2 / b**2 - 1)
                x_positive.append(x_val + x0)
                x_negative.append(-x_val + x0)
            else:
                x_positive.append(np.nan)
                x_negative.append(np.nan)
        
        x_positive = np.array(x_positive)
        x_negative = np.array(x_negative)
        
        asymptote_x1 = x0 + (a / b) * (y - y0)
        asymptote_x2 = x0 - (a / b) * (y - y0)

        plt.plot(x_positive, y, 'b', label='Hipérbole')
        plt.plot(x_negative, y, 'b')
        plt.plot(asymptote_x1, y, 'r--', label='Assíntota')
        plt.plot(asymptote_x2, y, 'r--')
        plt.plot([x0, x0], [y0 + b, y0 - b], 'go', label='Vértices')
        plt.plot([x0, x0], [y0 + c, y0 - c], 'ro', label='Focos')
        
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlim(x0 - 10, x0 + 10)
    plt.ylim(y0 - 10, y0 + 10)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico da Hipérbole com Elementos Adicionais')
    plt.legend()
    plt.show()

def main():
    a = float(input('Valor de a: '))
    b = float(input('Valor de b: '))
    x0 = float(input('Coordenada x do centro: '))
    y0 = float(input('Coordenada y do centro: '))

    Construct_Hiperbole(a, b, x0, y0)

if __name__ == '__main__':
    main()
