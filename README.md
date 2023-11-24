## Hello World (⌐■ ͟ʖ■) 

I'm Alex Hawking, and I'm passionate about music, code, and everything in between. 🎵💻

I am currently displaying some community-created art. Find out how to contribute below!

**Recent Changes**
Most recent change: 3x13 to #FFFFFF

![](./table.svg)

[My Personal Website](https:/alexhawking.dev)  |  [LinkedIn Profile](https://www.linkedin.com/in/alex-hawking-3541b223a/)  |  [Instagram Profile](https://www.instagram.com/ah33803/)

<br /><br />

### How to vandalise my profile

As a fun (but poorly thought out project), you can now change the image displayed on the 16x16 grid on my README by sending a POST request to the endpoint described below.


**Endpoint Information**

- **URL**: `https://git-profile-2fa28e441ca5.herokuapp.com/update-color`
- **Method**: POST
- **Content-Type**: application/json

**Request Format**

Each request should be a JSON object containing two fields:
- `pos`: The position of the cell in the format 'x-coord x y-coord'. For example, '3x4'.
- `color`: The desired color in a valid CSS format (e.g., '#RRGGBB', 'rgb(r, g, b)').

*Example JSON:*
```json
{
  "pos": "3x4",
  "color": "#FF5733"
}
```
**Example Request**

To change a cell color using curl, execute the following command in your terminal:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"pos": "3x4", "color": "#FF5733"}' https://git-profile-2fa28e441ca5.herokuapp.com/update-color
```
Replace "3x4" with the desired cell position and "#FF5733" with the color you want.