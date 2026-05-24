<?php
$_SERVER['REQUEST_METHOD'] = 'POST';
$_POST['template'] = 'Hello {{ 7*7 }}';
$page = [];
ob_start();
include('vulnerabilities/SSTI/source/low.php');
$out = ob_get_clean();
echo "OUTPUT IS:\n";
echo $output;
