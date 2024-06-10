# Lab 1 Important concepts

### SSH
- SSH, or Secure Shell, also known as Secure Socket Shell, is a protocol that facilitates a secure connection to a remote computer or server through a text-based interface
- Upon establishing a secure SSH connection, a shell session is initiated, allowing the manipulation of the server through commands issued via the client on the local machine

Login to UQCloud through SSH: (using PuTTY)

locate hostname
```
infs3202-xxxxx.zones.eait.uq.edu.au
```

Through Powershell:

```
ssh studentusername@infs3202-yourcode.zones.eait.uq.edu.au
```



Connection type SSH

### File Management on the UQCloud zone

**File Transfer Protocol (FTP)**
- Standard network protocol used for transferring files from one host to another over a TCP-based network, such as the internet
- It utilizes a client-server model, where the FTP client initiates a connection to the FTP server and requests the transfer of one or more files

**Secure File Transfer Protocol (SFTP)**
- SFTP is based on the SSH protocol and is designed to be a more secure alternative to FTP. 
- It encrypts all the data in transit, including authentication credentials and the actual data being transferred, ensuring that it cannot be intercepted or modified by unauthorized third parties.

The UQCloud zone webserver employs SFTP as its data transfer protocol. Therefore, in order to manage files on the UQzone, either FileZilla or WinSCP can be used.


## Nginx

### Configuration file

Can use ``nano`` as in-terminal text editor:

```bash
nano /etc/nginx/sites-enabled/https-site
```

```
http {
    server {
        listen 80; # Listen on port 80 for HTTP requests
        server_name example.com; # Replace with your domain name or use localhost

        # Document root where the files are located
        root /var/www/html/htdocs;

        # Default file to serve
        index index.html index.htm;

        # Serve files
        location / {
            try_files $uri $uri/ =404;
        }
    }
}
```

### Serving files with Nginx

By placing an HTML file in the ``htdocs`` folder (or the specified root directory), you can view it by navigating to the corresponding URL. If you create a file named index.html within that directory, it would be served as the default page when accessing the root URL of your server.

- A file located at ``/var/www/htdocs/about/index.html`` can be accessed at https://yourdomain.com/about/.
- A file located at ``/var/www/htdocs/products/widget.html`` can be accessed at https://yourdomain.com/products/widget.html.

also included this:
```
location /resumebuilder {
    alias /var/www/resumebuilder/public/;
    try_files $uri $uri/ @resumebuilder;

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php8.3-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $request_filename;
    }
}

location @resumebuilder {
    rewrite /resumebuilder/(.*)$ /resumebuilder/index.php?/$1 last;
}
```

- location /resumebuilder { ... }:
  - This block matches any request starting with /resumebuilder.
- ``alias /var/www/resumebuilder/public/;:``
  - This means that for any request matching /resumebuilder, the part /resumebuilder is replaced with /var/www/resumebuilder/public.

## Important linux commands

``ssh``:
- connects to secure shell of another server

Example
```bash
ssh studentusername@infs3202-yourcode.zones.eait.uq.edu.au
```

``nano``:
- A text editor that runs in browser
- usage: ``nano <filename>``

```bash
nano /etc/nginx/sites-enabled/https-site
```

``sudo``
- stands for 'system user do'
- allows you to perform commands as a different user (superuser as default)
```bash
sudo systemctl start code-server@USERNAME
```


``curl``
- command line tool that developers use to transfer data to and from a server
```bash
curl http://example.com
```

``chmod``
- allows an administrator to set or modify a files permissions
- The characters are indicators for the presence or absence of one of the permissions. They are either a dash (-) or a letter. If the character is a dash, it means that permission is not granted. If the character is an r, w, or an x, that permission has been granted.
  - r: Read permissions. The file can be opened, and its content viewed.
  - w: Write permissions. The file can be edited, modified, and deleted.
  - x: Execute permissions. If the file is a script or a program, it can be run (executed).
Groups:
- u: User, meaning the owner of the file.
- g: Group, meaning members of the group the file belongs to.
- o: Others, meaning people not governed by the u and g permissions.
- a: All, meaning all of the above.

- ``-R`` - recursive
```bash
sudo chmod -R 777 /var/www/resumebuilder
```

``cd``
- change directory
```bash
cd <directory>
```

``mv``
- move file(s)
- file path needs to end in a /
```bash
mv [options(s)] [source_file_name(s)] [Destination_file_name or destination file path]
```

