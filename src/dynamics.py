import numpy as np

def lyapunov_spectrum(jacobian, steps=100):
    """Черновая оценка спектра Ляпунова по заданному якобиану."""
    vals = np.linalg.eigvals(jacobian)
    return np.real(vals) / steps

def hausdorff_dim(d0, alpha, K):
    """Формула dim_H(A) = sum_{l=0}^K d_l alpha^l при d_l = d0."""
    l = np.arange(K + 1)
    return np.sum(d0 * (alpha ** l))
