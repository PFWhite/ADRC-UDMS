<?php
    include('/var/www/redcap/redcap_v' . $argv[1] . '/Config/init_functions.php');
    include('./redcap_actions_config.php');

    define('USERID', 'site_admin');

    if(!isset($enable_logging)) {
        $enable_logging = true;
    }

    foreach ($projects as $project_id) {
        deleteProjectNow($project_id, $enable_logging);
    }
?>
