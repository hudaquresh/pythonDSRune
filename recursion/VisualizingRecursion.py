import turtle
import random 

myTurtle = turtle.Turtle() 
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen): 
	if lineLen > 0: 
		myTurtle.forward(lineLen)
		myTurtle.right(90)
		drawSpiral(myTurtle, lineLen-5) 

def tree(branchLen, t): 
	if branchLen > 5:
		if branchLen < 10: 
			t.pencolor("green")  
		t.forward(branchLen)
		t.right(random.randrange(15,46)) 
		tree(branchLen-random.randrange(0,15),t)
		t.left(random.randrange(15,46))
		tree(branchLen-random.randrange(0,10),t)
		t.right(random.randrange(15,46))
		t.backward(branchLen) 

def main():  
	t = turtle.Turtle() 
	myWin = turtle.Screen()
	t.left(90)
	t.up()
	t.backward(100)
	t.down()
	t.color('black')
	tree(75,t)
	myWin.exitonclick()
	
#	drawSpiral(myTurtle, 100)
#	myWin.exitonclick() 

main() 
