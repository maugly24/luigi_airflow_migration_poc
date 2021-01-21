import luigi
from glob import glob
import os
import gzip
import shutil
from subprocess import check_output
raw_zips = '*.gz'

class WC(luigi.Task):
    document_id = luigi.Parameter()

    def requires(self):
        return ExtractGZ(self.document_id)

    def output(self):
        return luigi.LocalTarget(self.document_id+'.count')

    def run(self):
        with self.input().open('r') as f_in, open(self.document_id+'.count', 'w') as f_out:
            print(len(f_in.read().splitlines()), file=f_out)

class ExtractGZ(luigi.Task):
    document_id = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(self.document_id+'.txt')

    def run(self):
        with gzip.open(self.document_id) as f_in, open(self.document_id+'.txt', 'bw') as f_out:
            shutil.copyfileobj(f_in, f_out)
        print(os.path.dirname(self.document_id))

class TestTask(luigi.WrapperTask):
    def requires(self):
        for fname in glob(raw_zips):
            #print fname
            yield WC(fname)

