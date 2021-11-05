#!/usr/bin/env python
import sys
for line in sys.stdin:

	tel    = ""
	duree  = "z"
	de     = "z"
	nom    = "z"
	prenom = "z"
	dept   = "z"
	ville  = "z"

	line   = line.strip()         
	splits = line.split("\t")


# 		"""
# 		-- calls(de, vers, duree)
# 		-- users(nom, prenom, tel, dept, ville)

# 		SELECT ville, count(*)
# 		FROM users, calls
# 		WHERE dept = 78
# 		AND tel = vers
# 		GROUP BY ville
# 		HAVING count(*) > 2;
# 		"""


	if len(splits) == 5:
		nom    = splits[0]
		prenom = splits[1]
		tel    = splits[2]
		dept   = splits[3]
		ville  = splits[4]
	else:
		de     = splits[0]
		tel    = splits[1]
		duree  = splits[2]                 
	print('%s\t%s\t%s\t%s\t%s\t%s\t%s' % (tel, nom, prenom, de, dept, ville, duree))
















# #!/usr/bin/env python
 
# import sys
 
# # input comes from STDIN (standard input)
# for line in sys.stdin:
# 	try: #sometimes bad data can cause errors use this how you like to deal with lint and bad data
        
# 		nom = "-" 
# 		prenom = "-" 
# 		tel = "" 
# 		dept = "-" 
# 		ville = "-" 
# 		duree = "-" 

# 		"""
# 		-- calls(de, vers, duree)
# 		-- users(nom, prenom, tel, dept, ville)

# 		SELECT ville, count(*)
# 		FROM users, calls
# 		WHERE dept = 78
# 		AND tel = vers
# 		GROUP BY ville
# 		HAVING count(*) > 2;
# 		"""

# 		# remove leading and trailing whitespace
# 		line = line.strip()

# 		splits = line.split("\t") 

# 		if len(splits) == 5: #users data
# 			nom     = splits[0]
# 			prenom  = splits[1]
# 			tel     = splits[2]
# 			dept    = splits[3]
# 			ville   = splits[4]
# 		else:				 #calls data
# 			tel     = splits[1]
# 			duree   = splits[2]        

# 		print('%s\t%s\t%s\t%s\t%s\t%s' % (tel, nom, prenom, dept, ville, duree))
# 	except: 
# 		pass