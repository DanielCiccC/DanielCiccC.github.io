# Lecture 2

### Design document
- Project overview - purpose of project, target audience etc
- Key features
- UI / UX design HTML mockups
- Database Design - ER diagram with all database tables, fields and relationships between tables
- Technology research timeline 

### Structure of HTML

```html
<html>
<head>
  <title>Sample HTML Pag Structure</title>
</head>
<body>

  <h1>Heading 1</h1>

  <p><b>Welcome</b> to <i>HTML</i>!</p>

</body>
</html>
```

- Headings
- Paragraphs
- Lists (ordered and unordered)
- Images
- Tables

#### Adding CSS
```html
<head>
  <title>Common HTML Tags</title>
  <style>
    h1 {
      color: purple;
    }

    .rounded-border {
      border: 2px solid purple;
      border-radius: 8px;
    }
  </style>
</head>

<body>

  <h1>Heading 1</h1>

  <p><b>Welcome</b> to <i>HTML</i>!</p>

```

#### Why cascading?
- Cascading Style Sheets (CSS) refers to the priority scheme used to determine which style rules apply to elements in the web document if multiple rules conflict  or overlap. 
- This cascading mechanism allows multiple style sheets to influence the look of a document, with a well-defined order of precedence determining how conflicts are resolved. 
- If two rules have the same specificity, the last rule declared in the CSS is applied.

#### Advantages of Classless CSS Frameworks:
- Simplicity and Speed: Rapid development of websites by minimizing the need for writing custom CSS or applying specific classes to HTML elements.
- Learning Curve: Great for beginners because they don't require learning a system of classes.

#### \<a> Href tag
- The \<a> tag, also known as the anchor tag, is used in HTML to 
create hyperlinks that navigate to other web pages or resources.
- The href attribute within the \<a> tag specifies the destination 
URL that the link points to.

#### Simple form

- Each of elements can be included 
within a  ``<form>`` element
- Use the action and method attributes 
of the ``<form>`` element to specify where 
and how the form data should be 
submitted
- ``<input>`` is a single line text field
- ``<textarea>`` is a multiline text field
- ``<button>`` is a button and with the type attribute set to ‘submit’ will send the values entered into the form to the action path of the form 

### Forms – method Get vs Post
GET Method
- Data Appended to URL: Sends data in the URL itself, as key-value pairs in the query string.
- Read Operations: Typically used for retrieving data, not modifying it.
- Limited Data Size: Length restrictions due to URL length limitations (usually up to 2048 characters).
POST Method
- Data in Body: Sends data in the request body, allowing for larger and more complex payloads. No inherent size limitation like with GET.
- Write Operations: Typically used for sending data to be processed or stored on the server.
- Encoding: GET uses URL encoding, whereas POST allows for multiple data types (e.g., application/json, multipart/form-data).

#### Details and summary
• The ``<details>`` and ``<summary>`` tags are HTML elements used together to create an interactive widget that users 
can click to hide or show more content. 
• This feature is particularly useful for implementing FAQs, collapsible lists, or any content that benefits from a 
hide/show interaction to keep the page clean and improve user experience by not overwhelming them with 
information all at once.

### PHP
What is PHP?
- PHP: Hypertext Preprocessor
- Server-side scripting language designed for web development
- Can be embedded into HTML
Why Use PHP?
- Widely used and open-source
- Efficient for building dynamic web pages
- Compatible with various databases
- Large community and extensive documentation

#### Basic syntax
- Starts with <?php and ends with ?>
- PHP statements end with a semicolon (;)
- A PHP file normally contains HTML tags, and some PHP scripting codes. 
- The file extension is “.php”
