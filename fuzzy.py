import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Input variables
dirt = ctrl.Antecedent(np.arange(0, 11, 1), 'dirt')
grease = ctrl.Antecedent(np.arange(0, 11, 1), 'grease')

# Output variable
time = ctrl.Consequent(np.arange(0, 61, 1), 'time')

# Membership functions for dirt
dirt['low'] = fuzz.trimf(dirt.universe, [0, 0, 5])
dirt['medium'] = fuzz.trimf(dirt.universe, [0, 5, 10])
dirt['high'] = fuzz.trimf(dirt.universe, [5, 10, 10])

# Membership functions for grease
grease['low'] = fuzz.trimf(grease.universe, [0, 0, 5])
grease['medium'] = fuzz.trimf(grease.universe, [0, 5, 10])
grease['high'] = fuzz.trimf(grease.universe, [5, 10, 10])

# Membership functions for wash time
time['short'] = fuzz.trimf(time.universe, [0, 0, 30])
time['medium'] = fuzz.trimf(time.universe, [10, 30, 50])
time['long'] = fuzz.trimf(time.universe, [30, 60, 60])

# Define fuzzy rules
rule1 = ctrl.Rule(dirt['high'] | grease['high'], time['long'])
rule2 = ctrl.Rule(dirt['medium'] & grease['medium'], time['medium'])
rule3 = ctrl.Rule(dirt['low'] & grease['low'], time['short'])
rule4 = ctrl.Rule(dirt['medium'] & grease['low'], time['medium'])
rule5 = ctrl.Rule(dirt['low'] & grease['medium'], time['medium'])

# Create control system
wash_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
washing_machine = ctrl.ControlSystemSimulation(wash_ctrl)

# Input values (example)
washing_machine.input['dirt'] = 6
washing_machine.input['grease'] = 8

# Compute output
washing_machine.compute()

# Output result
print(f"Recommended wash time: {washing_machine.output['time']:.2f} minutes")

# Optional: Visualize result
time.view(sim=washing_machine)
plt.show()
