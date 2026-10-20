#!/usr/bin/env python3
"""Exact quadratic illustration, not a theta certificate.

Prepared for Edward Baker with substantial LLM assistance.
20 October 2026; gpt-6-astra (Codex), recorded effort ultra.
Requires numpy and matplotlib. Output defaults beside the script; use
--output-dir to select another folder. No source data are acquired.
"""

from pathlib import Path
import argparse
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def arrow(ax, xs, ys, index, color):
    ax.annotate(
        "",
        xy=(xs[index + 5], ys[index + 5]),
        xytext=(xs[index - 5], ys[index - 5]),
        arrowprops=dict(arrowstyle="-|>", color=color, lw=2, mutation_scale=14),
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).parent)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    eta, radius = 0.16, 1.0
    lower_y = np.sqrt(2 * eta)
    upper_y = np.sqrt(2 * radius)
    cap_y = np.linspace(-upper_y, upper_y, 401)
    cap_t = np.full_like(cap_y, radius)
    right_t = np.linspace(radius, eta, 401)
    right_y = np.sqrt(2 * right_t)
    connector_y = np.linspace(lower_y, -lower_y, 401)
    connector_t = connector_y**2 - eta
    left_t = np.linspace(eta, radius, 401)
    left_y = -np.sqrt(2 * left_t)
    blue, purple, orange, red = "#226B93", "#7554A3", "#B86522", "#A33D3D"
    segments = [
        (cap_y, cap_t, purple),
        (right_y, right_t, blue),
        (connector_y, connector_t, orange),
        (left_y, left_t, blue),
    ]

    plt.rcParams.update(
        {"font.family": "DejaVu Sans", "font.size": 11, "axes.spines.top": False,
         "axes.spines.right": False, "svg.fonttype": "none"}
    )
    fig, (ax, jet) = plt.subplots(1, 2, figsize=(12, 6.4))
    fig.subplots_adjust(left=0.07, right=0.96, bottom=0.22, top=0.82, wspace=0.36)
    fig.suptitle("A heat flow contour can isolate exactly one collision", fontsize=17, y=0.96)
    fig.text(0.5, 0.90, r"Exact quadratic control:  $H(\tau,y)=y^2-2\tau$,  $J=H+iH_y$",
             ha="center", fontsize=12)

    ax.add_patch(Rectangle((-2, -0.36), 4, 1.36, facecolor="#F2EFE8",
                           edgecolor="#B7B2A8", lw=1, zorder=0))
    boundary_y = np.concatenate([part[0] for part in segments])
    boundary_t = np.concatenate([part[1] for part in segments])
    ax.fill(boundary_y, boundary_t, color="#E4EFF5", zorder=1)
    tiny_t = np.linspace(0, eta, 100)
    for sign in (-1, 1):
        ax.plot(sign * np.sqrt(2 * tiny_t), tiny_t, "--", color="#9EB4C2", lw=1.4)
    for ys, ts, color in segments:
        ax.plot(ys, ts, color=color, lw=2.5)
        arrow(ax, ys, ts, 200, color)
        real, imag = ys**2 - 2 * ts, 2 * ys
        jet.plot(real, imag, color=color, lw=2.5)
        arrow(jet, real, imag, 200, color)

    ax.scatter([0], [0], color=red, s=45, zorder=5)
    ax.annotate("collision", xy=(0, 0), xytext=(0.60, -0.06), color=red,
                arrowprops=dict(arrowstyle="-", color=red), fontsize=10)
    ax.text(0, 0.58, r"inner region: $W=-1$", ha="center", fontsize=12)
    ax.text(-1.58, 0.46, "remainder\nhas no event", ha="center", color="#756F62",
            fontsize=10)
    ax.text(0, 1.05, r"later cap: phase $-\pi$", ha="center", color=purple)
    ax.text(0, -0.30, r"rounded lower connector: phase $-\pi$",
            ha="center", color=orange, fontsize=10)
    ax.set(xlim=(-2.15, 2.15), ylim=(-0.40, 1.20),
           xlabel=r"$y=x-a$", ylabel=r"$\tau=t-T$")
    ax.set_title("Spacetime contour", fontsize=13, pad=12)
    ax.axhline(0, color="#C7CDD1", lw=0.8, zorder=0)

    jet.axhline(0, color="#C7CDD1", lw=0.8, zorder=0)
    jet.axvline(0, color="#C7CDD1", lw=0.8, zorder=0)
    jet.scatter([0], [0], color=red, s=45, zorder=5)
    jet.text(-1.65, 2.10, r"cap: $-\pi$", color=purple)
    jet.text(0.20, 2.10, r"zero path: $0$", color=blue, fontsize=10)
    jet.text(0.20, -2.10, r"zero path: $0$", color=blue, fontsize=10)
    jet.annotate(r"connector: $-\pi$", xy=(0.30, -0.30), xytext=(0.65, -0.60),
                 color=orange, fontsize=10,
                 arrowprops=dict(arrowstyle="-", color=orange))
    jet.text(-1.25, -0.15, r"one clockwise turn", ha="center", fontsize=11)
    jet.set(xlim=(-2.3, 1.55), ylim=(-3.25, 3.25),
            xlabel=r"$H$", ylabel=r"$H_y$")
    jet.set_title("Image of the same contour in the jet plane", fontsize=13, pad=12)
    fig.text(0.5, 0.055,
             "Increasing t runs upward and splits the real pair; ordinary heat runs downward.\n"
             "The tip must be rounded: passing through the collision makes physical winding undefined.",
             ha="center", fontsize=10, color="#4F5960", linespacing=1.6)
    for extension in ("png", "svg"):
        output = args.output_dir / f"HEAT_FLOW_LENS_20261020.{extension}"
        fig.savefig(output, dpi=170, facecolor="white")
        print(output)
    plt.close(fig)


if __name__ == "__main__":
    main()
