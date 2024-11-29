from mpmath import quad as mpmath_quad, cos, sin, mpf
import numpy as np
import matplotlib.pyplot as plt

n = 7
N = 100*n

f = lambda t: (t**(2 * n)).real

def F(wk):
    wk = mpf(wk)
    N_mpf = mpf(N)

    def real_integrand(t):
        t = mpf(t)
        return f(t) * cos(-wk * mpf(np.pi) * t)

    def imag_integrand(t):
        t = mpf(t)
        return f(t) * sin(-wk * mpf(np.pi) * t)

    real = mpmath_quad(real_integrand, [-N_mpf, N_mpf])
    imag = mpmath_quad(imag_integrand, [-N_mpf, N_mpf])

    return real, imag

specter = lambda real, imag: np.sqrt(real**2 + imag**2)

def main():
    T_values = [4, 8, 16, 32, 64, 128]
    k_values = np.arange(0, 21, 1)

    fig, axes = plt.subplots(3, 2, figsize=(14, 10))

    for i, T in enumerate(T_values):
        Re_values = []

        for k in k_values:
            wk = 2 * np.pi * k / T
            real, imag = F(wk)
            Re_values.append(real)

        row, col = divmod(i, 2)

        axes[row, col].stem(k_values, Re_values, basefmt=" ",
                            label=f"Re(F(w_k)), T = {T}")
        axes[row, col].set_xlabel("k")
        axes[row, col].set_ylabel("Re(F(w_k))")
        axes[row, col].grid(True)
        axes[row, col].legend()

    plt.show()

    fig, axes = plt.subplots(3, 2, figsize=(14, 10))

    for i, T in enumerate(T_values):
        Re_values = []
        Amplitude_values = []

        for k in k_values:
            wk = 2 * np.pi * k / T
            real, imag = F(wk)
            Re_values.append(real)
            Amplitude_values.append(specter(real, imag))

        row, col = divmod(i, 2)

        axes[row, col].stem(k_values, Amplitude_values, basefmt=" ", linefmt='orange',
                            markerfmt='o', label=f"|F(w_k)|, T = {T}")
        axes[row, col].set_xlabel("k")
        axes[row, col].set_ylabel("|F(w_k)|")
        axes[row, col].grid(True)
        axes[row, col].legend()

    plt.show()

    

    plt.figure(figsize=(10, 6))
    for T in T_values:
        Re_values = [F(2 * np.pi * k / T)[0] for k in k_values]
        plt.plot(k_values, Re_values, marker='o',
                 linestyle='-', label=f"T = {T}")
    plt.xlabel("k")
    plt.ylabel("Re(F(w_k))")
    plt.title("Real part of F(w_k) for different T values")
    plt.grid(True)
    plt.legend()
    plt.show()

    plt.figure(figsize=(10, 6))
    for T in T_values:
        Amplitude_values = [specter(*F(2 * np.pi * k / T)) for k in k_values]
        plt.plot(k_values, Amplitude_values, marker='o',
                 linestyle='-', label=f"T = {T}")
    plt.xlabel("k")
    plt.ylabel("|F(w_k)|")
    plt.title("Amplitude |F(w_k)| for different T values")
    plt.grid(True)
    plt.legend()
    plt.show()

    t = np.linspace(-2, 2, 500)
    n = 7  
    y = t ** (2 * n)

    plt.figure(figsize=(8, 6))
    plt.plot(t, y, label=f"$t^{{2n}}, n={n}$", color='blue')
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    plt.title(f"Plot of $t^{{2n}}$ for n = {n}", fontsize=16)
    plt.xlabel("$t$", fontsize=14)
    plt.ylabel("$t^{2n}$", fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(alpha=0.3)
    plt.show()




if __name__ == "__main__":
    main()