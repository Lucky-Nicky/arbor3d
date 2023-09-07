# -*- coding: utf-8 -*-
import time
import requests

def upload_file(file_path,cookies):
    for i in range(5):
        try:
            print(f"现在是第{i}次+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            file_path=file_path
            files = {
                'file': open(f"{file_path}", 'rb')
            }
            # with open("img/5.jpg","rb") as f:
            #     a=f.read()
            print('当前需要上传的file_path为：',file_path)
            file_name=file_path.split("/")[1]
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

            add_json={"tagList":[],"imgsrc":f"607/sourceimg/{img_uuid}.jpg","imgname":f"{img_uuid}.jpg","filename":f"{file_name}","folder_id":1509}

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

    cookies={'userName': '1', 'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d': 'eyJpdiI6IlBadmRGNldMWStCaUg4SmFUMEdKYUE9PSIsInZhbHVlIjoiWVhtaktSXC9RVExYaWk2dURRbk1TZFRsa0FKS2tadVpveVwveUpUSlF3RTI4RUtcL1ZLclRDQTg2YUVWKzk5MUxVNVwvMzg4UXN0dTUyYWowXC83MVZKc000SW1PQVN5VTVkeTB6c2Vta3hHZ05kMUxcL0kxakJnWk1MXC9KUXVEamhKYTFRNnd3NStwQVdvYUtjczFsZDFPeTQxSktEYVRLZUc1cVwvbjczXC9qd24wbXp3UW1LUVQwZVpIRXlXNXZOaE1vWEhBaUtidDVTd252elFtNUN3UnY5ZzJRY3hmZGhMNHhpbFl0OEM3SkdnQVZpST0iLCJtYWMiOiJmMjcxNzRkMGY3YzQ1NDVlNzg3Y2ZlZDA4NzM2NjAzYmY3MTdlNzA1Zjk0ZmFmYmIwMjgzYTNlNWNjN2JkZjVjIn0%3D', 'ADMIN-TOKEN': '2Zj7bumCn61BVZBcOzU8AVOKGXGaY9VGFasj3W0Do5IG44JnUS7sAcQ2AeVM', 'XSRF-TOKEN': 'eyJpdiI6InBQaHFXSnpGTDNiS2UrWFJZR2o2OVE9PSIsInZhbHVlIjoiQ2pFc0M2V0lIRDFtdGRMOFVvRlFqWFNQZUtFajBEYWlQc3hUTnA0enhUSlhvN1RKQyt4aHFHMjVcLzZiekV2R2RrVFJvRGRLNEt0NHo4UXpibEJEc01GRDBhQ1lESmZKTXFkYk5vTzlxcXFEdUdrNlRaYitpUW9qS2xIblwvdjlMOCIsIm1hYyI6IjEwZTY2MmUyNWIxNDBhYzQ5YmEzMGYzNTQ0NzFkOTVjOTBlYzhhMTU3MmE3MWZjYmJhODI1Y2YzNTdlN2IwMmUifQ%3D%3D', 'laravel_session': 'eyJpdiI6ImpHbllWSllFdWd0ZkZMNWVXXC9DVmpBPT0iLCJ2YWx1ZSI6Inpkd0oxcUdsK1lWZkdqXC8xbUJPVFJGdXZuVXNpVlBDZGZ3ZXRKeFd1VnFlVmFYYm0xRCthWlhDWll6QU1NV1wvWit3MVdUTFNCOHROXC9vcWgrR01YQkFMYk1yNjE5NGppM2NtSGpGOGFMOUlkV1YrdEd2WUVpdWR2d0dvdCtaME54IiwibWFjIjoiYTViNmI5ZmE5NTAyNzdjMzA4NWE5YzM4MzAzMGI3ZDlkYzI5NDM5NDAyOGFhMGUxNTM1Y2M5NTNkMGVmOTdjNCJ9'}
    file_paths = ["img/1.jpg", "img/2.jpg", "img/3.jpg", "img/4.jpg", "img/5.jpg","img/6.jpg", "img/7.jpg", "img/8.jpg", "img/9.jpg", "img/10.jpg"]
    num_threads=10
    #需要传入三个参数，第一个是页面上的cookies，第二个是需要轮流上传的图片，第三个是需要启动线程的数量
    threading_upload_file(num_threads, file_paths, cookies)