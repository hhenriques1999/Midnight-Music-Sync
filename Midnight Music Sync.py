import datetime
import logging
import subprocess
import time


def get_time(purpose: str):
    print(f"Enter the {purpose}:")
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))
    milliseconds = int(input("Enter the number of milliseconds: "))
    time = minutes * 60 + seconds + milliseconds / 1000
    return time


def get_target_datetime(target_date: str, target_time: str = "00:00:00") -> datetime.datetime:
    """Parses the target date and time strings to create a datetime object."""
    return datetime.datetime.strptime(f"{target_date} {target_time}", "%d/%m/%Y %H:%M:%S")


def get_drop_timestamp(target_datetime: datetime.datetime, drop_time: float) -> float:
    """Calculates the timestamp for the target date and time, minus the drop time."""
    return (target_datetime - datetime.timedelta(seconds=drop_time)).timestamp()


def get_drop_datetime(drop_timestamp: float) -> datetime.datetime:
    """Converts the drop timestamp to a datetime object."""
    return datetime.datetime.fromtimestamp(drop_timestamp)


def wait_for_drop(drop_timestamp: float):
    """Runs a loop waiting for the drop timestamp to be reached."""
    while datetime.datetime.now().timestamp() < drop_timestamp:
        time.sleep(0.01)

def get_target_date() -> str:
    """Gets the target date for which day the music should drop at."""
    return input("Enter the desired target date in the following format: (DD/MM/YYYY): ")


def get_target_time() -> str:
    """Gets the target time for when the music should drop at."""
    return input("Enter the desired target time in the following format: HH:MM:SS: ")

def play_track(track_length: float, drop_time: float, target_date: str, target_time: str = "00:00:00"):
    # Configure logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    
    # Ask the user for the path to the track
    track_path = input("Enter the path to the track: ")
    
    # Get the target datetime, drop timestamp, and drop datetime
    target_datetime = get_target_datetime(target_date, target_time)
    drop_timestamp = get_drop_timestamp(target_datetime, drop_time)
    drop_datetime = get_drop_datetime(drop_timestamp)
    
    # Check if it is possible to reach the target date and time
    if datetime.datetime.now() + datetime.timedelta(seconds=drop_time) > target_datetime:
        logging.error("It is not possible to reach the target date and time")
        return
    
    logging.info(f"Track length: {track_length}")
    logging.info(f"Drop time: {drop_time}")
    logging.info(f"Target date: {target_date}")
    logging.info(f"Target time: {target_time}")
    logging.info(f"Drop timestamp and datetime: {drop_timestamp} => {drop_datetime}")
    
    # Wait for the drop timestamp to be reached
    wait_for_drop(drop_timestamp)
    logging.info("Drop timestamp reached")
    
    # Open the application and start playing the track
    subprocess.run([r"C:\Program Files\AIMP\AIMP.exe", track_path])


if __name__ == "__main__":
    track_length = get_time("track length")
    drop_time = get_time("drop time")
    target_date = get_target_date()
    target_time = get_target_time()
    play_track(track_length, drop_time, target_date, target_time)
