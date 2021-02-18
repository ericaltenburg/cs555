# Eric Altenburg
# I pledge my honor that I have abided by the Stevens Honor System.

f = open('family.ged', 'r')
lines = f.readlines()

tags = ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]

for line in lines:
	split = line.split();

	level = split[0]
	start = 2