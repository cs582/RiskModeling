import matplotlib.pyplot as plt
from src.super_gaussian import SuperGaussianDistribution1D

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    x_pows = [1, 2, 3]
    coefs = [1, 2, 3]

    n_plots = len(x_pows) * len(coefs)

    n_cols = 3
    n_rows = (n_plots // n_cols)

    figsize = (n_rows*7, n_cols*7)
    fig, ax = plt.subplots(n_rows, n_cols, figsize=figsize)
    print(ax.shape)
    print(figsize)

    idx = 0
    for x_pow in x_pows:
        for coef in coefs:
            model = SuperGaussianDistribution1D(xlims=(-2, 2), x_pow=x_pow, coef=coef)
            print([idx % n_rows, idx // n_rows], idx)
            model.plot_gaussian(ax=ax[idx % n_rows][idx // n_rows])
            idx += 1

    plt.savefig("tmp/figures/sg_1d_test.png")
