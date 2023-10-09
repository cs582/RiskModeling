import matplotlib.pyplot as plt
from src.super_gaussian import SuperGaussianDistribution1D

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    x_pows = [1, 2, 3]
    x_stds = [1, 2, 3]
    coefs = [1]

    n_plots = len(x_pows) * len(x_stds) * len(coefs)

    n_cols = 3
    n_rows = (n_plots // n_cols) + 1

    figsize = (n_rows*7, n_cols*7)
    fig, ax = plt.subplots(n_rows, n_cols, figsize=figsize)
    print(ax.shape)
    print(figsize)

    idx = 0
    for x_pow in x_pows:
        for x_std in x_stds:
            for coef in coefs:
                model = SuperGaussianDistribution1D(xlims=(-2, 2), x_pow=x_pow, x_std=x_std, coef=coef)
                print([idx % n_rows, idx // n_rows], idx)
                model.plot_gaussian(ax=ax[idx % n_rows][idx // n_rows])
                idx += 1

    plt.savefig("tmp/figures/test.png")
