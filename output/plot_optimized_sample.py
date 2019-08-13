import sys
import os

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))


def plot_optimized_sample(base, title='title',
                          y_min=None, y_max=None, y2_min=None, y2_max=None):
    data_sample = base.return_optimized_sample()
    theta = base.theta
    dens_a = base.a_dens
    dens_b = base.b_dens

    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 10))

    consumptions = ['Qoutlet (fact), st. m3/s', 'Qoutlet (calc), st. m3/s']
    data_sample[consumptions].plot(ax=axes[0],
                                   legend=True, marker='o', markersize=1.2)

    pressures = ['Pinlet, Pa', 'Poutlet, Pa']
    ax0_2 = data_sample[pressures].plot(ax=axes[0], secondary_y=True,
                                        legend=True, marker='o', markersize=1.2)
    [t.set_visible(True) for t in axes[0].get_xticklabels()]
    axes[0].set_xlabel(data_sample.index.name).set_visible(True)

    press_min = data_sample['Poutlet, Pa'].min()
    press_max = data_sample['Pinlet, Pa'].max()
    press_step = (press_max - press_min) / 100
    press = np.arange(press_min, press_max, press_step)
    perm = np.zeros(press.shape, dtype=float)
    for i in range(len(theta)):
        perm += np.power(press, i) * theta[i]
    perm_curve = axes[1].plot(press, perm, label='permeability')

    dens = dens_a * press + dens_b
    ax1_2 = axes[1].twinx()
    dens_curve = ax1_2.plot(press, dens, 'tab:grey', label='density')

    curves = perm_curve + dens_curve
    labels = [l.get_label() for l in curves]
    axes[1].legend(curves, labels, loc=9)

    if y_min is not None and y_max is not None:
        axes[0].set_ylim([float(y_min), float(y_max)])
    if y2_min is not None and y2_max is not None:
        ax0_2.set_ylim([float(y2_min), float(y2_max)])

    fig.suptitle(title)
    axes[0].set_title('Consumptions and Pressures')
    axes[1].set_title('Permeability and Density')

    axes[0].set_ylabel('consumption, m3/s')
    ax0_2.set_ylabel('pressure, Pa')
    axes[1].set_ylabel('permeability, m2')
    axes[1].set_xlabel('pressure, Pa')
    ax1_2.set_ylabel('density, kg/m3')

    axes[0].grid(True, which='major', axis='y')
    axes[0].grid(True, which='major', axis='x')
    axes[1].grid(True, which='major', axis='y')
    axes[1].grid(True, which='major', axis='x')

    axes[0].ticklabel_format(axis='y', style='sci', scilimits=(-2, 2))
    ax0_2.ticklabel_format(axis='y', style='sci', scilimits=(-2, 2))
    axes[1].ticklabel_format(axis='y', style='sci', scilimits=(-2, 2))
    axes[1].ticklabel_format(axis='x', style='sci', scilimits=(-2, 2))

    diff_text = 'Qoutlet Calculation Accuracy\n'
    diff_text += '(relative deviation)\n'
    diff_text += '\nmean    ' + "{:.2e}".format(data_sample['Gerror'].mean())
    diff_text += '\nstd        ' + "{:.2e}".format(data_sample['Gerror'].std())
    diff_box = mpl.offsetbox.AnchoredText(diff_text, loc=6)
    axes[0].add_artist(diff_box)

    plt.show()
