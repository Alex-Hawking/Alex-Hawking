from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import subprocess
import os

github_token = os.environ.get('GITHUB_TOKEN')
repo_url = f'https://Alex-Hawking:{github_token}@github.com/Alex-Hawking/Alex-Hawking.git'

repo_path = '.'
repo = Repo(repo_path)


def edit_background_color(html_file, element_id, new_color):
    # Read the HTML file
    with open(html_file, 'r') as file:
        html_content = file.read()

    # Parse the HTML
    soup = BeautifulSoup(html_content, 'xml')

    # Find the element by ID
    element = soup.find(id=element_id)
    if element:
        # Modify the background color
        element['style'] = f'width: 45px; height: 45px; background-color: {new_color};'

        with open(html_file, 'w') as file:
            file.write(str(soup))

        subprocess.run(['git', 'add', '.'])
        commit_message = "Update: " + element_id + " to " + new_color
        subprocess.run(['git', 'commit', '-m', commit_message])
        subprocess.run(['git', 'push', repo_url, 'master'])
        result = subprocess.run(['git', 'push', repo_url, 'master'], capture_output=True, text=True)
        if result.returncode != 0:
            print("Error pushing to GitHub:", result.stderr)
            return False
        else:
            print("Pushed successfully:", result.stdout)
        return True
    else:
        return False

# Example usage
html_file = 'table.svg'  

app = Flask(__name__)
@app.route('/update-color', methods=['POST'])
def update_color():
    data = request.get_json()  
    location = data.get('pos')
    color = data.get('color') 

    print(location, color)
    edit_successful = edit_background_color(html_file, location, color)
    if edit_successful:
        print("Background color updated successfully.")
    else:
        print("Element not found.")

    
    return jsonify(message='Color updated successfully')

if __name__ == '__main__':
    app.run(debug=True)

