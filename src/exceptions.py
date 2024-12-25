import sys
import logging

def error_msg_details(error,err_details:sys):
    _, _, exc_tb = err_details.exc_info()
    err_msg ="Error occured [{0}] line number [{1}] error message [{2}]".format(exc_tb.tb_frame.f_code.co_filename, exc_tb.tb_lineno, str(error))
    return err_msg
    

class CustomException(Exception):
    def __init__(self, err_msg, err_details:sys):
        super().__init__(err_msg)
        self.err_msg = error_msg_details(err_msg,err_details=err_details)

    def __str__(self):
        return self.err_msg
