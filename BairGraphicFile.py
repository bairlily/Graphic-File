import matplotlib.pyplot as plot
# set up your lists
numlist = [11, 12, 7, 4]
namelist = ['freshmen', 'sophomores', 'juniors', 'seniors']
colorlist = ['orange', 'purple', 'blue', 'yellow' ]
explodelist = [0.0, 0.0, 0.0, 0.0]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.2f%%', colors=colorlist,
    	explode = explodelist, startangle = 90)
plot.axis('equal')
plot.savefig('piechart.png')
