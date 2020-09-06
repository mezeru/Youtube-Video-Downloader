from pytube import YouTube
import os

videofiles = []

if __name__=='__main__':
    print("Enter a link for the youtube Video to be downloaded : ",end="")
    link = input()

    try:
        youobj = YouTube(link)
        while not videofiles:
            print("Enter the resolution Needed (ex.720p) ",end="")
            user_res =  input()

            if(user_res[-1] != 'p'):
                user_res = user_res + 'p'

            videofiles = youobj.streams.filter(type="video",res=user_res,progressive="True")
            
            if not videofiles:
                print("\nVideo in this Resolution is not available for Download , Please select another resolution \n")
            
            else:
                print("\n")
                print("Title : ",youobj.title)
                print("Channel : ",youobj.author)
                print("Number of views: ",youobj.views)
                print("Length of video: ",youobj.length," seconds")
                print("Ratings: ",youobj.rating)
                
                down_dir = os.getcwd()+ "//Videos Downloaded//"             
                
                print("\nConfirm (Y/N) ?")
                userc = input()
                
                if (userc == 'y' or userc == 'Y'):
                    videofiles.last().download(down_dir)
                    print("Download Has Been Completed at the location ",os.getcwd())
                
                else:
                    print("Download Has Been Canceled")    
    except:
        print("Check Your Internet Connection or Check the Link and try Again")
    
       


    
    