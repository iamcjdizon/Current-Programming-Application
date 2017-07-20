totalSeconds = int(input("Enter value for seconds: "))
hours = totalSeconds // 3600
minutes = totalSeconds // 60 % 60
seconds = totalSeconds % 60
print ("That\'s equivalent to: ", hours, " hours ,", minutes, " minutes, and ", seconds, " seconds")
