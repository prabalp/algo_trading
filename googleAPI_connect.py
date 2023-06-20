import os

from apiclient import discovery
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload


class googleAPI_connect:
    def __init__(self, cred_loc) -> None:
        self.scopes = [
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/spreadsheets",
        ]
        self.secret_file = os.path.join(os.getcwd(), cred_loc)
        self.credentials = service_account.Credentials.from_service_account_file(
            self.secret_file, scopes=self.scopes
        )

    def drive_connect(self) -> None:
        self.service = discovery.build("drive", "v3", credentials=self.credentials)

    def upoload_file(self, file_name, folder_id) -> None:
        mime_type = "application/octet-stream"
        file_metadata = {
            "name": file_name,
            "parents": [folder_id],
        }
        media = MediaFileUpload(file_name, mimetype=mime_type)
        file_data = (
            self.service.files().create(body=file_metadata, media_body=media).execute()
        )  # make a loader for this file upload which will give me how much file is uploaded
        print(f"{file_name} uploaded with file id as {file_data['id']}")


if __name__ == "__main__":
    test = googleAPI_connect("creds.json")
    test.drive_connect()
    test.upoload_file("test.db", "1jyAyepmvvbRv8YXRkisEisEL1rbWYay5")
