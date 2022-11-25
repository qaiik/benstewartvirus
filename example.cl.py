import chilledwin as cw

orig = cw.screenshot()

man = cw.Displayer()

man.say('Hello, since you have executed this, I will take over your pc.')
man.say('Ready?')

man.fitDisplay(cw.rotate(orig, -45), 1000)
man.fitDisplay(cw.rotate(orig, 45), 1000)
man.fitDisplay(cw.rotate(orig, -45), 1000)
man.fitDisplay(cw.rotate(orig, 45), 1000)
man.fitDisplay(cw.rotate(orig, -45), 1000)
man.fitDisplay(cw.rotate(orig, 45), 1000)
man.fitDisplay(cw.rotate(orig, -45), 1000)
man.fitDisplay(cw.rotate(orig, 45), 1000)
man.say('Ok, on to the next phase')
man.say('I will now remove display colors and freeze device')
man.fitDisplay(cw.gray(orig), 5000)
man.say('Like it?')
man.say('I will now invert them')
man.fitDisplay(cw.invert(orig), 5000)
man.say('Next')

for i in range(1,8+1):
    man.fitDisplay(cw.distort(orig, i), 200)

man.say('Not done')
man.fitDisplay(cw.distort(orig,1),200)
man.fitDisplay(cw.distort(orig,8),200)
man.fitDisplay(cw.distort(orig,1),200)
man.fitDisplay(cw.distort(orig,8),200)
man.fitDisplay(cw.distort(orig,1),200)
man.fitDisplay(cw.distort(orig,8),200)
man.fitDisplay(cw.distort(orig,1),200)
man.fitDisplay(cw.distort(orig,8),200)
man.fitDisplay(cw.distort(orig,1),200)
man.fitDisplay(cw.distort(orig,8),200)
man.fitDisplay(cw.distort(orig,1),200)
man.fitDisplay(cw.distort(orig,8),200)
man.fitDisplay(cw.distort(orig,1),200)
man.fitDisplay(cw.distort(orig,8),200)
man.fitDisplay(cw.distort(orig,1),200)
man.fitDisplay(cw.distort(orig,8),200)
man.fitDisplay(cw.distort(orig,1),200)
man.fitDisplay(cw.distort(orig,8),200)
man.fitDisplay(cw.distort(orig,1),200)
man.fitDisplay(cw.distort(orig,8),200)
man.fitDisplay(cw.distort(orig,1),200)
man.fitDisplay(cw.distort(orig,8),200)
man.fitDisplay(cw.distort(orig,1),200)
man.fitDisplay(cw.distort(orig,8),200)
man.fitDisplay(cw.distort(orig,1),200)
man.fitDisplay(cw.distort(orig,8),200)
man.fitDisplay(cw.distort(orig,1),200)
man.fitDisplay(cw.distort(orig,8),200)

man.say('Now, bye bye!')
cw.sound('glitch.wav')
man.fitDisplay(cw.Image.open('ren.png'), 6000)
man.say('Lol, jk')





