# Lab 4 - Forms

Ensure that both the search input field and the Search button are enclosed within ``<form>`` tags, setting the form’s method to GET to facilitate easy retrieval of query parameters. The type of the Search button must be set to Submit as the button needs to send the form data to the server.

```html
<div class="row mb-4">
    <div class="col-md-6 mb-3 mb-lg-0">
        <form method="get" action="<?= base_url('admin/'); ?>">
            <div class="input-group">
                <input type="text" class="form-control" placeholder="Enter your search..." name="search">
                <button class="btn btn-primary" type="submit">Search</button>
            </div>
        </form>
    </div>
    <div class="col-md-6 text-md-end">
        <button class="btn btn-primary" href="<?= base_url('addedit/');?>">Add User</button>
    </div>
</div>
```

- When the form method is set to `GET`, the form data is encoded into the URL, appended as query parameters. This behavior has several advantages:
  - **Bookmarkability**: Users can bookmark specific searches for quick access in the future.
  - **Shareability**: It’s easy to share URLs with specific query parameters, facilitating collaboration or support scenarios.

### Implement the Add/Edit Functionality
- In the interest of efficiency and minimizing redundancy, we aim to streamline the user management process by utilizing a single form and controller method for both adding and editing users.

  - Configure a grouped route that responds to both `GET` and `POST` requests

```php

use CodeIgniter\Router\RouteCollection;

/**
 * @var RouteCollection $routes
 */

$routes->get('/', 'ResumeController::index');

// Routes for admin
$routes->group('admin', function($routes) {
    $routes->get('/', 'ResumeController::admin');
    $routes->match(['get', 'post'], 'addedit', 'ResumeController::addedit');
    $routes->match(['get', 'post'], 'addedit/(:num)', 'ResumeController::addedit/$1');
    $routes->get('delete/(:num)', 'ResumeController::delete/$1');
});

$routes->get('/resume/(:num)', 'ResumeController::resume/$1');
```


### FlashData
