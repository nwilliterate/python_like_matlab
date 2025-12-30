"""
Advanced Example: Signal Processing
"""

from matlab import *

print("Advanced Example: Signal Processing")
print("=" * 60)

# Sampling parameters
fs = 1000  # Sampling frequency (Hz)
T = 1.0    # Duration (seconds)
t = linspace(0, T, int(fs * T))

# Signal generation: Sum of sinusoids at multiple frequencies
f1, f2, f3 = 50, 120, 200  # Frequencies (Hz)
signal = sin(2 * 3.14159 * f1 * t) + \
         0.5 * sin(2 * 3.14159 * f2 * t) + \
         0.3 * sin(2 * 3.14159 * f3 * t)

# Add noise
noise = 0.2 * randn(len(signal))
noisy_signal = signal + noise

# Visualization
figure(figsize=(12, 10))

# Original signal
subplot(3, 1, 1)
plot(t[:200], signal[:200], 'b-', linewidth=1.5)
xlabel('Time (s)')
ylabel('Amplitude')
title('Original Signal')
grid('on')

# Noisy signal
subplot(3, 1, 2)
plot(t[:200], noisy_signal[:200], 'r-', linewidth=1)
xlabel('Time (s)')
ylabel('Amplitude')
title('Noisy Signal')
grid('on')

# FFT (Frequency analysis)
subplot(3, 1, 3)
N = len(signal)
freq = linspace(0, fs/2, N//2)
fft_signal = abs(np.fft.fft(noisy_signal))
plot(freq, fft_signal[:N//2], 'g-', linewidth=1.5)
xlabel('Frequency (Hz)')
ylabel('Magnitude')
title('Frequency Spectrum (FFT)')
xlim(0, 300)
grid('on')

savefig('signal_processing.png', dpi=150)
print("Graph saved as 'signal_processing.png'.")
show()
