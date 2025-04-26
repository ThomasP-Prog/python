"""Write a function analyze_sensor_data(timestamps, readings, locations) that takes three lists: 
   timestamps (e.g., strings like "10:00", "10:05"), readings (e.g., floats like 22.5, 23.1), 
   and locations (e.g., strings like "Lab A", "Lab B"). The lists might not be the same length. 
   Use zip to process them together (remembering it stops at the shortest list). Use enumerate to 
   assign a sequential event ID (starting from 1) to each correlated entry. The function should return 
   a list of tuples. Each tuple should contain (event_id, timestamp, reading, location) but only for 
   readings that are greater than a threshold (e.g., 23.0). 
   Add a check at the beginning: if the lists are not the same length, print a warning message (but still proceed with zip).

   Concepts Reinforced: enumerate, zip, lists, tuples, functions, returning a list of tuples, conditional logic (if), 
   basic comparison, handling potentially unequal list lengths (awareness of zip's behavior), printing warnings."""

def analyze_sensor_data(timestamps : list[str], readings : list[float], locations : list[str],threshold : float) -> list[tuple[int,str,float,str]]:
    """Return list of tuple with temps > threshold"""
    if not timestamps or not readings or not locations or threshold == None:
        return []
    if len(set(map(len, [timestamps, readings, locations]))) > 1:
        print("Warning lists of different size")
    
    sensor_data = [(index,time,read,loc) for index,(time,read,loc) in enumerate(zip(timestamps,readings,locations),start=1) if read > threshold]
    return sensor_data

def main() -> None:
    """main function"""
    times = ["10:00", "10:05", "10:10", "10:15"]
    temps = [22.5, 23.1, 23.5, 22.9]
    sites = ["Lab A", "Lab B", "Lab A"] # Shorter than others
    threshold = 23.0
    # Expected Output (Note: zip stops after 3 entries due to 'sites'):
    # Warning: Input lists have different lengths. Processing up to the shortest list (length 3).
    # [(2, '10:05', 23.1, 'Lab B'), (3, '10:10', 23.5, 'Lab A')]
    sensor_data = analyze_sensor_data(times,temps,sites,threshold)
    print(sensor_data)

if __name__ == "__main__":
    main()