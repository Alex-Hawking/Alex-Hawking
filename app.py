from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import subprocess
import os

github_token = os.environ.get('TOKEN')
repo_url = f'https://Alex-Hawking:{github_token}@github.com/Alex-Hawking/Alex-Hawking.git'

readme_file='./README.md'

subprocess.run(['git', 'config', '--global', 'user.email', 'alexhawking23@gmail.com'])
subprocess.run(['git', 'config', '--global', 'user.name', 'Alex-Hawking'])

subprocess.run(['git', 'clone', repo_url, 'repo_folder'])

os.chdir('repo_folder')


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
        element['style'] = f'width: 25px; height: 25px; background-color: {new_color};'

        with open(html_file, 'w') as file:
            file.write(str(soup))
        
        with open('./README_template.md', 'r') as file:
            readme_contents = file.read()

        updated_contents = readme_contents.replace('$RECENT UPDATE$', "Most recent change: " + element_id + " to " + new_color)

        with open('./README.md', 'w') as file:
            file.write(updated_contents)

        subprocess.run(['git', 'add', '.'])
        commit_message = "Update: " + element_id + " to " + new_color
        subprocess.run(['git', 'commit', '-m', commit_message])
        subprocess.run(['git', 'push', repo_url, 'master'])
        result = subprocess.run(['git', 'push', repo_url, 'master'], capture_output=True, text=True)
        if result.returncode != 0:
            print("Error pushing to GitHub:", result.stderr)
            return False

        return True
    else:
        return False

# Example usage
table_file = 'table.svg'  

app = Flask(__name__)
@app.route('/update-color', methods=['POST'])
def update_color():
    client = request.remote_addr
    if client == os.environ.get('ENEMY'):
        return jsonify(message='Go away')
    data = request.get_json()  
    location = data.get('pos')
    color = data.get('color') 

    edit_successful = edit_background_color(table_file, location, color)
    if edit_successful:
        return jsonify(message='Color updated successfully :)\n Wait a few minutes and it should be reflected on my profile:\nhttps://github.com/Alex-Hawking')
    else:
        return jsonify(message='Color update failed :(')

    

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) 
    app.run(debug=True, host='0.0.0.0', port=port)

