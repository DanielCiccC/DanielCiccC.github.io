# HTML tags

Form, a, img, link, table, p,

### `<form>`
- An HTML form is used to collect user input. The user input is most often sent to a server for processing.
- 
**Attributes**
- `method` - can be sent with `"get"` or `"post"`
- `action` - page specified to send the data
- `target` - The target attribute can be used to control how the linked content is displayed when clicked eg _blank opens the link in a new tab or window.

```html
<form method="get" action="<?= base_url('admin/'); ?>">
    <div class="input-group">
        <input type="text" class="form-control" placeholder="Enter your search..." name="search">
        <button class="btn btn-primary" type="submit">Search</button>
    </div>
</form>
```
**Elements used inside forms**
- ``<input>`` is a single line text field
- ``<textarea>`` is a multiline text field
- ``<button>`` is a button and with the type attribute set to ‘submit’ will send the values entered into the form to the action path of the form 

---

### `<a>`

The `<a>` tag defines a hyperlink, which is used to link from one page to another.

The href value can be an absolute URL, a relative URL, or a URL fragment (used for scrolling to specific sections within the same page).

- **Absolute URL:** A complete web address, including the protocol 
(e.g., http://, https://), domain, and path. 
```html
 <a href="https://www.example.com">Visit</a>
```
- **Relative URL:** A partial web address that is relative to the current 
page's location. Relative URLs are often used for links within the 
same website. 
```html
<a href="about/index.html">Learn More</a>
```
---

### `<img>`

The `<img>` tag is used to embed an image in an HTML page.
- Images are not technically inserted into a web page; images are linked to web pages. The `<img>` tag creates a holding space for the referenced image.

**attributes**
- `alt` - alternate text for an image
- `src` - Specifies the path to the image

**Usage**

```html
<img src="img_girl.jpg" alt="Girl in a jacket" width="500" height="600">
```
---

### ``<ul>`` and `<ol>`

**Usage**
```html
<ol start="50">
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol>

<ul>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>
```
**Rendered**

<ol start="50">
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol>

<ul>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>

---

### `<table>`

-  `<tr>` defines a table row
-  `<th>` element defines a table header
-  `<td>` element defines a table cell

```html
<table>
  <tr>
    <th>Month</th>
    <th>Savings</th>
  </tr>
  <tr>
    <td>January</td>
    <td>$100</td>
  </tr>
</table>
```

**Rendered**
<table>
  <tr>
    <th>Month</th>
    <th>Savings</th>
  </tr>
  <tr>
    <td>January</td>
    <td>$100</td>
  </tr>
</table>

---

### `<link>`

The `<link>` tag defines the relationship between the current document and an external resource.

```html
<head>
  <link rel="stylesheet" href="styles.css">
</head>
```

---

### `<main>`

---

### `<footer>`

---

### `<html>`

---

### `<section>`

---

### `<label>`

