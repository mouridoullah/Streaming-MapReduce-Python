#!/usr/bin/env python
import sys
import string

last_user_tel = None
cur_de        = ""
cur_duree     = ""
cur_nom       = "z"
cur_prenom    = "z"
cur_dept      = "z"
cur_ville     = "z"

for line in sys.stdin:
    line = line.strip()
    tel, nom, prenom, de, dept, ville, duree = line.split("\t")


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

    # if this is the first iteration
    if not last_user_tel or last_user_tel != tel:
        last_user_tel = tel
        cur_duree     = duree
        cur_de        = de
        cur_nom       = nom
        cur_prenom    = prenom
        cur_dept      = dept
        cur_ville     = ville
    elif tel == last_user_tel:
        duree         = cur_duree
        de            = cur_de
        nom           = cur_nom
        prenom        = cur_prenom
        dept          = cur_dept
        ville         = cur_ville
        
        print('%s\t%s\t%s\t%s\t%s' % (tel, nom, prenom, dept, ville))





























# #!/usr/bin/env python
# import sys
# import string

# lastTel   = None
# curNom    = "-"
# curPrenom = "-"
# curDept   = "-"
# curVille  = "-"
# curDuree  = "-"

# for line in sys.stdin:
# 	line = line.strip()
# 	"""tel, nom, prenom, dept, ville, duree""" splits = line.split("\t")

# 	#print('%s\t%s\t%s\t%s\t%s\t%s' % (tel, nom, prenom, dept, ville, duree))
# 	"""
# 	-- calls(de, vers, duree)
# 	-- users(nom, prenom, tel, dept, ville)

# 	SELECT ville, count(*)
# 	FROM users, calls
# 	WHERE dept = 78
# 	AND tel = vers
# 	GROUP BY ville
# 	HAVING count(*) > 2;
# 	"""

# 	if not lastTel or lastTel != tel:
# 		#print("------------------------------------on rentre")
# 		lastTel   = tel
# 		curNom    = nom
# 		curPrenom = prenom
# 		curDept   = dept
# 		curVille  = ville
# 		curDuree  = duree
# 		#print('%s\t%s\t%s\t%s\t%s\t%s' % (lastTel, curNom, curPrenom, curDept, curVille, curDuree))
# 	elif tel == lastTel:
# 		#print("on Ne rentre Pas")
# 		nom       = curNom
# 		prenom    = curPrenom
# 		dept      = curDept
# 		ville     = curVille
# 		duree     = curDuree
# 		print('%s\t%s\t%s\t%s\t%s\t%s' % (tel, nom, prenom, dept, ville, duree))

	







# #!/usr/bin/env python
# import sys
# import string


# # maps words to their counts
# foundKey     = ""
# foundValue   = ""
# isFirst      = 1
# currentCount = 0
# curTel       = "-"
# curNom       = "-"
# curPrenom    = "-"
# curDept      = "-"
# curVille     = "-"
# curDuree     = "-"
# isTelMappingLine = False

# for line in sys.stdin:
# 	line = line.strip()

# 	try:
# 		tel, nom, prenom, dept, ville, duree = line.split("\t")

# 		if nom == "-":
# 			curTel = tel
# 			curDuree = duree
# 			isTelMappingLine = True
# 		else:
# 			isTelMappingLine = False

# 		if not isTelMappingLine:
# 			if curTel != tel:
# 				curTel = tel
# 				curVille = ville
# 				curDept = dept

# 			currentKey = '%s\t%s\t%s\t%s\t%s' % (curTel, nom, prenom, dept, ville)

# 			if foundKey != currentKey:
# 				if isFirst == 0:
# 					print('%s\t%s'%(foundKey,currentCount))
# 					currentCount = 0
# 				else:
# 					isFirst = 0

# 				foundKey = currentKey

# 			currentKey += 1
# 	except:
# 		pass

# try:
# 	print('%s\t%s' % (foundKey, currentCount))
# except:
# 	pass










