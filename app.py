from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import subprocess
from git import Repo, GitCommandError

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

        try:
            repo.git.add(A=True)
        except GitCommandError as e:
            print(f"Error: {e}")

        commit_message = 'Update SVG file'
        try:
            repo.git.commit('-m', commit_message)
        except GitCommandError as e:
            print(f"Error: {e}")

        remote_name = 'origin'
        branch_name = 'master'  # Replace with your branch name

        try:
            repo.git.push(remote_name, branch_name)
        except GitCommandError as e:
            print(f"Error: {e}")
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

