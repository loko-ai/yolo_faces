import logging

# Root logger: console logger
format_str = "%(asctime)s - %(name)s - %(threadName)s - %(levelname)s - %(message)s"
log_formatter = logging.Formatter(format_str, datefmt="%y-%m-%d %H:%M:%S")
root_logger = logging.getLogger()  # root logger
root_logger.setLevel(logging.DEBUG)

# Add console logger to root logger
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
root_logger.addHandler(console_handler)
