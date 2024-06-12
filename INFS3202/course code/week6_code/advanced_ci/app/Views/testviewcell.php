<?= $this->extend('template') ?>
<?= $this->section('content') ?>

<h1>Testing the Alert View cell</h1>

<?= view_cell('AlertMessageCell', 'type=success, message=The task has been successful.') ?>

<?= view_cell('AlertMessageCell', 'type=warning, message=The task has failed.') ?>

<?= view_cell('AlertMessageCell', 'type=info, message=This is additional information.') ?>


<?= $this->endSection() ?>

