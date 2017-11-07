import requests
from requests.exceptions import RequestException

def download_image(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print('get')
    except RequestException:
        print('请求图片出错',url)
        return None

if __name__ == '__main__':
    download_image('//p3.pstatp.com/origin/3c7c0001ed84f784045c')
    download_image('http://p3.pstatp.com/origin/3c7c0001ed84f784045c')

