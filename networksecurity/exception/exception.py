import sys
from networksecurity.logging import logger

def NetworkSecurityException(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() ## this variable will have the error details like in which file the error has occured ,error line number
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message='Error occurred in the python script name [{0}] line number [{1}] error message [{2}]'.format(file_name,exc_tb.tb_lineno,str(error))
    
    return error_message
    


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=NetworkSecurityException(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
if __name__=='__main__':
    try:
        logger.logging.info('enter the try block')
        a=1/0
        print('this will not be printed',a)
    except Exception as e:
        raise CustomException(e,sys)
