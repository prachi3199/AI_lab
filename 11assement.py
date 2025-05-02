import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables
attendance = ctrl.Antecedent(np.arange(0, 101, 1), 'attendance')
marks = ctrl.Antecedent(np.arange(0, 101, 1), 'marks')
discipline = ctrl.Antecedent(np.arange(0, 11, 1), 'discipline')
performance = ctrl.Consequent(np.arange(0, 101, 1), 'performance')

# Membership functions for attendance
attendance['low'] = fuzz.trimf(attendance.universe, [0, 0, 50])
attendance['medium'] = fuzz.trimf(attendance.universe, [30, 50, 70])
attendance['high'] = fuzz.trimf(attendance.universe, [60, 100, 100])

# Membership functions for marks
marks['low'] = fuzz.trimf(marks.universe, [0, 0, 50])
marks['medium'] = fuzz.trimf(marks.universe, [30, 50, 70])
marks['high'] = fuzz.trimf(marks.universe, [60, 100, 100])

# Membership functions for discipline
discipline['bad'] = fuzz.trimf(discipline.universe, [0, 0, 5])
discipline['average'] = fuzz.trimf(discipline.universe, [3, 5, 7])
discipline['good'] = fuzz.trimf(discipline.universe, [6, 10, 10])

# Membership functions for performance
performance['poor'] = fuzz.trimf(performance.universe, [0, 0, 50])
performance['average'] = fuzz.trimf(performance.universe, [30, 50, 70])
performance['excellent'] = fuzz.trimf(performance.universe, [60, 100, 100])

# Define fuzzy rules
rules = [
    ctrl.Rule(attendance['high'] & marks['high'] & discipline['good'], performance['excellent']),
    ctrl.Rule(attendance['medium'] | marks['medium'] | discipline['average'], performance['average']),
    ctrl.Rule(attendance['low'] & marks['low'], performance['poor']),
    ctrl.Rule(discipline['bad'] & (attendance['medium'] | marks['medium']), performance['poor']),
    ctrl.Rule(attendance['high'] & marks['medium'] & discipline['good'], performance['average']),

    # Additional rules
    ctrl.Rule(attendance['low'] & marks['high'] & discipline['good'], performance['average']),
    ctrl.Rule(attendance['medium'] & marks['low'] & discipline['average'], performance['poor']),
    ctrl.Rule(attendance['high'] & marks['low'] & discipline['bad'], performance['poor']),
    ctrl.Rule(attendance['medium'] & marks['medium'] & discipline['good'], performance['average']),
    ctrl.Rule(attendance['medium'] & marks['high'] & discipline['average'], performance['excellent']),
    ctrl.Rule(attendance['high'] & marks['high'] & discipline['average'], performance['excellent']),
    ctrl.Rule(attendance['low'] & marks['medium'] & discipline['average'], performance['poor'])
]

# Control system and simulation
performance_ctrl = ctrl.ControlSystem(rules)
performance_sim = ctrl.ControlSystemSimulation(performance_ctrl)

# Set input values
performance_sim.input['attendance'] = 75
performance_sim.input['marks'] = 80
performance_sim.input['discipline'] = 7

# Perform computation
performance_sim.compute()

# Output result
print("Student Performance:", round(performance_sim.output['performance'], 2))
