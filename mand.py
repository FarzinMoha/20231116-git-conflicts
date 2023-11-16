import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z**2 + c
        n += 1
    if n == max_iter:
        return max_iter
    return n + 1 - np.log(np.log2(abs(z)))


def mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter):
    x, y = np.meshgrid(np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height))
    c = x + 1j * y
    mandelbrot_image = np.vectorize(lambda c: mandelbrot(c, max_iter))(c)
    return mandelbrot_image


def plot_fractal(fractal_image, x_min, x_max, y_min, y_max):
    plt.imshow(fractal_image, extent=(x_min, x_max, y_min, y_max), cmap='hot', interpolation='bilinear')
    plt.colorbar()
    plt.title('Mandelbrot Set')
    plt.show()

# Set the parameters for the Mandelbrot set
width, height = 800, 800
x_min, x_max = -0.8, 0.8
y_min, y_max = -0.8, 0.8
max_iter = 20

# Generate and plot the Mandelbrot set
mandelbrot_image = mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter)
plot_fractal(mandelbrot_image, x_min, x_max, y_min, y_max)
