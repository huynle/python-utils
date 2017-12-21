
class FormatString(object):
    @staticmethod
    def time():
        import datetime
        import time
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d__%H_%M_%S')
        return st
