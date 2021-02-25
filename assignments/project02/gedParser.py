# Eric Altenburg
# I pledge my honor that I have abided by the Stevens Honor System.

f = open('family.ged', 'r')
lines = f.readlines()

tags = ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]

for line in lines:
	split = line.split();

	level = split[0]
	start = 2
	end = len(split)
	tag = split[1]
	args = ""

	if (tag in tags):
		validOutput = "Y"

		if (tag == "NAME" and level == "2"):
			validOutput = "N"
		elif (tag == "DATE" and level == "1"):
			validOutput = "N"
	elif (len(split) == 3 and (split[2] == "INDI" or split[2] == "FAM")):
		validOutput = "Y"
		start = 1
		end-=1
		tag = split[2]
	else:
		validOutput = "N"

	for x in split[start:end]:
		args += (x + " ")

	print("--> " + line)
	print("<-- " + level + "|" + tag + "|" + validOutput + "|" + args + "\n")

f.close()
