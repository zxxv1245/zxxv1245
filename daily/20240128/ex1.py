#아스키 코드 
#0~9 => 48~57 0 1 2 3 4 5 6 7 8 9
#A~Z => 65~90 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#a~z => 97~122 a b c d e f g h i j k l m n o p q r s t u v w x y z

T = input()

number_str = '0123456789'

upper_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

lower_str = 'abcdefghijklmnopqrstuvwxyz'

tot_as = []

for a in enumerate(number_str, start = 48) :
    tot_as.append(a[0])

for b in enumerate(upper_str, start = 65) :
    tot_as.append(b[0])

for c in enumerate(lower_str, start = 97) :
    tot_as.append(c[0])

tot = number_str + upper_str + lower_str
TT = tot.find(T)
print(tot_as[TT])