#include <iostream>
#include <vector>
#include <io.h>
using namespace std;

void getFiles( string path, vector<string>& files, bool find_sub=false)
{
    //文件句柄
    long hFile = 0;
    //文件信息
    struct _finddata_t fileinfo;
    string p = path + "\\*";
    // if((hFile = _findfirst(p.assign(path).append("\\*").c_str(),&fileinfo)) !=  -1)
    if((hFile = _findfirst(p.c_str(),&fileinfo)) !=  -1)
    {
        do
        {
            if((fileinfo.attrib & _A_SUBDIR))
            {
                if(strcmp(fileinfo.name,".") != 0  &&  strcmp(fileinfo.name,"..") != 0 && find_sub)
                    getFiles( p.assign(path).append("\\").append(fileinfo.name), files );
            }
            else
            {
                files.push_back(p.assign(path).append("\\").append(fileinfo.name) );
            }
        }while(_findnext(hFile, &fileinfo)  == 0);
        _findclose(hFile);
    }
}

int main()
{
    
    auto filePath = "D:\\Work\\ECA\\NDVI_mask";
    cout << "请输入路径：";
    // cin >> filePath;
    vector<string> files;
     
    // 获取该路径下的所有文件
    getFiles(filePath, files );
    int size = files.size();
    for (int i = 0;i < size;i++)
    {
        cout<<files[i].c_str()<<endl;
    }
    return 0;
}

