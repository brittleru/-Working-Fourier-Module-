# Fourier Module for the sum of the harmonic components
This is the next phase of another project, it consists of a python module that allows us to calculate the Fourier series coefficients and sum the harmonic components, 
regardless of the type of signal. Is a work in progress, I work under the supervision of Dr. Ing. Philip Coanda. **The goal** of this project is to transform an audio file into a list of values that we can plot and use that signal in our harmonic component gathering application.
</br></br>
The inputs should be <code>m</code> which is the number of periods, and <code>n</code> the number of waves. The function <code>dreptunghi()</code> takes as parameters frequency 
<code>f</code>, number of samples <code>N</code> and the time base <code>T</code> it should return a list with <code>g</code> the value at the time <code>t</code> which is the 
discrete time, the increment <code>dt</code>, the number of samples <code>N</code> and the frequency <code>f</code>. The function <code>coef()</code> takes as parameters the signal
<code>s</code>, the frequency <code>f</code>, the increment <code>dt</code> and the number of samples <code>N</code>, here is the mathematical logic for the Fourier even coefficients 
an and odd coefficients bn and forming the lists for waves and it's sum, those two being what the function <code>coef()</code> will return.

## For the moment those are the results:
### The original signal for square: 
![Original signal sqare](https://github.com/brittleru/-Working-Fourier-Module-/blob/master/original_signal.jpeg?raw=true)

### First 5 waves:
![alt text](https://github.com/brittleru/-Working-Fourier-Module-/blob/master/first_five_waves.jpeg?raw=true)

### The original signal for square:
![alt text](https://github.com/brittleru/-Working-Fourier-Module-/blob/master/harmonics_and_sum.jpeg?raw=true)
