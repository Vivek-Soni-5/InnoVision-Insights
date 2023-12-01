<?php

$DOMAIN_NAME = "localhost";  
$DATABASE_NAME = "docintel";
$USERNAME = "root";     //username of phpmyadmin
$PASSWORD = "";     //password of phpmyadmin

//making connection 
$conn = mysqli_connect("$DOMAIN_NAME", "$USERNAME", "", "$DATABASE_NAME");
if($conn)
{
    echo "Connection Success\n";
}
else
{
    echo "Connection Failed\n";
}

$urls = null;

// if ($_SERVER['REQUEST_METHOD'] === 'POST')
//     {
//         $json = file_get_contents('php://input');
//         $data = json_decode($json, true);
//         $num_url = $data['num_url'];
//         $urls = $data['urls'];
//     }

$uploadDir = '/pdf_database';   // directory where pdfs is stored

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $uploadedFile = $_FILES['pdfFile'];

    // Check if the file is a PDF
    $fileType = pathinfo($uploadedFile['name'], PATHINFO_EXTENSION);
    if (strtolower($fileType) !== 'pdf') {
        echo 'Please upload a PDF file.';
        exit;
    }

    // Move the uploaded file to the destination directory
    $destination = $uploadDir . '/' . $uploadedFile['name'];
    move_uploaded_file($uploadedFile['tmp_name'], $destination);

    echo 'File uploaded successfully.';
}

$flaskUrl_extract_many_pdf = 'http://127.0.0.1:5000/extract_many_pdf';

if($urls != null)
{
    $data = array(
        'num' => $num_url,
        'urls' => $urls
    );

    // Initialize a new cURL session
    $ch = curl_init($flaskUrl_extract_many_pdf);
    // CURLOPT_RETURNTRANSFER instructing cURL to return the response as a string instead of outputting it directly.
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    // Set the request method to POST
    curl_setopt($ch, CURLOPT_POST, true);
    // Set CURLOPT_POSTFIELDS with encoded data
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
    // Execute the request and store the response
    $response = curl_exec($ch);
    // Close the cURL session
    curl_close($ch);

    if($response)
    {
        $index_name = mt_rand(10000, 99999);
        $responseArray = json_decode($response, true);
        if($responseArray != null)
        {
            foreach($responseArray as $item)
            {
                $videoID = null;
                $videoTitle = null;
                $videoThumbnail = null;
                $product_description = $item['product_description'];
                $link_to_buy_again = $item['link_to_buyAgain'];
                $name = $item['name'];
                $address = $item['address'];
                $pan = $item['PAN'];
                $total = $item['total'];
                $invoiceNumber = $item['invoice_number'];
                $invoiceDate = $item['invoice_date'];
                $productReviewVideos = $item['product_review_video'];
                foreach ($productReviewVideos as $video) {
                    $videoTitle = $video['title'];
                    $videoID = $video['videoID'];
                    $videoThumbnail = $video['thumbnail'];
                }

                $sql_query = "INSERT INTO `invoice`(`invoice_number`, `invoice_date`, `pan_number`,`name`,`address`,`product_description`,`total_value`,`purchase_links`,`related_video_id`,`related_video_title`,`related_video_thumbnail`) VALUES (?,?,?,?,?,?,?,?,?,?,?)";
                $stmt = mysqli_prepare($conn, $sql_query);
                mysqli_stmt_bind_param($stmt, "sssssssssss", $invoiceNumber, $invoiceDate, $pan, $name, $address, $product_description, $total, $link_to_buy_again, $videoID, $videoTitle, $videoThumbnail);
                mysqli_stmt_execute($stmt);
                if(mysqli_stmt_errno($stmt)) {
                    $error_message = mysqli_stmt_error($stmt);
                }
                mysqli_stmt_close($stmt);
            }
            echo "successfull !";
        }
        else
        {
            echo "Error Decoding json data!";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PDF Uploader</title>
</head>
<body>

<form action="main_screen.php" method="post" enctype="multipart/form-data">
    <label for="pdfFile">Choose a PDF file:</label>
    <input type="file" name="pdfFile" id="pdfFile">
    <input type="submit" value="Upload">
</form>

</body>
</html>
