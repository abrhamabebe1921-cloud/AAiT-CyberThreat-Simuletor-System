<?php
// source/low.php — DVWA-style Low Level SSTI challenge (intentionally vulnerable)


ini_set('display_errors', 0);
error_reporting(E_ALL);


$message = '';
$output  = '';
$input   = $_POST['template'] ?? 'Hello';


/**
* INTENTIONALLY VULNERABLE “template renderer”
* Replaces {{ expr }} with the result of evaluating PHP expressions.
* Provides a tiny context: $user, $now, $server
*/
function vulnerable_render_template(string $tpl, array $context = []): string {
   // Make context variables ($user, $now, $server) directly available
   extract($context, EXTR_SKIP);


   return preg_replace_callback('/\{\{\s*(.*?)\s*\}\}/s', function ($m) use ($context) {
       // Re-extract so each callback has the context in scope
       extract($context, EXTR_SKIP);


       $expr = $m[1];
       ob_start();
       $result = null;


       // Try to evaluate as an expression first: {{ 7*7 }} or {{ phpversion() }}
       try {
           $result = eval('return ' . $expr . ';');
       } catch (Throwable $e1) {
           // If that fails (e.g., {{ echo "hi"; }}), try as a statement
           try {
               eval($expr . ';');
               $result = null; // echoed output will be captured
           } catch (Throwable $e2) {
               ob_end_clean();
               return '[error: ' . htmlspecialchars($e2->getMessage(), ENT_QUOTES, 'UTF-8') . ']';
           }
       }


       $echoed = ob_get_clean();
       if ($echoed !== '') {
           return $echoed;
       }
       if (is_null($result)) {
           return '';
       }
       return is_scalar($result) ? (string)$result : '[non-scalar]';
   }, $tpl);
}


if ($_SERVER['REQUEST_METHOD'] === 'POST') {
   if (trim($input) === '') {
       $message = 'Please enter a template.';
   } else {
       // Minimal context exposed to the template (for realism)
       $ctx = [
           'user'   => 'guest',
           'now'    => time(),
           'server' => $_SERVER, // e.g., {{ server["SERVER_SOFTWARE"] }}
       ];
       // VULNERABLE sink
       $output = vulnerable_render_template($input, $ctx);
   }
}


$html = "
<form method='POST'>
   <label>Enter Note to Display:</label><br>
   <textarea name='template' rows='6' cols='60' placeholder='Try: Hello {{ user }} or {{ phpversion() }}'>"
   . htmlspecialchars($input ?? '', ENT_QUOTES, 'UTF-8') .
"</textarea><br><br>
   <button type='submit'>Render</button>
</form>
";


if ($message) {
   echo "<p style='color:red; font-weight:bold;'>".htmlspecialchars($message, ENT_QUOTES, 'UTF-8')."</p>";
}


if ($output !== '') {
   echo "<h3>Rendered Output:</h3>
       <div>$output</div>";
}


// DVWA body block (matches your format)
$page['body'] .= "<div class='body_padded'>
   <h2>Low Level - SSTI Vulnerability</h2>
   <details style='margin-top:16px;'><summary>Hints</summary>
   <p>This page renders a naive template. Anything inside <code>{{ ... }}</code> is evaluated as PHP (INTENTIONALLY VULNERABLE).</p>
   <ul>
       <li>Math: <code>{{ 7*7 }}</code></li>
       <li>PHP version: <code>{{ phpversion() }}</code></li>
       <li>Read file: <code>{{ file_get_contents(\"/etc/hostname\") }}</code></li>
       <li>Command exec: <code>{{ system(\"id\") }}</code> or <code>{{ shell_exec(\"ls -la\") }}</code></li>
       <li>Echo: <code>{{ echo \"hi\"; }}</code></li>
   </ul>
   </details>
   $html
</div>";

