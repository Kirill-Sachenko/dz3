import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файл file_path на яндекс диск"""
        headers = {
            'Authorization': f'OAuth {self.token}'
        }

        # Получаем информацию о текущем пользователе
        response = requests.get('https://cloud-api.yandex.net/v1/disk/', headers=headers)
        if response.status_code == 200:
            user_info = response.json()
            disk_path = user_info['root']

            # Определяем имя файла из его пути
            file_name = file_path.split('/')[-1]

            # Формируем URL для загрузки файла
            upload_url = f'https://cloud-api.yandex.net/v1/disk/resources/upload?path={disk_path}/{file_name}&overwrite=true'

            # Загружаем файл
            with open(file_path, 'rb') as file:
                response = requests.put(upload_url, headers=headers, files={'file': file})

                if response.status_code == 202:
                    print(f"File '{file_name}' uploaded successfully.")
                else:
                    print(f"Failed to upload file '{file_name}'. Status code: {response.status_code}")
        else:
            print(f"Failed to get user info. Status code: {response.status_code}")

if __name__ == '__main__':

    token = 'YOUR_YANDEX_DISK_TOKEN'
    path_to_file = 'path/to/your/file.txt'

    uploader = YaUploader(token)
    uploader.upload(path_to_file)