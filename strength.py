import collections

def m_round(x, base=5):
    return int(base * round(float(x)/base))


program_duration = 12
maxes = {
	"bench_press" : 210,
	"squat" : 280,
	"overhead_press" : 135,
	"deadlift" : 395
}

exercises = {
	"bench_press": "Bench Press",
	"squat" : "Squat",
	"overhead_press" : "Overhead Press",
	"deadlift" : "Deadlift"
}

program = {}
press_increment = 5
lower_increment = 10

def create_strength_program(maxes, program_duration=12):
	progression = [0.75, 0.8, 0.85, 0.6]
	scheme      = ["4x7","6x5", "8x3", "5x5"]

	cycle_length = 4
	current_increment = 0
	for week in range(program_duration):
		if week > 0 and (week % cycle_length == 0):
			current_increment += 1

		program[str(week + 1)] = {"bench_press": "{} for {}".format(m_round(0.9*progression[week%4]*(maxes["bench_press"]+press_increment*current_increment)),        scheme[week%4]),
										  "squat" : "{} for {}".format(m_round(0.9*progression[week%4]*(maxes["squat"]+lower_increment*current_increment)),                   scheme[week%4]),
										  "overhead_press" : "{} for {}".format(m_round(0.9*progression[week%4]*(maxes["overhead_press"]+press_increment*current_increment)), scheme[week%4]),
										  "deadlift" : "{} for {}".format(m_round(0.9*progression[week%4]*(maxes["deadlift"]+lower_increment*current_increment)),             scheme[week%4])
										  }
	return program


current_program = create_strength_program(maxes, program_duration=12)

for week, training_weights in current_program.items():
	print("Week {} of Training".format(week))
	for exercise_name, training_weight in training_weights.items():
		print("{} {}".format(exercises[exercise_name], training_weight))
	if int(week) < program_duration:
		print("\n\n")

	# print("{} of training".format(week))
	# print("Bench Press    {}".format(weights["bench_press"]))
	# print("Squat          {}".format(weights["squat"]))
	# print("Overhead Press {}".format(weights["overhead_press"]))
	# print("Deadlift       {}\n\n".format(weights["deadlift"]))