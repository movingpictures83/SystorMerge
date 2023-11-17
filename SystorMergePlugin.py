import sys
import time
import os
import pandas as pd
import numpy as np
import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
import calendar
from datetime import datetime, timedelta, tzinfo
from calendar import timegm


class SystorMergePlugin:
 def input(self, inputfile):
     self.input_dir_name = inputfile
 def run(self):
     pass
 def output(self, outputfile):
  # filename = str(sys.argv[1])
  output_dir_name = outputfile
  folders =  os.listdir(self.input_dir_name)
  

  for folder in folders:
      
      folder_location = self.input_dir_name +folder+"/"
      if os.path.isdir( folder_location ):
        print(folder_location)
        filenames =  os.listdir(folder_location )
        for filename in filenames:
            file_location = folder_location + filename
            if os.path.isfile(file_location):
                fileName,fileExtension = os.path.splitext(file_location)
                if fileExtension==".csv" :

                    # print("********",filename, "****************")
                    name = filename.split(".")[0] 
                    date = name.split("-")[0][:-2] 
                    disk_name = name.split("-")[-1] 
                    print(date,disk_name)
                    # df = pd.read_csv(file_location)
                    with open(self.input_dir_name +"converted"+"_"+disk_name+'.csv', 'w') as outfile:
                        
                            for line in open( file_location, 'r' ):
                                # print(line)
                                outfile.write( line )
       

      
