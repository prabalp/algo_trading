# import httplib2
import os

from apiclient import discovery
from google.oauth2 import service_account

class gsheet_connect():
    def __init__(self, cred_loc, sheet_id):
        self.scopes = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/spreadsheets"]
        self.secret_file = os.path.join(os.getcwd(), cred_loc)
        self.sheet_id = sheet_id
        self.credentials = service_account.Credentials.from_service_account_file(self.secret_file, scopes=self.scopes)
        self.service = discovery.build('sheets', 'v4', credentials=self.credentials)
    def write(self, values, range_name):
        # data should be a array
        data = {
            'values' : values
        }
        self.service.spreadsheets().values().update(spreadsheetId=self.sheet_id, body=data, range=range_name, valueInputOption='USER_ENTERED').execute()
    def read(self, range_,value_render_option='', date_time_render_option='' ):
        # the range shoukd have some values
        request = self.service.spreadsheets().values().get(spreadsheetId=self.sheet_id, range=range_)
        response = request.execute()
        return response


if __name__ == '__main__':
    test = gsheet_connect('creds.json','1rZUkl8o04L-Qst2X-HMh1SoSpJ1xWnZclg2ZybKnH1I')
    test.write([[1,2,3]], 'Sheet1!A1:C1')
    print(test.read('Sheet1!B1')['values'][0][0])
    # response structure ----------------- {'range': 'Sheet1!A1:C1', 'majorDimension': 'ROWS', 'values': [['1', '2', '3']]}
    print('working fine')