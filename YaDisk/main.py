import requests
from pprint import pprint
from access_token import ya_token as TOKEN


class YaDiskUploader:
    def __init__(self, token: str):
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/disk'

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_upload_link(self, disk_file_path, vk_url):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": disk_file_path, "url": vk_url}
        response = requests.get(upload_url, headers=headers, params=params)
        data = response.json()
        url = data.get('url')
        return url

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def create_folder(self, disk_file_path):
        upload_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {"path": disk_file_path}
        response = requests.put(upload_folder, headers=headers, params=params)
        response.raise_for_status()
        if response.status_code == 201:
            return "Success"


if __name__ == '__main__':
    ya = YaDiskUploader(token=TOKEN)
    disk_file_path = 'New_folder_for_tests_123'
    print(ya.create_folder(disk_file_path))
    pprint(ya.get_files_list())
