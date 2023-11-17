import os 
import shutil as st

#Les extentions:--------------------------------------------------

Texte=["txt","pdf","docx","doc","rtf","html","csv"]
Image=["png","jpg","gif","bmp","tiff","svg"]
Video=["mp4","avi","mkv","mov","wmv","flv"]
Fichier_executable=["exe","app","sh","bat","jar","msi"]

Type_Extention={"Textes":Texte,"Images":Image,"Videos":Video,"Fichier_executable":Fichier_executable}

#Function :--------------------------------------------------

def Create_Folders(path,name_folder):
    path=path+"/"+name_folder
    os.mkdir(path+"/")
    PathFolder_Ext={}
    for Type,ext in Type_Extention.items():
        os.mkdir(path+"/"+Type+"/")
        PathFolder_Ext[path+"/"+Type+"/"]=ext
    os.mkdir(path+"/Others/")
    PathFolder_Ext[path+"/Others/"]=[]
    return PathFolder_Ext

#Main_function:----------------------------------------------------

def Organise_Copy_Folder(path_folder,path_create_folders,name_folder):
    file_name_ext=os.listdir(path_folder)
    if file_name_ext==[]:
        print("There is no file in this folder")
    else:
        PathFold_Ext=Create_Folders(path_create_folders,name_folder)
        for file in file_name_ext:
            ext=file.split(".")[-1]
            for Path,Ext in PathFold_Ext.items():
                if ext in Ext:
                    st.copy(path_folder+"/"+file,Path)
                    break
                if Ext==[]:
                    st.copy(path_folder+"/"+file,Path)

#--------------------------------------------------------------------

def Organise_Nocopy(path_folder,path_create_folders,name_folder):
    file_name_ext=os.listdir(path_folder)
    if file_name_ext==[]:
        print("There is no file in this folder")
    else:
        PathFold_Ext=Create_Folders(path_create_folders,name_folder)
        for file in file_name_ext:
            ext=file.split(".")[-1]
            for Path,Ext in PathFold_Ext.items():
                if ext in Ext:
                    st.move(path_folder+"/"+file,Path+file)
                    break
                if Ext==[]:
                    st.move(path_folder+"/"+file,Path+file)
