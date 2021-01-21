# my_module.py, available in your sys.path
import luigi
import datetime

class MyTask(luigi.Task):
#    x = luigi.IntParameter()
#    y = luigi.IntParameter(default=45)

    def run(self):
        print(datetime.datetime.now())
#        print(self.x + self.y)
