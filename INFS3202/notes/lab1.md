# Lab 1 Important concepts

### SSH
- SSH, or Secure Shell, also known as Secure Socket Shell, is a protocol that facilitates a secure connection to a remote computer or server through a text-based interface
- Upon establishing a secure SSH connection, a shell session is initiated, allowing the manipulation of the server through commands issued via the client on the local machine

Login to UQCloud through SSH: (usning PuTTY)

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

