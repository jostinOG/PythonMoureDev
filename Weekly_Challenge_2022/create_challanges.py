path=r'C:\Users\JOSTI\PycharmProjects\cursoPython\ejercicios/'
type='.py'
path_final=''
for i in range(51):
    path_final=path + str(i) + '_challenge' + type
    file = open(path_final, "w")