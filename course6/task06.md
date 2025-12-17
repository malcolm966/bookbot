

# Assignment
FPS stands for frames per second. We're going to restrict our game to draw a maximum of 60 times per second, or 60 FPS.

After initializing pygame, but before the game loop starts, create:
A new clock object using pygame.time.Clock.
A dt variable set to 0.
At the end of each iteration of the game loop, call the .tick() method on the clock object, and pass it 60. It will pause the game loop until 1/60th of a second has passed.
The .tick() method also returns the amount of time that has passed since the last time it was called: the delta time. Divide the return value by 1000 (to convert from milliseconds to seconds) and save it into the dt variable we created earlier.
Print the updated dt value to the console.
Re-run the game. You should still see the same black screen, but this time it should use less of your system's resources! You should also see the dt value printed over and over to the console, it may even fluctuate a bit as your computer's CPU speed changes.
Remove the line that prints dt to the console (but leave the variable itself, we'll need it later) - it creates a lot of noise, we just wanted to see it working.
If everything is still working as you'd expect, run and submit the CLI tests.

# Check
Run the CLI commands to test your solution.

jq -s '.[2].elapsed_s - .[0].elapsed_s >= 1' game_state.jsonl
Expecting exit code: 0
Expecting stdout to contain all of:
true