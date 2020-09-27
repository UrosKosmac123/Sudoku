% setdefault("editable", False)
% setdefault("errors", [[None] * 9] * 9)

<table class="matrix">
    <tbody>
        % for x in range(9):
            <tr>
            % for y in range(9):
                <td>
                    % disabled = not editable or game.state.locked[x][y]
                    % locked = game.state.locked[x][y]
                    % value = game.state.matrix[x][y]
                    % error = errors[x][y]
                    <%
                        classes = []
                        if locked:
                            classes.append("locked")
                        end
                        if error:
                            classes.append("error")
                            value = error[0]
                        end
                        if not value:
                            classes.append("empty")
                        end
                    %>
                    <input
                        class="{{ ' '.join(classes) }}"
                        pattern="[1-9]{1}"
                        maxlength="1"
                        value="{{value or ''}}"
                        % if disabled:
                            disabled="disabled"
                        % else:
                            name="{{x}},{{y}}"
                        % end
                    >
                </td>
            % end
            </tr>
        % end
    </tbody>
</table>