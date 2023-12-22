
# Hello World (⌐■ ͟ʖ■)

I'm **Alex Hawking**, a developer from Western Australia. 🎵💻

Currently curating **community-created art** on my 16x16 digital canvas you can see below. Fancy adding your pixel? See how below!

---

![](./table.svg)

---

**📢 Latest Canvas Update**
- Most recent change: 6x0 to #FFFFFF

## 🚀 Quick Links
[My Personal Website](https:/alexhawking.dev)  |  [LinkedIn Profile](https://www.linkedin.com/in/alex-hawking-3541b223a/)  |  [Instagram Profile](https://www.instagram.com/ah33803/)

---

## 🎨 Canvas Contributions - How to Vandalize Artistically

Want to ruin my potential employment oppurtunities? Paint on the canvas above! Just send a POST request:

### Endpoint Palette

- **URL**: `https://git-profile-2fa28e441ca5.herokuapp.com/update-color`
- **Method**: `POST`
- **Consumes**: `application/json`

### Pixel Placement Protocol

```json
{
  "pos": "x-coord x y-coord",
  "color": "CSS color code"
}
```

### Brush Stroke Example

```bash
curl -X POST -H "Content-Type: application/json" -d '{"pos": "3x4", "color": "#FF5733"}' https://git-profile-2fa28e441ca5.herokuapp.com/update-color
```

---

## 📊 My GitHub Stats

![Alex's GitHub stats](https://github-readme-stats.vercel.app/api?username=Alex-Hawking&show_icons=true)