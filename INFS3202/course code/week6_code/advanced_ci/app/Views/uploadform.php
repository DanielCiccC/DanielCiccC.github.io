<!DOCTYPE html>
<html>
<head>
    <title>Dropzone File Upload</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/dropzone/5.9.2/min/dropzone.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/dropzone/5.9.2/min/dropzone.min.js"></script>
    <style>
        .message {
            margin-top: 20px;
            padding: 10px;
            border-radius: 5px;
        }
        .success {
            background-color: #d4edda;
            color: #155724;
        }
        .error {
            background-color: #f8d7da;
            color: #721c24;
        }
    </style>
</head>
<body>
    <h2>Dropzone File Upload</h2>

    <form action="<?= base_url('upload'); ?>" class="dropzone" id="myDropzone">
        <?= csrf_field() ?>
    </form>

    <div id="message" class="message"></div>

    <script>
        Dropzone.options.myDropzone = {
            paramName: "file",
            maxFilesize: 2, // MB
            acceptedFiles: ".jpg,.jpeg,.png,.gif",
            init: function() {
                this.on("success", function(file, response) {
                    if (response.success) {
                        showMessage("File uploaded successfully!", "success");
                    } else {
                        showMessage("File upload failed!", "error");
                    }
                });
                this.on("error", function(file, errorMessage) {
                    showMessage("File upload error: " + errorMessage, "error");
                });
            }
        };

        function showMessage(message, type) {
            var messageElement = document.getElementById("message");
            messageElement.textContent = message;
            messageElement.className = "message " + type;
        }
    </script>
</body>
</html>