import os,shutil
from PIL import Image

def main():
    # img_dir="C:\Users\%username%\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets\""
    uname=os.environ['username']
    img_dir="C:/Users/{}/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/".format(uname)
    save_dir="C:/Users/{}/Pictures/Saved Pictures/".format(uname)
    hash_file="C:/Users/{}/Pictures/Saved Pictures/hash.txt".format(uname)
    
    hash_list=[]
    with open(hash_file,'r') as f:
        tmp=f.readlines()
        for i in tmp:
            hash_list.append(i.strip())

    size_type=[(1920, 1080),(1080, 1920),(44, 44)]

    f_list=[]
    for root,dirs,files in os.walk(img_dir):
        for f in files:
            if f in hash_list:
                continue
            fpath=os.path.join(root,f)
            image_obj=Image.open(fpath)
            if image_obj.size==(1920, 1080):
                f_list.append(f+'\n')
                shutil.copy(fpath,save_dir+f+".jpg")
    
    with open(hash_file,'a') as f:
        f.writelines(f_list)


if __name__ == "__main__":
    main()
