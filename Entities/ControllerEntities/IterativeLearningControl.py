""" a simple example of ILC
    from Moore, Iterative learning control: a tutorial and big picture 2006 6p
"""
# https://en.wikipedia.org/wiki/Iterative_learning_control
# https://en.wikipedia.org/wiki/LTI_system_theory


from __future__ import division
import sys
import numpy as np


__version__ = "2015-02-17 feb  denis-bz-py t-online de"

# ...............................................................................
rates = [1.15, 1.5]  # aka gamma, eta, learning rate, stepsize
n = 50
errtol = 1e-3  # av |target - y|
plot = 0
save = 0
seed = 0

A = np.array([[-.8, -.1], [1, 0]])  # from Moore
B = np.array([.5, 1])  # grr lti [:,np.newaxis]
C = np.array([1, .5])
D = np.zeros(1)
niter = 20

# to change these params in sh or ipython, run this.py  a=1  b=None  c=[3] ...
for arg in sys.argv[1:]:
    exec(arg)

np.set_printoptions(threshold=10, edgeitems=3, linewidth=150,
                    formatter=dict(float=lambda x: "%.2g" % x))  # float arrays %.2g
np.random.seed(seed)
thispy = __file__.split("/")[-1]
plot = True
if plot:
    from matplotlib import pyplot as pl
    # import seaborn

    fig, axes = pl.subplots(nrows=len(rates))
    fig.suptitle("A simple example of ILC, iterative learning control  from Moore et al.")
    for rate, ax in zip(rates, axes):
        ax.set_ylabel("rate %.3g" % rate)
else:
    axes = len(rates) * [None]

# target = np.sin(8 * np.arange(n) / n)
target = np.zeros(n)

target[10:] = 10
print(len(target))
# print "A %s \nB %s \nC %s \nD %s" % (A, B[:,np.newaxis], C, D)
# ltisys = ssig.ltisys.lti( A, B[:,np.newaxis], C, D )
# scipy/signal/filter_design.py:400: BadCoefficients

# ...............................................................................
def ltistep(U, A=A, B=B, C=C):
    """ LTI( A B C ): U -> y  linear
        straight up
    """
    U, A, B, C = map(np.asarray, (U, A, B, C))
    xk = np.zeros(A.shape[1])
    x = [xk]
    for u in U[:-1]:
        xk = A.dot(xk) + B.dot(u)
        x.append(xk.copy())
    return np.dot(x, C)

for rate, ax in zip(rates, axes):
    print(    "\nrate %g --" % rate  )# todo: optimize rate_k curve
    U = np.zeros(n)
    errs = []
    Us = []
    for iter in range(niter):
        y = ltistep(U)
        err = target - y  # oscillates:
        U[:-1] += rate * err[1:]  # why is the shift so effective ?

        abserr = np.fabs(err)
        av, maxerr = abserr.mean(), abserr.max()
        deltaU = np.fabs(U - Us[-1]).mean() if len(Us) > 0 \
            else np.NaN

        print("err: %2d: av %-8.2g  max %-8.2g  dU %-8.2g  %s " % (
            iter, av, maxerr, deltaU, err)
        )
        errs.append(err.copy())
        Us.append(U.copy())
        if plot and iter >= 5:
            ax.plot(errs)
            # yrug( ax, maxerr )
        if maxerr <= errtol:
            break

    errs = np.array(errs)
    Us = np.array(Us)
    # print "u - target:", Us[-1] - target
    if save:
        npz = "rate%.3g.npz" % rate
        print("saving to %s  err %s  U %s" % (npz, errs.shape, Us.shape))

        np.savez(npz, err=errs, U=Us, rate=rate)
plot = True
if plot:
    pl.show()
