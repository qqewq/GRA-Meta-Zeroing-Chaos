import matplotlib.pyplot as plt
import numpy as np

def plot_trajectory(trajectory, filename="attractor_3d.png"):
    """Простейшая 3D-визуализация траектории."""
    from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

    traj = np.array(trajectory)
    if traj.shape[-1] < 3:
        raise ValueError("Нужно минимум 3 координаты для 3D-плота.")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(traj[:, 0, 0], traj[:, 0, 1], traj[:, 0, 2], lw=0.5)
    ax.set_title("Траектория мультиверсной динамики (заглушка)")
    plt.tight_layout()
    plt.savefig(filename, dpi=200)
    plt.close(fig)
