<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel='stylesheet' type='text/css' media='screen'>
        <title>Sudoku</title>
    </head>
<body>
    
    <h1>Sudoku</h1>

    <form>
        <table>
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
        </table>
        <button>Preveri</button>
    </form>
    
</body>


</html>