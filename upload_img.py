# -*- coding: utf-8 -*-
import time
import requests

def upload_file(file_path,cookies):
    for i in range(400):
        try:
            print(f"现在是第{i}次+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            file_path=file_path
            files = {
                'file': open(f"{file_path}", 'rb')
            }
            # with open("img/5.jpg","rb") as f:
            #     a=f.read()
            print('当前需要上传的file_path为：',file_path)
            set_up_url="https://119.45.117.181:4321/api/set_up_url"
            set_up_headers = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
            }

            set_up_res=requests.post(url=set_up_url,headers=set_up_headers,cookies=cookies,verify=False)

            print(set_up_res.json())

            upload_url="https://119.45.117.181:4321/api/upload_file"


            file_route = '607/sourceimg'  # 文件的路由
            # 将文件流作为二进制数据传递给接口

            # 发起上传请求
            response = requests.post(url=upload_url,headers=set_up_headers, files=files,cookies=cookies, data={'route': file_route},verify=False).json()

            # 打印响应结果
            print(response)

            img_uuid=response['data']['view_uuid']
            print(img_uuid)
            add_img_url="https://119.45.117.181:4321/api/add_imgs_main"

            add_json={"tagList":[],"imgsrc":f"607/sourceimg/{img_uuid}.jpg","imgname":f"{img_uuid}.jpg","filename":"5.jpg","folder_id":1062}

            add_res=requests.post(url=add_img_url,json=add_json,headers=set_up_headers, cookies=cookies,verify=False).json()
            print(f"现在是第{i}次+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        except Exception as e:
            print(f"这里报错了，错误信息为{e}")

if __name__ == '__main__':

    def threading_upload_file(num_threads,file_paths,cookies):
        import threading

        threads = []
        for i in range(num_threads):
            file_path = file_paths[i % len(file_paths)]
            thread = threading.Thread(target=upload_file, args=(file_path,cookies))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    cookies={}
    file_paths = ["img/1.jpg", "img/2.jpg", "img/3.jpg", "img/4.jpg", "img/5.jpg"]
    num_threads=10
    #需要传入三个参数，第一个是页面上的cookies，第二个是需要轮流上传的图片，第三个是需要启动线程的数量
    threading_upload_file(num_threads, file_paths, cookies)