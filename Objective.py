# Function checking objective
def checkObjective(objective_score, scores):
	objective = False
	for s in scores:
		if s[0] >= objective_score and s[1] >= objective_score:
			objective = True
	return objective
