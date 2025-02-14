# importing os module
import os 
def clear_clutter():
    # rename the specific file 
    os.rename("PNGfiles/github-recovery-codes.txt", "PNGfiles/1.txt")
    # list of files
    files= os.listdir("PNGfiles")
    i=1
    for file in files:
        # rename specific extension files 
        if file.endswith(".png"):
            print("___",file)
            os.rename(f"PNGfiles/{file}", f"PNGfiles/{i}.png")
            i=i+1
    
clear_clutter()
