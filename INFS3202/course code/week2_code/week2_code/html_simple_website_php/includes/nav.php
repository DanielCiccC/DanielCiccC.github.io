<nav>
  <ul>
    <li><a href="index.php" <?php if ($activePage == 'index') { echo 'class="active"'; } ?>>Home</a></li>
    <li><a href="about.php" <?php if ($activePage == 'about') { echo 'class="active"'; } ?>>About</a></li>
    <li><a href="contact.php" <?php if ($activePage == 'contact') { echo 'class="active"'; } ?>>Contact</a></li>
  </ul>
</nav>
