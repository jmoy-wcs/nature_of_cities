import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from os.path import join
plt.style.use('ggplot')

wb_path = r'F:\working_copies\nature_of_cities\data\four figures_copy.xlsx'
outputs = r'F:\working_copies\nature_of_cities\figures'

# Formating
dpi = 300
w = 1812 / dpi
h = 810 / dpi
matplotlib.rc('xtick', labelsize=6)
matplotlib.rc('ytick', labelsize=6)
label_size = 6
title_size = 8
x_lim = (-10000, 2100)
# Population
pop_df = pd.read_excel(wb_path, sheetname='population', header=7)

fig1 = plt.figure(figsize=(w, h))
ax1 = fig1.add_subplot(111)
ax1.plot(pop_df.Year, pop_df['Population (millions)'])
plt.xlim(x_lim[0], x_lim[1])
plt.title('Human Population', fontsize=title_size)
plt.xlabel('Year', fontsize=label_size)
plt.ylabel('Population (millions)', fontsize=label_size)
fig1.savefig(join(outputs, 'population.jpg'), dpi=dpi)


# Urbanization
urb_df = pd.read_excel(wb_path, sheetname='urbanization', header=4)

fig2 = plt.figure(figsize=(w, h))
ax2 = fig2.add_subplot(111)
ax2.plot(urb_df.Year, urb_df['Urbanization (% population)'])
plt.xlim(x_lim[0], x_lim[1])
plt.title('Urbanization', fontsize=title_size)
plt.xlabel('Year', fontsize=label_size)
plt.ylabel('Urbanization (% population)', fontsize=label_size)
fig2.savefig(join(outputs, 'urbanization.jpg'), dpi=dpi)

# GDP
gdp_df = pd.read_excel(wb_path, sheetname='GDP', header=5)
fig3 = plt.figure(figsize=(w, h))
ax3 = fig3.add_subplot(111)
ax3.plot(gdp_df.Year, gdp_df['GDP (billions of constant 2011 USD)'])
plt.xlim(x_lim[0], x_lim[1])
plt.title('Size of the world economy', fontsize=title_size)
plt.xlabel('Year', fontsize=label_size)
plt.ylabel('GDP (billions of constant 2011 USD)', fontsize=label_size)
fig3.savefig(join(outputs, 'gdp.jpg'), dpi=dpi)


# CO2
co2_df = pd.read_excel(wb_path, sheetname='CO2', header=4)

fig4 = plt.figure(figsize=(w, h))
ax4 = fig4.add_subplot(111)
ax4.plot(co2_df.Year, co2_df['Atmospheric carbon dioxide concentration (ppm)'])
plt.xlim(x_lim[0], x_lim[1])
plt.title('Atmospheric carbon dioxide', fontsize=title_size)
plt.xlabel('Year', fontsize=label_size)
plt.ylabel('Atmospheric carbon dioxide concentration (ppm)', fontsize=label_size)
fig4.savefig(join(outputs, 'co2.jpg'), dpi=dpi)