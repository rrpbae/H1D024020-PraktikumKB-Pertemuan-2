import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

suhu = ctrl.Antecedent(np.arange(0, 41, 1), 'suhu')
kelembapan = ctrl.Antecedent(np.arange(0, 101, 1), 'kelembapan')
kecepatan = ctrl.Consequent(np.arange(0, 101, 1), 'kecepatan')

suhu['dingin'] = fuzz.trimf(suhu.universe, [0, 0, 20])
suhu['normal'] = fuzz.trimf(suhu.universe, [15, 25, 35])
suhu['panas'] = fuzz.trimf(suhu.universe, [30, 40, 40])

kelembapan['kering'] = fuzz.trimf(kelembapan.universe, [0, 0, 50])
kelembapan['lembab'] = fuzz.trimf(kelembapan.universe, [30, 50, 70])
kelembapan['basah'] = fuzz.trimf(kelembapan.universe, [60, 100, 100])

kecepatan['lambat'] = fuzz.trimf(kecepatan.universe, [0, 0, 50])
kecepatan['sedang'] = fuzz.trimf(kecepatan.universe, [30, 50, 70])
kecepatan['cepat'] = fuzz.trimf(kecepatan.universe, [60, 100, 100])

rule1 = ctrl.Rule(suhu['dingin'] | kelembapan['basah'], kecepatan['lambat'])
rule2 = ctrl.Rule(suhu['normal'], kecepatan['sedang'])
rule3 = ctrl.Rule(suhu['panas'] & kelembapan['kering'], kecepatan['cepat'])

kipas_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
simulasi_kipas = ctrl.ControlSystemSimulation(kipas_ctrl)

suhu_input = 32
kelembapan_input = 40

simulasi_kipas.input['suhu'] = suhu_input
simulasi_kipas.input['kelembapan'] = kelembapan_input

simulasi_kipas.compute()

print("====================================")
print("HASIL LOGIKA FUZZY KIPAS ANGIN")
print("====================================")
print(f"Input Suhu       : {suhu_input} °C")
print(f"Input Kelembapan : {kelembapan_input} %")
print(f"Hasil Kecepatan  : {simulasi_kipas.output['kecepatan']:.2f}")
print("====================================")

suhu.view()
kelembapan.view()
kecepatan.view(sim=simulasi_kipas)

plt.show()