from ftp.ftp_client import FTPClient
import base64

LOCAL_FILE_DIR = './testdir/'
LOCAL_FILE_NAME = 'test.pdf'

UPLOAD_TO_DIR = '/Users/zhenghan/Development/Python/file-transfer/testdir/upload/'
UPLOAD_FILE_NAME = 'uploaded.pdf'

DOWNLOAD_FROM_DIR = UPLOAD_TO_DIR
DOWNLOAD_FILE_NAME = UPLOAD_FILE_NAME

DOWNLOAD_FILE_SAVED_DIR = '/Users/zhenghan/Development/Python/file-transfer/testdir/download/'
DOWNLOAD_FILE_SAVED_NAME = 'download.pdf'


def test_upload():
    ftpClient = FTPClient()

    with open(LOCAL_FILE_DIR + LOCAL_FILE_NAME, 'rb') as f:
        remoteFileData = base64.b64encode(f.read())
        f.close()

        ftpClient.upload(UPLOAD_TO_DIR, UPLOAD_FILE_NAME, remoteFileData)

    ftpClient.close()


def test_download():
    ftpClient = FTPClient()

    remoteFileData = ftpClient.download(DOWNLOAD_FROM_DIR, DOWNLOAD_FILE_NAME)
    with open(DOWNLOAD_FILE_SAVED_DIR + DOWNLOAD_FILE_SAVED_NAME, 'wb') as f:
        f.write(base64.b64decode(remoteFileData))
        f.close()

    ftpClient.close()


if __name__ == '__main__':
    test_upload()
    test_download()
