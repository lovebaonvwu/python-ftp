from ftplib import FTP
import StringIO
import base64


class FTPClient:
    '''FTP Client

    constructor args:
        host: ftp server host, default 127.0.0.1
        user: ftp user name, default user
        password: ftp user password, default 12345
    '''

    def __init__(self, host='127.0.0.1', user='user', password='12345'):
        self.user = user
        self.password = password

        self.ftp = FTP(host)

        self.ftp.login(user, password)

    def upload(self, remoteDir, remoteFileName, remoteFileData):
        self.ftp.cwd(remoteDir)

        binaryStringIO = StringIO.StringIO(base64.b64decode(remoteFileData))
        self.ftp.storbinary('STOR ' + remoteFileName, binaryStringIO)

    def download(self, remoteDir, remoteFileName):
        self.ftp.cwd(remoteDir)

        binaryStringIO = StringIO.StringIO()
        self.ftp.retrbinary('RETR ' + remoteFileName,
                            binaryStringIO.write, 1024 * 10)

        return base64.b64encode(binaryStringIO.getvalue())

    def close(self):
        self.ftp.quit()
