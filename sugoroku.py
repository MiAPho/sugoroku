import random
goal_pos=20
num=int(input("何人>"))
membersPos=[0]*num
continue_game=True
while continue_game:
	for i in range(num):
		dice=random.randint(1,6)
		membersPos[i]=membersPos[i]+dice
		backStep=0
		if membersPos[i]>goal_pos:
			backStep=membersPos[i]-goal_pos
			membersPos[i]=goal_pos-backStep
		if backStep>0:
			print(f'Overしたので{backStep}戻った')
		print(f'P{i+1}...{membersPos[i]}({dice})')
		for j in range(goal_pos):
			if membersPos[i]<goal_pos and j==goal_pos-1:
				print('|')
			elif j<membersPos[i]:
				print('☆',end="")
			else:
				print(' ',end="")
		if membersPos[i]==goal_pos:
			print()
			print(f'Goal! P{i+1} Win!')
			continue_game=False
			break
		if membersPos[i]>goal_pos:
			backStep=membersPos[i]-goal_pos
			membersPos[i]=goal_pos-backStep
		input()
