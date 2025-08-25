import requests

class STEADFAST:
    def __init__(self, API_KEY, API_SECRET):
        self.API_URL = "https://portal.packzy.com/api/v1"
        self.HEADERS = {
            "Api-Key": API_KEY,
            "Secret-Key": API_SECRET,
            "Content-Type": "application/json"
        }
    

    def _sendGetReq(self, path, params=None):
        """:param params: `OPTIONAL`"""
        try:
            res = requests.get(f"{self.API_URL}/{path}", params=params, headers=self.HEADERS)
            return res.text
        except Exception as e:
            return str(e)
    

    def check_delivery_status(self, data):
        """
        :param data: `json` E.g. {"name": "ID"}\n
            **Available names:**\n
                'Consignment ID' - `status_by_cid`,\n
                'invoice ID' - `status_by_invoice`,\n
                'Tracking Code' - `status_by_trackingcode`
        """
        paths = ["status_by_cid", "status_by_invoice", "status_by_trackingcode"]
        path = ""
        path_id = ""
        for d in data:
            if d in paths:
                path = d
                path_id = data[d]
        
        return self._sendGetReq(f"{path}/{path_id}")
    

    def check_balance(self):
        return self._sendGetReq("get_balance")




API_KEY = ""
API_SECRET = ""

steadfast = STEADFAST(API_KEY, API_SECRET)



print(steadfast.check_balance())




