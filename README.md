# dataloop_pacman_assignment

I calculated each ghost's current distance from pacman, and tried to discern which way (up / right / down / left) is best in terms of getting closer to pacman.
Ideally (i.e. if there were no obstacles), only pacman's coords would dictate each ghost's next step (i.e. if pacman's x > ghost.x, move to (ghost.x+1, ghost.y)).  
If this move is impossible because of walls or other ghosts, I would try the same process for the other coordinate that would get me closer to pacman, and if that wasn't possible, I would try to understand which one of the remaining coordinates (both get me farther away from pacman) is available, and move there.

If I had more time, I would implement the above recursively for each step, and also try to understand if it's possible to calculate the BEST step among available steps, without breaking complexity. 
I would also translate the implementation to use the board from the .npy file instead of a simple list of lists. 
