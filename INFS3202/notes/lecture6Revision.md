# Lecture 6
# MVC – Advanced CodeIgniter

### Caching
- Caching is a technique used to store copies of files or data results in a temporary storage location 
(cache), so future requests for those files or data can be served faster. 
- In web development, caching can refer to storing parts of web pages or views, database query results, or 
even computational results to improve performance and reduce the load on the system.

**Why Do We Need It?**
- Performance Enhancement:
  - By reducing the need to perform time-consuming operations (like database queries or complex calculations) for every request, caching significantly speeds up the response time of applications.
- Reduced Load:
  - It decreases the load on the server, as cached content is served directly without going through the entire application logic or database querying process again.
- Improved User Experience:
  - Faster response times contribute to a smoother and more responsive user experience.
- Scalability:
  - Caching helps in scaling applications by managing resource utilization more efficiently, allowing the system to handle more users without requiring proportional increases in hardware or processing power.

> - using up server resources
> - Sometimes it might not be worth it to rerun queries and regenerate page
> - Person editing blog page e.g. once a week, might not need to regenerate page every min
>
> - Cache a page, and can just retrieve it
> - Faster, reduce the load on the server, and can scale the servers

### What type of Caching does CodeIgniter Support?
CodeIgniter provides a simple yet flexible caching mechanism that supports different types of 
caching:
- Page Caching:
This method caches the entire output of a page. When a request is made, CodeIgniter checks 
if a cached version of the page exists and serves it directly, bypassing the normal system 
execution.
- Querystring Caching:
Uses the combination of variables in the URL querystring and saves versions to the cache.

### Cache Config
- Location of Cache Settings:
The primary configuration file for cache settings in CodeIgniter is located at 
app/Config/Cache.php. Specify the default cache handler eg file or redis etc.

> - In codeigniter, a cache file directory
>   - HTML is rendered and saved
> - memcache, redis and filetype e.g.

### Where is the cached file stored?
- Cached files are saved in the writable/cache folder

- Get cache information
  - ``php spark cache:info``
- Clear cache
  - ``php spark cache:clear``

### File uploads
- File uploads are a critical component of many web applications, from social media platforms where users share images and videos, to business applications that handle documents, spreadsheets, and other business-critical files.

- **Personalization**: Allows users to upload avatars, backgrounds, or other personal images, 
enhancing their engagement and personal connection to the application.
- **Content Sharing**: Enables users to share content, such as photos, videos, and 
documents, facilitating collaboration and interaction within the application.
- **Dynamic Content**: File uploads are essential for content management systems (CMS), 
enabling administrators and users to update website content, including text, images, and 
videos.
- **Data Import**: Enables efficient data import processes, allowing users to upload files 
containing bulk data, which can be processed and integrated into the application's 
database.

> - upload images and share them, e.g.
> - upload their own image or avatar


### Processing a File Upload
**Create Routes**
- Same /uploads route will handle get and post
- Get will display the upload form
- Post will accept the posted file

![alt text](assets\IMG38.PNG)

**Create the View**
- Use the DropZone Javascript Library
- A CSRF must be included
in the form to make sure the
form post is from the same
server.

**View** | **Code**
| --- | ---
| ![alt text](assets\IMG39.PNG)| ![alt text](assets\IMG40.PNG)

**Create the Controller**
- The file is saved to /writable/uploads with a random filename
- A JSON response needs to be returned
- You will need to manage where uploads are stored for your users and how to secure access

![alt text](assets\IMG41.PNG)

