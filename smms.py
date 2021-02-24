import json
import requests

BASE_PATH = 'https://sm.ms/api/v2/'


class SMMS:
    def __init__(self, username, password):
        self.login_success = False
        self.api_key = None
        self.username = username
        self.password = password

    def login(self):
        """
        登录SMMS username,password
        :return:
        """
        result = self.__post('token', data={'username': self.username, 'password': self.password})
        self.login_success = True  # result['success']
        if self.login_success:
            self.api_key = result['data']['token']
        return self.login_success

    def upload_image(self, file_path):
        """
        图片上传
        :param file_path:
        :return:
        """
        headers = {}
        if self.login_success:
            headers['Authorization'] = self.api_key
        return self.__post(url='upload', headers=headers, files={'smfile': open(file_path, 'rb+')})

    def upload_image_2markdown(self, file_path):
        result = self.upload_image(file_path)
        if result['success']:
            data = result['data']
            return '![%s](%s)' % (data['filename'], data['url'])
        else:
            result['message']
        return result

    def upload_history(self):
        if format != 'xml' and format == 'json':
            Exception('输出格式错误！可选值有 json、xml')
        if self.login_success:
            Exception('请先登录！')
        return self.__get('history', headers={
            'Content-Type': 'multipart/form-data',
            'Authorization': self.api_key
        })

    @staticmethod
    def __post(url, data=None, headers=None, files=None):
        SMMS.__req('POST', url, data=data, headers=headers, files=files)

    @staticmethod
    def __get(url, params=None, headers=None, files=None):
        SMMS.__req('GET', url, params=params, headers=headers, files=files)

    @staticmethod
    def __req(method, url, data=None, params=None, headers=None, files=None):
        """
        SMMS基础POST请求函数
        :param url: 请求地址
        :param data: 请求发送的数据
        :param headers: 请求头设置
        :return:
        """
        post = requests.request(method=method, url=f'{BASE_PATH}{url}', params=params, data=data, headers=headers,
                                files=files)
        if post.status_code == 200:
            result = json.loads(post.content.decode(encoding='utf-8'))
            print(result)
            if result['success']:
                print(result['message'])
            else:
                print(result['message'])
            return result
        return {'success': False}


if __name__ == '__main__':
    smms = SMMS('Huey', 'ahgyzhy168')
    smms.login()
    print(smms.upload_image_2markdown(r'E:\\files\\Python\\MessageBoard\\111.jpeg'))
    print(smms.upload_history())
