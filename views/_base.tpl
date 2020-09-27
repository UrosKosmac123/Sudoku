<html>

<head>
    <title>Sudoku</title>

    <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">

    <!--Let browser know website is optimized for mobile-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>

    <style>
        body {
            font-family: 'Inter', sans-serif;
        }

        table.matrix {
            width: 100%;
            table-layout: fixed;
            border-spacing: 0;
            border-collapse: collapse;
            border: 2px solid #6C757D;
        }
        table.matrix td {
            position: relative;
            padding: 0;
            border: 1px solid #6C757D;
            height: 0;
            padding-bottom: calc(100% / 9);
        }
        table.matrix td:nth-child(3),
        table.matrix td:nth-child(6) {
            border-right: 2px solid #6C757D;
        }
        table.matrix tr:nth-child(3) td,
        table.matrix tr:nth-child(6) td {
            border-bottom: 2px solid #6C757D;
        }
        table.matrix td input {
            position: absolute;
            text-align: center;
            border: none !important;
            margin: 0;
            width: 100%;
            height: 100%;
        }
        table.matrix td input.locked {
            background-color: #6C757D80;
        }
        table.matrix td input.error {
            background-color: #ff000080;
        }
        table.matrix td input.empty {
            font-weight: bold;
        }
        table.matrix td input:disabled {
            color: unset;
        }

        form {
            margin-block-end: 0;
        }
    </style>
</head>

<body>
    % include("_nav.tpl")
    {{!base}}

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>

    <script>
        function validateMatrixCellInput(event) {
            const regexp = /[1-9]$/;
            const match = event.target.value.match(regexp);
            event.target.value = match && match[0] || "";
        }

        (function () {
            const cells = document.querySelectorAll("table.matrix input");
            cells.forEach(cell => {
                cell.addEventListener("input", validateMatrixCellInput);
            })
        })();

    </script>
</body>

</html>