# dataloop_pacman_assignment

## What did I do?
For every ghost, I query its surrounding cells and understand what my walking options are.
For every walking option, I calculate if it's closer or farther away from PacMan.
I take the closer-to-PacMan-move, add it to my walking-distance counter, and repeat the same process excluding the step I already took to avoid walking backwards.

## How did I do it?
I first had to figure out how to work with .npy very quickly.
...

## What can be improved?
I realize that this approach can be further optimised because sometimes there might be unexpected walls or other ghosts which block the road to get to PacMan. That challenges the whole assumption that every step brings me closer to PacMan. I'm not sure what the best way to approach that optimization, but with more time I can try to figure it out! ;p
