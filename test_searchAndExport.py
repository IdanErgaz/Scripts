import logging
logging.basicConfig(filename="E:/TestFiles/test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s', #SET the row syntax
                    # level=logging.DEBUG,  #setting the logging with the lowest level of DEBUG
                    datefmt='%d/%m/%y %I:%M:%S %p' #set the date and time syntax
                    )


logger=logging.getLogger()
logger.setLevel(logging.DEBUG)


logFile = "E:\\TestFiles\\file1.txt"
resultsFile="E:\\TestFiles\\results.txt"
results=[]
#Open the file
infile = open(logFile, 'r')
logger.info("==========================================================================")
logger.info("Open the source file")
# print(f.read())
lines=infile.readlines()
strings=["GAME"]
logger.info("Searching for each STRING in strings list in each LINE")
for line in lines: #lines is a list with each item representing a line of the file
    for string in strings:
        if string.casefold() in line:#Using casefold() to disable the case sensitive!!!
            print(line)
            results.append(line)
            print(results)
infile.close() #close the file when you're done!

#creating a new file, copy the result to this file
resultsFile = open("E:\\TestFiles\\results.txt", "w")
resultsFile.write("These are the results:\n")
resultsFile.write("________________________\n")
resultsFile.writelines(results)
resultsFile.close()
