<!DOCTYPE html>
<html>
<head></head><body>
<h1>Keyboard-Logger</h1>
<ul type="disc">
  <li>This program is useful for logging the pressed keyboard in the log file.</li>
  <li>It can run in attached .bat[Windows Batch] file.</li>
  <li>This Batch File will run the commands in "pythonw.exe" application.</li>
  <li>"pythonw.exe" application is useful to hide the running process.</li>
  <li>In Short about "pythonw.exe" application, It runs the process without Console.</li>
  <li>I have shared only for Educational Purpose</li> 
</ul>
<h3>Disclaimer</h3>
<ul><li>Running this File can have serious Ethical and Legal Implications, If it is used without the explicit consent of the computer owner.</li>
<li>Handle this kind of data with care due to the Privacy concerns related to Key logging.</li>
<li>You need to have necessary permissions and Legal Rights before using Key Logging</li>
<li>This Script might need to be run with Administrator Privileges</li>
<li>These are important to respect Privacy and use this program responsibly</li></ul>
<h3>Requirements</h3>
<ol type="1">
<li><h5>Python-3 or above</h5></li>
<li><h5>Python Modules</h5>
<ol type="a">
	<li>pynput.keyboard.Listener</li>
	<li>keyboard</li>
	<li>sys(Default Module)</li>
</ol></li>
</ol>
<h3>Installation</h3>
<ul><li>pip install pynput</li>
<li>pip install keyboard</li></ul>
<h3>How to Run</h3>
<video controls autoplay loop="true">
<source src="REC.mp4" type="video/mp4">
<source src="https://github.com/Sudharshank-cpu/Keyboard-Logger/assets/138243791/23912900-a52c-47a6-8630-238d24a3597f" type="video/mp4">
</video>
<ul><li>For Linux or MacOS users, Open "keyLogger.py" using python text editors or type "python (location_of_file)\keylogger.py" in your terminal</li>
<li>For Windows, Open "keyboardTrack.bat" Windows Batch file. Process has been begun.</li></ul>
<h3>How to Stop this program</h3>
<ul><li>Press "ctrl + z + x" to stop listening and ends the process.</li></ul>
<h3>Check "Task Manager"(Windows) or Process Tracking Application(Others) to "block or End the Process" in Python which is available in Processes tab at Task Manager.
<h3>Explaination</h3>
<ol><li>In "pynput.keyboard" module, "Key" is used to represent  special keys on keyboard like "ctrl","escape",etc.</li>
<li>"on_press(key)" function checks if "ctrl + z + x" keys are pressed to return False(Stops listener).</li>
<li>Otherwise, Opens the file(If not Creates a New File) as "keyboard_log.txt" using append mode. Writes the Pressed Keys and starts Listener.</li></ol>
<li>If you press Tabspace, Writes "    "(Four Spaces). If you press Enter, Writes new line. If key returns "_l" at end, key's position at Left Side. If key returns "_r" at end, key's position at Right Side.</li>
<li>Special Keys return as (key+" pressed\n").</li></ol>
</body>
</html>

https://github.com/Sudharshank-cpu/Keyboard-Logger/assets/138243791/23912900-a52c-47a6-8630-238d24a3597f

