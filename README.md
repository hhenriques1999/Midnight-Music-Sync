# Midnight-Music-Sync
Syncs music so the drop hits at Midnight

# Usage:
This used to be a Jupyter Notebook... 
The idea is that the code will ask you for a tracks duration in Minutes:Seconds.Milliseconds and for the moment it drops.
It could be any moment in the track, anything remarkable that you want it to hit.

When calling the main function "play_track" you will have to pass the date that you want it to happen. For NYE's that's usually 01/01/YEAR.

It will default to midnight but you can also pass the time, here's a couple examples:

`play_track(track_length, drop_time, "01/01/2023")`

`play_track(track_length, drop_time, "02/03/2023", "00:12:12")`

# Note:
If it's not possible to reach the target time it will error out and exit.
For most things the script will ask you about minutes, seconds and milliseconds. You don't have to worry about inputting formats too perfectly for that.
Although for the date... I didn't make a function for that so just deal with having to define it as a parameter of play_track. Or submit a PR idk lmao.
