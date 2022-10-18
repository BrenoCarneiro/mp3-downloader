print("Inicializando...")
try:
    from tqdm import tqdm
    from pytube import YouTube
    import moviepy.editor as mp
    import re
    import os
    import subprocess
    import sys
    from art import *
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'tqdm'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pytube'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'moviepy']) 
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'art']) 
finally:
    from tqdm import tqdm
    from pytube import YouTube
    import moviepy.editor as mp
    from art import *
tprint('Youtube \n MP3 \n Downloader')
menu = '1'
while menu == '1':
    link = input("\nCole o link do vídeo que deseja baixar: \n-> ")
    if 'youtube' in link or 'youtu' in link:
        yt = YouTube(link)
        option = '1'
        while option != '1' or option != '2' or option != '3':
            option = input("\nOnde quer salvar o arquivo?\nEscolha uma opção abaixo: \n  1 - Salvar o áudio na pasta atual.\n  2 - Criar uma nova pasta ao lado desse arquivo. \n  3 - Informar o diretório completo manualmente.\n->")
            match option:
                case '1':
                    path = os.path.dirname(os.path.abspath(__file__))
                    break
                case '2':
                    path = input("\nDigite o nome da pasta que deseja criar (apenas letras e números):\n->")
                    break
                case '3':
                    path = input("\nInforme o diretório completo que deseja salvar o vídeo:\n->")
                    break               
                case default:
                    print("\nOpção Inválida. Favor informar uma opção válida.")             
        try:
            ys = yt.streams.filter(only_audio=True).first().download(path)
        except:
            if option == '1':
                option = input("\nNão foi possível baixar o arquivo.\nVerifique a sua conexão com a internet ou o link informado.\nDeseja tentar novamente?\n  1 - Sim\n  2 - Não \n->")
            else:
                option = input("\nNão foi possível baixar o arquivo.\nPossíveis erros: sem conexão com internet, link ou diretório inválido.\nDeseja tentar novamente?\n  1 - Sim\n  2 - Não \n->")
        finally:
            for i in tqdm(range(10)):
                for file in os.listdir(path):
                    if re.search('mp4', file):
                        mp4_path = mp4_path = os.path.join(path, file)
                        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
                        new_file = mp.AudioFileClip(mp4_path)
                        new_file.write_audiofile(mp3_path)
                        os.remove(mp4_path)
            print("\nDownload Concluído!")
        menu = input("Deseja baixar outro arquivo?\n  1 - Sim\n  2 - Não \n->")
        while menu != '1' and menu != '2':
            menu = input("\nEscolha uma opção válida:\n  1 - Baixar outro arquivo\n  2 - Sair \n->")         
    else:
        menu = input("\nLink inválido. Esse aplicativo só é compatível com vídeos do YouTube.\nDeseja tentar com outro link?\n  1 - SIM\n  2 - NÃO \n->")