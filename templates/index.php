<!doctype html>
    <head>
        <title>UI</title>
        <meta charset="UTF-8">
        <meta name="viewport"content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="/static/test.css" type="text/css" />
    </head>
        <h2>Data in Topic</h2>
        <div class="table-wrapper">
            <table class="fl-table">
                <thead>
                <tr>
                    <th>Module Number</th>
                    <th>Location</th>
                    <th>CallbackURL</th>
                    <th>Date and Time</th>
                </tr>
                <?php
                    $servername = "localhost";
                    $username = "root";
                    $password = "password";
                    $dbname = "CarWashLog";

                    // Create connection
                    $conn = new mysqli($servername, $username, $password, $dbname);
                    // Check connection
                    if ($conn->connect_error) {
                        die("Connection failed: " . $conn->connect_error);
                    }

                    $sql = "SELECT module_no, place, callbackurl, time_stamp FROM topicdetails";
                    $result = $conn->query($sql);

                    if ($result->num_rows > 0) {
                        while($row = $result->fetch_assoc()) {
                            echo "<tr><td>" . $row["module_no"]. "</td><td>" . $row["place"]. "</td><td>" . $row["callbackurl"]. "</td><td>" . $row["time_stamp"]."</td></tr>";
                        }
                    } else {
                        echo "0 results";
                    }

                    $conn->close();
                    ?>
                </thead>
            </table>
        </div>
</html>