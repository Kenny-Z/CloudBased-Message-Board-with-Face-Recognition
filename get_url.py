import requests
import json
from send_mms import SendMsg

BASE_PATH = 'https://sm.ms/api/v2/'
testmsg = SendMsg()


class SMMS:
    def __init__(self, username, password):
        self.login_success = False
        self.api_key = None
        self.username = username
        self.password = password

    def upload_image(self, file_path):
        """
        图片上传
        :param file_path:
        :return:
        """
        headers = {}
        if self.login_success:
            headers['Authorization'] = 'WLFP6suzJEMEzEe6nwxBbEMWbQ3nOGHx'
        return self.__post(url='upload', headers=headers, files={'smfile': open(file_path, 'rb+')})

    @staticmethod
    def __post(url, data=None, headers=None, files=None):
        SMMS.__req('POST', url, data=data, headers=headers, files=files)

    @staticmethod
    def __req(method, url, data=None, params=None, headers=None, files=None):
        """
        SMMS基础POST请求函数
        :param url: 请求地址
        :param data: 请求发送的数据
        :param headers: 请求头设置
        """
        post = requests.request(method=method,
                                url=f'{BASE_PATH}{url}',
                                params=params,
                                data=data,
                                headers=headers,
                                files=files)
        if post.status_code == 200:
            result = json.loads(post.content.decode(encoding='utf-8'))
            # print(result)
            if result['success']:
                print('face picture ', result['message'])
                print('url is :', result['data']['url'])
                im_url = result['data']['url']
                testmsg.knocksend('Waiting guest for you!', im_url)
            else:
                print(result['message'])
            return result
        return {'success': False}


# if __name__ == '__main__':
#     smms = SMMS('Huey', 'ahgyzhy168')
#     smms.upload_image(r'C://Users//takumi//Pictures//picture//图片//8DF2428B49465803E7363E162E46BC7F.jpg')
    # im_url = results['data']['url']
    # print(im_url)
