# Midnight-Music-Sync
Syncs music so the drop hits at Midnight

# Usage:
This used to be a Jupyter Notebook... 
The idea is that the code will ask you for a tracks duration in Minutes:Seconds.Milliseconds and for the moment it drops.
It could be any moment in the track, anything remarkable that you want it to hit.

When calling the main function "play_track" you will have to pass the date that you want it to happen. For NYE's that's usually 01/01/YEAR.

It should default to midnight but you can also pass the time as a parameters, here's a couple examples:

# Note:
If it's not possible to reach the target time it will error out and exit.
For most things the script will ask you about minutes, seconds and milliseconds. You don't have to worry about inputting formats too perfectly for that.
Although for the date... It's not as perfect but I have specified the format
