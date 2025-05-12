"""
Define a class Logger.

    Add a class variable log_level = "INFO" (string).
    Add a class variable instance_count = 0 (integer).
    Its __init__ should increment Logger.instance_count. It should also take an optional filename (string) 
    for this specific logger instance, storing it as self.filename. If no filename is provided, self.filename should be None.
    Add a method log(message: str) that prints a log message formatted as: "[LEVEL] (Filename: [filename_or_default]): Message". 
    For [LEVEL], use the Logger.log_level. If self.filename is None, print "Console" instead of the filename.

Sample Usage: Create two Logger instances, one with a filename, one without. Log a message with each. 
Print Logger.instance_count. Change Logger.log_level to "DEBUG" and log another message with one of the instances.
"""

class Logger:
    log_level: str = "INFO"
    instance_count:int = 0

    def __init__(self, filename:str = None) -> None:
        """Initialize logger"""
        Logger.instance_count += 1
        self.filename = filename

    def log(self,message:str) -> None:
        """print the formatted log message"""
        if self.filename is None:
            print(f"{Logger.log_level} (Console): {message}")
        else:
            print(f"{Logger.log_level} ({self.filename}): {message}")

def main() -> None:
    """main function"""
    logger1 = Logger("Admin")
    logger2 = Logger()
    logger1.log("Hello")
    logger2.log("World")
    print(f"Logger count : {Logger.instance_count}")
    Logger.log_level = "DEBUG"
    logger1.log("debug log")

if __name__ == "__main__":
    main()