import requests
import hashlib
import subprocess
import os
def main():

    # Get the expected SHA-256 hash value of the VLC installer
    expected_sha256 = get_expected_sha256()

    # Download (but don't save) the VLC installer from the VLC website
    installer_data = download_installer()

    # Verify the integrity of the downloaded VLC installer by comparing the
    # expected and computed SHA-256 hash values
    if installer_ok(installer_data, expected_sha256):

        # Save the downloaded VLC installer to disk
        installer_path = save_installer(installer_data)

        # Silently run the VLC installer
        run_installer(installer_path)

        # Delete the VLC installer from disk
        delete_installer(installer_path)

def get_expected_sha256():

    sha256_url='http://download.videolan.org/pub/videolan/vlc/3.0.18/win64/'

    get_request=requests.get(sha256_url)
    return 

def download_installer():
    installer_url='http://download.videolan.org/pub/videolan/vlc/3.0.18/win64/'
    get_request=requests.get(installer_url)
    if get_request.status_code == requests.codes.ok:

        return

def installer_ok(installer_data, expected_sha256):
    installer_hash=hashlib.sha256().hexdigest()
    if expected_sha256==hashlib.sha256(installer_data):
        return True
    else:
        return False

    

def save_installer(installer_data):
    path= "C:\Users\SIR\Documents\COMP593-Lab06"
    with open(path,'wb') as f:
        f.write(installer_data)
    return

def run_installer(installer_path):
    subprocess.run(installer_path,'/S')

    return installer_path
    
def delete_installer(installer_path):
    os.remove(installer_path)
    return

if __name__ == '__main__':
    main()