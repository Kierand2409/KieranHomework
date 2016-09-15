seq1="CGCAGCTAACGCATTAAGCACTCCGCCTGGGGAGTACGACCGCAAGGTTGAA"

countA=0
countT=0
countC=0
countG=0

for nextCharacter in seq1:
	print (nextCharacter)
	if nextCharacter == "A":
		countA=countA+1
	elif nextCharacter == "T":
		countT=countT+1
	elif nextCharacter == "C":
		countC=countC+1
	else nextCharacter == "G":
		countG=countG+1
		
print ('sequence:', 'CGCAGCTAACGCATTAAGCACTCCGCCTGGGGAGTACGACCGCAAGGTTGAA') > ncounts.txt
print 'A\'s', countA >> ncounts.txt
print 'C\'s', countC >> ncounts.txt
print 'T\'s', countT >> ncounts.txt
print 'G\'s', countG
print 'GC content\:' countG+countC

seq2="CGGATCGTAAAGCTCTGTTGTTGGTGAAGAAGGATAGAGGTAGTAACTGGCCT"

countA=0
countT=0
countC=0
countG=0

for nextCharacter in seq1:
	print (nextCharacter)
	if nextCharacter == "A":
		countA=countA+1
	elif nextCharacter == "T":
		countT=countT+1
	elif nextCharacter == "C":
		countC=countC+1
	else nextCharacter == "G":
		countG=countG+1
		
print ('sequence:', 'CGCAGCTAACGCATTAAGCACTCCGCCTGGGGAGTACGACCGCAAGGTTGAA')
print 'A\'s', countA #prints A's 14
print 'C\'s', countC
print 'T\'s', countT
print 'G\'s', countG
print 'GC content\:' countG+countC