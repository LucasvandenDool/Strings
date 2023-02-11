# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
ruud = 'Ruud Gullit'
bast = 'Marco van Basten'
goal_0 = '32'
goal_1 = '54'

scorers = f"{ruud} {goal_0}, {bast} {goal_1}"
print(scorers)

report = f"{ruud} scored in the {goal_0}nd minute \n{bast} scored in the {goal_1}th minute"
print(report)

player = ['Ruud', 'Gullit']
first_name = player[0]
last_name_len = len(player[1])
name_short = f"{player[0][0]}. {player[1]}"

x = len(player[0])
ex = '!'
chant = f"{player[0]}{ex}" * x
print(chant)

good_chant = chant[-1] != ' '
print(good_chant)



