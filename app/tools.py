import typer
import os

app = typer.Typer()

@app.command()
def install():

    directory = 'D:/Informatique/TesCliquesEtTesCloques/'
    venv_name = 'venv'
    os.makedirs(directory, exist_ok=True)
    venv_path = os.path.join(directory, venv_name)

    venv = f'python -m venv {venv_path}'
    pip = f'venv/lib/pip install -r requirements.txt'
    main = f'venv/lib/python main.py'

    print(f'You are running the install function')
    try:
        os.system(venv)
        activate_script = os.path.join(venv_path, 'Scripts', 'activate.bat')
        activate_command = f'call {activate_script}'
        os.system(activate_command)
    except OSError as error:
        print(error)

    os.system(pip)
    os.system(main)

@app.command()
def clean():
    print(f'You are running the clean function')
    try:
        os.rmdir('venv')
        print("Directory venv has been removed successfully")
    except OSError as error:
        print(error)
        print("Directory venv can not be removed")
        

if __name__ == "__main__":
    app()