import click
import subprocess
import os
import json

PATH = "C:/output"
os.makedirs(PATH, exist_ok=True)

def clear_terminal():
    subprocess.run(["powershell", "-Command", 'cls'])

def download_file(url, filename):
    full_path = os.path.join(PATH, filename)  
    command = f'Invoke-WebRequest -Uri "{url}" -OutFile "{full_path}"'
    subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
    

@click.command()
def cli():
    with open('downloads.json', 'r') as file:
        data = json.load(file)
        downloads = data["downloads"]
        for item in downloads:
            clear_terminal()
            click.echo(f'\nIniciando download de {item['name']}...')
            download_file(item['url'], item['fileName'])
    
    clear_terminal()
    click.echo(f'\nDownloads finalizados!')    

        

if __name__ == "__main__":
    cli()


