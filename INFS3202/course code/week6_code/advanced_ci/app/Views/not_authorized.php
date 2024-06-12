<?= $this->extend('template') ?>
<?= $this->section('content') ?>

<h2>Not Authorized</h2>

<p>You do not have permission to access this page.</p>

<p><a href="<?= base_url('login') ?>">Login</a></p>

<?= $this->endSection() ?>