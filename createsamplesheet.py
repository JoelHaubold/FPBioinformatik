import os


#Get current dictonary
cwd = os.getcwd()

#Test dictonary
cwd = "/home/bouzia00/Bioinformatik/FPBioinformatik/FPBioinformatik/Tests/"

#Sampledict
cwd += "reads/"
files = [f for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]

#Create Dictonary for DataFrame
sdict = {"sample" : ["a","b"], "fq1" : [files[1],files[2]], "fq2" : [files[0],files[3]], "condition" : []}
print(sdict)


