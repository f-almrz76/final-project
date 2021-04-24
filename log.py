import logging

my_logger=logging.getLogger(__name__)
my_logger.setLevel(logging.INFO)
event_handler=logging.FileHandler('Event.log')
ticket_handler=logging.FileHandler('Ticket.log')
error_handler=logging.FileHandler('Error.log')
error_handler.setLevel(logging.INFO)
ticket_handler.setLevel(logging.INFO)
error_handler.setLevel(logging.WARNING)
log_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
event_handler.setFormatter(log_format)
ticket_handler.setFormatter(log_format)
error_handler.setFormatter(log_format)
my_logger.addHandler(event_handler)
my_logger.addHandler(ticket_handler)
my_logger.addHandler(error_handler)