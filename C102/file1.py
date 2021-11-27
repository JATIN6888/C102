    import dropbox
    import time
    import random
    import cv2

    starttime=time.time()
    def snapshot():
        number=random.randint(0,100)
        videocap=cv2.VideoCapture(0)
        result=true
        while(result):
            ret,frame=videocap.read()
            imgname="img" + str(number)+".png"
            cv2.imwrite(imgname,frame)
            starttime=time.time
            result=False
        return imgname
        print("snapshot tecan") 
        videocap.release()
        cv2.destroyAllWindows()



    
    def fileupload(imgname):
        accesstocan="sl.A83SiC-iyZhjqeVcL_ac6pveNUyQMb2UUtA4U9x_EBcu9stVEZAHRuJNZ8hEf_IaOS1NjGUI8rNYPRm9zdYM2kbztv5JHD-YiPTUlKYf9GQSCyGryl5fdmc4PlRQZVbBuyoqsZE"           
        file=imgname
        fromfile=file
        tofile="/testfolder/"+(imgname)
        db=dropbox.Dropbox(accesstocan)

    with open(fromfile,'rb') as f:
        db.files_upload(f.read(), tofile,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")
       

    def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = snapshot()
            fileupload(name)

main()
      


    