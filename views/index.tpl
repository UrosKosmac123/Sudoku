<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel='stylesheet' type='text/css' media='screen'>
        <title>Sudoku</title>
    </head>
<body>

    <form>
        <style>
            table { border-collapse: collapse; font-family: Calibri, sans-serif; font-size: 20px; margin-left: auto; margin-right: auto; text-align: center; }
            colgroup, tbody { border: solid medium; }
            td { border: solid thin; height: 2.4em; width: 2.4em; text-align: center: ; padding: 0; }
            .button { text-align: center; }
            </style>
            <table>
            <caption><h1>Sudoku</h1></caption>
                <tbody>
                    % for row in range(9):
                        <tr>
                            % for col in range(9):
                                <td>
                                    <input type="number" name="{{col}}-{{row}}" min="1" max="9" />
                                </td>
                            % end
                        </tr>
                    % end
                </tbody>
                
                <button>Preveri</button>
            
            </table>
            
    </form>
    
</body>


</html>