import sys

def error_message_detail(error,error_detail:sys): #Parameter type hint
    _,_,exc_tb = error_detail.exc_info() # The map showing where the error happened
    file_name = exc_tb.tb_frame.f_code.co_filename # main object >> snapshot when crashed >> find code object >> find the filename
    error_mesagge = "Error ocurred in python script name [{0}] line number [{1}] error mesagge".format(file_name,exc_tb.tb_lineno,str(error))
    
    return error_mesagge


class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_mesagge