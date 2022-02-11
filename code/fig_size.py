from math import sqrt

def from_pt(width: float, fraction: float = 1, subplots: tuple[int, int] = (1, 1)) -> tuple[float, float]:
    fig_width = width * fraction

    inches_per_pt = 1 / 72.27

    golden_ratio = (sqrt(5) - 1) / 2

    fig_width_in = fig_width * inches_per_pt
    fig_height_in = fig_width_in * golden_ratio * (subplots[0] / subplots[1])

    return fig_width_in, fig_height_in
