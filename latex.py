import matplotlib.pyplot as plt


def plt_tex(text):
    text = cleaned(text)
    fig = plt.figure()
    fig.text(0.1, 0.5, rf"${text.strip()}$", fontsize=50)
    plt.axis('off')
    plt.draw()
    plt.savefig('input.png', bbox_inches='tight')


def cleaned(x):
    x = x.replace('(', '{').replace(')', '}')
    return x
    pass  # in developments


def default_tex():
    fig = plt.figure()
    fig.text(0.1, 0.5, r"$\text{hello!!}$", fontsize=50)
    plt.axis('off')
    plt.draw()
    plt.savefig('input.png', bbox_inches='tight')


if __name__ == "__main__":
    plt_tex(r"\text{testing with latex} \int xdx=\frac{x^2}{2}")
