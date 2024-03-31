import numpy as np
import matplotlib.pyplot as plt

# Konstanta dan Variabel
h_pangkalan = 1  # kilometer
v_o = 5  # km/s
theta = np.radians(30)  # konversi sudut ke radian
g = 9.8 / 1000  # km/s^2

# Hitung waktu yang diperlukan (t)
t = (v_o * np.sin(theta)) / g

# Hitung jarak horizontal maksimum (R)
R = v_o * t * np.cos(theta)

# Hitung ketinggian maksimum (h_maksimum)
h_maksimum = h_pangkalan + (v_o**2 * np.sin(theta)**2) / (2 * g)

# Buat lintasan peluru
t_array = np.linspace(0, 2*t, 100)
x_peluru = v_o * np.cos(theta) * t_array
y_peluru = h_pangkalan + (v_o * np.sin(theta) * t_array) - (0.5 * g * t_array**2)

# Plot lintasan peluru
plt.plot(x_peluru, y_peluru)
plt.xlabel('Jarak Horizontal (km)')
plt.ylabel('Ketinggian (km)')
plt.title('Lintasan Peluru Menuju Ketinggian Maksimum')
plt.grid(True)
plt.show()

# Tampilkan hasil
print(f"Jarak horizontal maksimum yang dapat dicapai oleh satelit sebelum masuk ke orbit adalah {R:.2f} kilometer.")
print(f"Waktu yang diperlukan satelit untuk mencapai ketinggian maksimumnya adalah {t:.2f} detik.")
print(f"Ketinggian maksimum yang dapat dicapai oleh satelit adalah {h_maksimum:.2f} kilometer.")
