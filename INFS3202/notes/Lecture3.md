# Lecture 3

### The MVC Architecture

- The 3-Layer Architecture is a software design pattern that divides applications into three main categories or layers: 
  - Presentation
  - Business Logic (or Application Layer)
  - Data Layer
- This architecture aims to separate the user interface, the business logic, and the data storage, which promotes a clean separation of concerns.


![alt text](assets\IMG18.PNG)


The MVC pattern is a specialized form of 3-layer architecture, making it highly relevant to modern web development practices

### Components of MVC
Model–view–controller (MVC) - a software architectural pattern, that separates an application's data, user 
interface, and control flow into three components: 
- Model: 
  - Represents the data. 
  - The model is often connected to a database and is responsible for retrieving and storing data.
- View: 
  - Represents the user interface of an application, 
  - is responsible for displaying data and getting user input. 
  - HTML, CSS, and JavaScript.
- Controller:
  - Manages the flow of data between the model and the view, 
  - is responsible for processing user input and directing the application’s behaviour. 
  - includes code that implements business rules and other functionality.

![alt text](assets\IMG19.PNG)


### Benefits of MVC
- Simplifies Complex Applications:
  
By separating the application into three components, developers can 
focus on one aspect without affecting others.
- Facilitates Parallel Development:

Different developers can work on the Model, View, and Controller 
simultaneously.
- Easy to Modify or Scale:

Changes to the business logic or user interface can be made with 
minimal impact on the other components.
- Supports Reusability:

Components can be reused across different parts of the application or in 
different applications.


### Convention vs Configuration
**Convention vs. Configuration** is a design philosophy that:
- impacts how software frameworks are structured  (i.e. where files are located)
- how they expect developers to interact with them
- It's a trade-off between the ease of following predefined paths and files (convention) or the flexibility to define everything explicitly (configuration).
- Important advice:
  - Web frameworks (CodeIgniter, Django, Ruby on Rails, Flask, Next,JS) come with a predefined folder structure
  - Learn what the structure is and where files go
  - This will improve your productivity!

## Codeigniter


