<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Home - My Website</title>
  <link rel="stylesheet" href="<?= base_url('styles/style.css'); ?>">

</head>
<body>
  <header>
    <h1>My Website</h1>
  </header>
  
  <nav>
    <ul>
        <li><a href="/" class="<?= service('router')->getMatchedRoute()[0] == '/' ? 'active' : ''; ?>">Home</a></li>
        <li><a href="/about" class="<?= service('router')->getMatchedRoute()[0] == 'about' ? 'active' : ''; ?>">About</a></li>
        <li><a href="/contact" class="<?= service('router')->getMatchedRoute()[0] == 'contact' ? 'active' : ''; ?>">Contact</a></li>
    </ul>
  </nav>

  <main>
    <?= $this->renderSection('content') ?> <!-- Placeholder for page content -->
  </main>

  <footer>
    <p>&copy; &copy; <?= date('Y') ?> My Website. All rights reserved.</p>
  </footer>
</body>
</html>

