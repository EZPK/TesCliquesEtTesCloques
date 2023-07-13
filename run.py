import subprocess
import sys
import os
import shutil
import logging

directory = 'D:\Informatique\TesCliquesEtTesCloques'
venv_name = 'venv'
venv_path = os.path.join(directory, venv_name)

devnull = open(os.devnull, 'w')


def main():   
    if len(sys.argv) < 2:
        print("Veuillez spécifier le nom d'une fonction à appeler.")
        sys.exit(1)

    function_name = sys.argv[1]

    if function_name == 'install':
        install_venv()
    elif function_name == 'clean':
        cleanvenv(directory, venv_name)
    elif function_name == 'lib':
        lib()
    else:
        print(f"La fonction '{function_name}' n'existe pas.")

def install_venv():
    # Install venv
    try:
        os.makedirs(directory, exist_ok=True)
        subprocess.check_call([sys.executable, '-m', 'venv', venv_path],stdout=devnull, stderr=devnull)
        print(f"L'environnement virtuel '{venv_name}' a été installé avec succès au path {venv_path}.")
        print(f"Activez le avec: > .\\venv\\Script\\activate")

        # if is_venv_active():
        #     print('Venv est déjà actif')
        # else:
        #     activate_script = os.path.join(venv_path, 'Scripts', 'activate.bat')
        #     # subprocess.check_call(activate_script, shell=True, stdout=devnull, stderr=devnull)
        #     subprocess.check_call(activate_script, shell=True)
        #     print(f"L'environnement virtuel '{venv_name}' a été activé avec succès.")

        # requirements_file = directory + '/requirements.txt'
        # subprocess.check_call([os.path.join(venv_path, 'Scripts', 'pip'), 'install', '-r', requirements_file], stdout=devnull, stderr=devnull)
        # print(f"L'environnement virtuel '{venv_name}' a installé les librairies")

    except OSError as error:
        print(error)

def lib():
    # Install lib from requirements.txt
    if is_venv_active():
        try:
            requirements_file = directory + '/requirements.txt'
            subprocess.check_call([os.path.join(venv_path, 'Scripts', 'pip'), 'install', '-r', requirements_file], stdout=devnull, stderr=devnull)
            print(f"L'environnement virtuel '{venv_name}' a installé les librairies")
        except OSError as error:
            print(error)
    else:
        print(f'Activez venv: venv/Scripts/activate')

def cleanvenv(directory, venv_name):
    # Remove venv
    if is_venv_active():
       print('Il faut désactiver le venv: deactivate')
    else:
        try:
            venv_path = os.path.join(directory, venv_name)
            if sys.platform.startswith('win'):  # Windows
                deactivate_command = os.path.join(venv_path, 'Scripts', 'deactivate.bat')
            try:
                subprocess.check_output(deactivate_command, shell=True, stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError as e:
                print(f"Une erreur s'est produite lors de la désactivation de l'environnement virtuel : {e.output.decode()}")
            shutil.rmtree(venv_path)

            print(f"L'environnement virtuel '{venv_name}' a été supprimé avec succès.")
        except OSError as error:
            print(error)



def stop(venv_path):
    try:
        subprocess.check_call(os.path.join(venv_path, 'Scripts', 'deactivate.bat'), stdout=devnull, stderr=devnull)
        print(f"L'environnement virtuel '{venv_name}' a été désactivé avec succès.")

    except OSError as error:
        print(error)

def is_venv_active():
    return 'VIRTUAL_ENV' in os.environ


if __name__ == '__main__':
    main()