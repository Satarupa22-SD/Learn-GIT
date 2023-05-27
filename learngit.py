import subprocess
import requests


def execute_command(command):
    try:
        result = subprocess.check_output(command.split(), stderr=subprocess.STDOUT)
        return result.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')


# list of git commands
def explain_git_command(command):
    explanations = {
        'init': 'Creates an empty Git repository or reinitialize an existing one.',
        'add': 'Adds file contents to the index (staging area) for commit.',
        'commit': 'Records changes to the repository with a commit message.',
        'log': 'Shows commit logs.',
        'config': 'Sets the author name and email address to be used with your commits.',
        'clone': 'Used to make a copy of a repository from an existing URL,can create local copy of the repository.',
        'status': 'Displays the state of the working directory and the staging area.',
        'push': 'Uploads local repository content to a remote repository',
        'pull': 'Receives data from GitHub. It fetches and merges changes on the remote server to your working '
                'directory',
        'branch': ' Lists all the branches available in the repository.',
        'merge': " Merges the specified branch's history into the current branch.",
        'remote': "Connects local repository to the remote server. Allows user's to create, view, and delete "
                  "connections to other repositories ",
    }
    # exit condition
    if command in explanations:
        return explanations[command]
    else:
        return "I'm sorry, I don't have an explanation for that Git command."


# default url
URL = 'https://education.github.com/git-cheat-sheet-education.pdf'


# function to download the default file
def download_pdf(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        return True
    else:
        return False


# exit condition 
def process_input(user_input):
    if user_input.lower() == 'exit':
        return False
    # prints list of git commands when user selects 'learn'
    if user_input.lower() == 'learn':
        print("Available Git commands:")
        print("- init")
        print("- add")
        print("- commit")
        print("- log")
        print("- config")
        print("- clone")
        print("- status")
        print("- push")
        print("- pull")
        print("- branch")
        print("- merge")
        print("- remote")
        print(" Enter command as git <command> ")
        return True
    # provides resource downloading option when user selects 'resource'
    if user_input.lower() == 'resource':
        print("- download")
        return True

    if user_input.startswith('git'):
        git_command = 'git ' + user_input[3:].strip()
        output = execute_command(git_command)
        print(output)
        explanation = explain_git_command(user_input.split()[1].lower())
        print(explanation)
    elif user_input.startswith('download'):
        print("Git Cheat Sheet")
        command_parts = user_input.split()
        if len(command_parts) == 1:
            url = URL
            file_path = "git-cheat-sheet-education.pdf"
            if download_pdf(url, file_path):
                print(f"\033[1;42mPDF downloaded successfully as {file_path}!\033[0m")
            else:
                print("\033[1;31mFailed to download PDF!!\033[0m")

    else:
        print("\033[1;31mInvalid command. Please enter a valid option!\033[0m")

    return True


def main():
    print("\033[38;5;214mWelcome to the Learn Git CLI!\033[0m")
    print("\033[1;35mLet's Chat!\033[0m")
    print("Enter 'exit' to quit.")
    print("Enter 'learn' to understand the existing commands.")
    print("Enter 'resource' for additional resources.")

    while True:
        user_input = input(">>> ")
        if not process_input(user_input):
            break


if __name__ == '__main__':
    main()
