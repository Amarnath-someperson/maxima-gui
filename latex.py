import matplotlib.pyplot as plt

plt.rcParams['figure.facecolor'] = 'salmon'
plt.rcParams['text.color'] = 'black'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'


def plt_result(text, tex: bool):
    fig = plt.figure()
    fig.text(0.1, 0.5, rf"${text.strip()}$", fontsize=50, usetex=tex)
    plt.axis('off')
    plt.draw()
    plt.savefig('input.png', bbox_inches='tight')


def cleaned(x):
    x = x.replace('(', '{').replace(')', '}')
    return x  # TODO: parser.


def default_tex():
    fig = plt.figure()
    fig.text(0.1, 0.5, r"$\text{hello!!}$", fontsize=50)
    plt.axis('off')
    plt.draw()
    plt.savefig('input.png', bbox_inches='tight')


if __name__ == "__main__":
    plt_tex(r"\text{testing with latex} \int xdx=\frac{x^2}{2}")
