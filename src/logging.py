class OLogger(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        logPath = "C:\\Users\\egikmnq\\Aadhi\\workspace\\pyArm.log"
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.FileHandler(logPath),
                logging.StreamHandler(sys.stdout)
                ]
            )
        self.log = logging
        
    def getLogger(self):
        return self.log
