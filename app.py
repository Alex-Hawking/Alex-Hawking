from flask import Flask, request, jsonify
from bs4 import BeautifulSoup

def edit_background_color(html_file, element_id, new_color):
    # Read the HTML file
    with open(html_file, 'r') as file:
        html_content = file.read()

    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the element by ID
    element = soup.find(id=element_id)
    if element:
        # Modify the background color
        element['style'] = f'background-color: {new_color};'

        with open(html_file, 'w') as file:
            file.write(str(soup))
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

