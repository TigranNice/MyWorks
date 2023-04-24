import requests
import pandas


class Client:

    def __init__(self, client_id, api_key):
        self.client_id = client_id
        self.api_key = api_key
        self.headers = {'Client-Id': str(self.client_id), 'Api-Key': self.api_key}
        self.headers2 = {'Client-Id': '12171', 'Api-Key': '437a1947-ee34-4595-8042-1f6ec883464e'}

        self.path_ozon = None
        self.path_1c = None
        self.path_exception = None
        self.product_ozon = None
        self.product_1c = None
        self.product_exception = None

    def set_path_ozon(self, path):
        self.path_ozon = path

    def set_path_1c(self, path):
        self.path_1c = path

    def set_path_exception(self, path):
        self.path_exception = path

    def connect(self):
        response = requests.post('https://api-seller.ozon.ru/', headers=self.headers2)
        return response

    def ozon_file_to_list(self):
        self.product_ozon = pandas.read_csv(self.path_ozon, sep=';')

    def c1_file_to_list(self):
        self.product_1c = pandas.read_excel(self.path_1c)

    # write
    def exception_file_to_list(self):
        self.product_exception = []

    def start_work(self):
        pass

    def get_items_from_ozon(self):
        response = requests.post('https://api-seller.ozon.ru/v2/product/info/list', headers=self.headers2,
                                 json={"offer_id": [],
                                       "product_id": self.product_ozon['Ozon Product ID'],
                                       "sku": []
                                       })
        items = response.json()['result']['items']
        sorted(items, key=lambda x: x['offer_id'])
        return items