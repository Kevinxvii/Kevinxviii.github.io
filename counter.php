<?php
// Set the name of the file that will store the visitor count
$filename = "count.txt";

// Open the file for reading
$fp = fopen($filename, "r");

// Read the current count from the file
$count = fread($fp, filesize($filename));

// Close the file
fclose($fp);

// Increment the count
$count = $count + 1;

// Open the file for writing
$fp = fopen($filename, "w");

// Write the new count to the file
fwrite($fp, $count);

// Close the file
fclose($fp);

// Print the count to the screen
echo "Tu sei il visitatore numero " . $count . " del mio sito.";
?>