import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Define fuzzy variables
hard_work = ctrl.Antecedent(np.arange(0, 11, 1), 'hard_work')
physics = ctrl.Antecedent(np.arange(0, 101, 1), 'physics')
maths = ctrl.Antecedent(np.arange(0, 101, 1), 'maths')
chemistry = ctrl.Antecedent(np.arange(0, 101, 1), 'chemistry')
risk = ctrl.Consequent(np.arange(0, 11, 1), 'risk')

# Membership functions for hard work
hard_work['low'] = fuzz.trimf(hard_work.universe, [0, 0, 5])
hard_work['medium'] = fuzz.trimf(hard_work.universe, [3, 5, 7])
hard_work['high'] = fuzz.trimf(hard_work.universe, [5, 10, 10])

# Membership functions for marks
for subject in [physics, maths, chemistry]:
    subject['low'] = fuzz.trimf(subject.universe, [0, 0, 50])
    subject['average'] = fuzz.trimf(subject.universe, [30, 50, 70])
    subject['high'] = fuzz.trimf(subject.universe, [60, 100, 100])

# Membership functions for risk
risk['high'] = fuzz.trimf(risk.universe, [6, 10, 10])
risk['medium'] = fuzz.trimf(risk.universe, [3, 5, 7])
risk['low'] = fuzz.trimf(risk.universe, [0, 0, 4])

# Define fuzzy rules
rules = [
    ctrl.Rule(hard_work['low'] & physics['low'], risk['high']),
    ctrl.Rule(hard_work['low'] & maths['low'], risk['high']),
    ctrl.Rule(hard_work['low'] & chemistry['low'], risk['high']),
    ctrl.Rule(hard_work['medium'] & physics['average'] & maths['average'], risk['medium']),
    ctrl.Rule(hard_work['medium'] & chemistry['low'], risk['medium']),
    ctrl.Rule(hard_work['high'] & physics['high'] & maths['high'] & chemistry['high'], risk['low']),
    ctrl.Rule(hard_work['high'] & physics['average'], risk['medium']),
    ctrl.Rule(hard_work['medium'] & maths['high'] & chemistry['high'], risk['low']),
    ctrl.Rule(hard_work['medium'] & physics['high'] & maths['low'], risk['medium']),
    ctrl.Rule(hard_work['high'] & physics['low'], risk['medium']),
    ctrl.Rule(hard_work['high'] & physics['low'] & maths['low'] & chemistry['low'], risk['medium']),
]


# Control system
risk_ctrl = ctrl.ControlSystem(rules)
risk_simulation = ctrl.ControlSystemSimulation(risk_ctrl)

# Sample input
risk_simulation.input['hard_work'] = 5   # out of 10
risk_simulation.input['physics'] = 50      # out of 100
risk_simulation.input['maths'] = 42
risk_simulation.input['chemistry'] = 58

# Compute the result
print("Input set:")
print(risk_simulation.input)

risk_simulation.compute()
output = risk_simulation.output['risk']
print(f"Calculated Risk Level Score: {output:.2f}")

# Interpret result
if output > 6:
    level = "High Risk"
elif output > 3:
    level = "Medium Risk"
else:
    level = "Low Risk"

print(f"Risk Level: {level}")
risk.view(sim= risk_simulation)
plt.show()
