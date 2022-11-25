import terriblechilledwin as cw

orig = cw.Image.open('youhavnobitcoin.png')

man = cw.Displayer()


man.say("Hello I am stewart from stewart incorporated and I have identified a major problem with you.")
man.say("As the research shows, you have know bitcoin.")
man.fitDisplay(orig, 3000)
man.fitDisplay(cw.rotate(orig, -45), 1000)
man.fitDisplay(cw.rotate(orig, 45), 1000)
man.fitDisplay(cw.distort(cw.rotate(orig, 45), 8), 3000)