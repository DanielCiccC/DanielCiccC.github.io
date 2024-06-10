# Lab 7 - RESTful API's

### Why RESTful was Developed:
- REST was developed to provide a simpler, more cohesive approach to designing network applications while reducing the complexity of communication between client and server. 
- It emphasizes scalability, generality of interfaces, and independent deployment of components. This approach allows developers to build reliable, performant, and scalable web services.

### JSON
- JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate. RESTful APIs commonly use JSON to format the data being sent and received

**JSON Objects**
Objects are enclosed in curly braces `{}`
```json
{
  "firstName": "Mary",
  "lastName": "Wise",
  "isStudent": false
}
```

A JSON list is an ordered collection of values, which are enclosed in square brackets `[]`

```json
[
  {"firstName": "John", "lastName": "Doe"},
  {"firstName": "Jane", "lastName": "Smith"},
  {"firstName": "Wei", "lastName": "Chen"}
]
```

### fetchAPI

The Fetch API provides a JavaScript interface for accessing and manipulating parts of the HTTP pipeline, such as requests and responses. 

- One of the key features of the Fetch API is that it uses *Promises*, which enables a simpler and cleaner way to handle asynchronous operations compared to callbacks.

**Here’s a basic breakdown of how to use the Fetch API:**

- **Making Requests:** You use the fetch() function, which accepts the URL of the resource you want to fetch and an optional configuration object where you can specify the method, headers, body, and other settings.
- **Handling Responses:** The fetch() function returns a Promise that resolves with the Response object once the request completes. The Response object does not directly contain the actual body but provides methods to handle it, such as json(), text(), or blob().
- **Error Handling**: If the request fails due to network issues, fetch() rejects the Promise. It’s important to note that HTTP error statuses (like 404 or 500) do not cause the Promise to be rejected. You must check the ok status or the status code to handle such errors.

const educationData = {
  institution: 'MIT',
  studyType: 'BSc',
  area: 'Computer Science',
  startDate: '2019-08',
  endDate: '2023-05'
};

const apiUrl = 'https://example.com/api/education';

```javaScript
fetch(apiUrl, {
  method: 'POST',  // or 'PUT' if updating
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(educationData)
})
.then(response => {
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  return response.json();  // Parse JSON response into native JavaScript objects
})
.then(data => {
  console.log('Success:', data);
  alert('Education added successfully!');
})
.catch(error => {
  console.error('Error:', error);
  alert('Error adding education.');
});
```

### Template ``<template>`` tag
- The HTML ``<template>`` tag is a mechanism for holding client-side content that you don’t want to be rendered when the page loads.

    - **Non-rendering**: Content inside a `<template>` tag is not displayed on the page when it loads. The content can contain any HTML, including images, tables, and other resources that are parsed but not rendered.
    - **Reusable**: The content can be cloned and inserted in the document multiple times using JavaScript. This avoids redundancy in HTML code and allows for dynamic generation of content based on user actions or data received from the server.
    - **Efficiency**: Since the content is only parsed and not rendered, it can improve the page’s load time and performance by not processing content until necessary.

**HTML**
```html
<template id="userFormTemplate">
  <div class="user-form">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name">
    <button type="button">Submit</button>
  </div>
</template>
```

**JavaScript**
```javaScript
document.getElementById('addFormBtn').addEventListener('click', function() {
  const template = document.getElementById('userFormTemplate');
  const clone = template.content.cloneNode(true); // Deep clone the template content
  document.body.appendChild(clone); // Append the cloned content to the body
});
```


