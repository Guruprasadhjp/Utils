# Author 		: Guruprasadh J P
# Date 	 		: Jan 4,2021
# Description 	: Python code to rename multiple files in a directory
# Version		: 1.0

  
# importing os module 
import os 
  
# Function to rename multiple files 
def rename(input_directorypath,output_directorypath): 
  
    for count, filename in enumerate(os.listdir(input_directorypath)): 
        
        #import pdb;pdb.set_trace()
        dst =output_directorypath + '\\' + "new_" + filename
        src =input_directorypath + '\\' + filename
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__':

    inputpath = r'C:\Projects\repos\DB\RF_data0\dat'
    outputpath = r'C:\Projects\repos\DB\RF_data0\dat1'
    
    rename(inputpath,outputpath)
    
    