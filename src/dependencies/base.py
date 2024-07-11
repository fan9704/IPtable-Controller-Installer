import subprocess
import platform

from rich import print

def check_installation():
    # 確認作業系統
    os_type = platform.system().lower()

    # 定義安裝命令
    install_commands = {
        'windows': ['powershell', '-Command', 'Install-Module -Name DockerMsftProvider -Repository PSGallery -Force'],
        'linux': ['sudo', 'apt-get', 'install', '-y', 'docker.io', 'docker-compose'],
        'darwin': ['brew', 'install', 'docker', 'docker-compose']
    }

    # 檢查 Docker 和 Docker Compose 是否已經安裝
    try:
        subprocess.run(['docker', 'version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print("[blue]Docker 已經安裝.[/blue]")
    except subprocess.CalledProcessError:
        print("[blue]Docker 沒有安裝.[/blue]")
        if os_type in install_commands['linux']:
            subprocess.run(install_commands['linux'])
        elif os_type in install_commands['darwin']:
            subprocess.run(install_commands['darwin'])

    try:
        subprocess.run(['docker-compose', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print("[blue]Docker Compose 已經安裝.[/blue]")
    except subprocess.CalledProcessError:
        print("[blue]Docker Compose 沒有安裝.[/blue]")
        if os_type in install_commands['linux']:
            subprocess.run(install_commands['linux'])
        elif os_type in install_commands['darwin']:
            subprocess.run(install_commands['darwin'])

if __name__ == '__main__':
    check_installation()