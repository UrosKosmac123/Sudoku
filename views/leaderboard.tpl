% rebase("_base.tpl")

<div class="container py-3">
    <table class="table table-hover">
        <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Ime</th>
                <th scope="col">Rešenih iger</th>
            </tr>
        </thead>
        <tbody>
            % for i, entry in enumerate(leaderboard):
                % u, games = entry
                <tr className="{{ 'bg-success' if user.id == u.id else '' }}">
                    <th scope="row">{{i + 1}}</th>
                    <td>{{u.name}}</td>
                    <td>{{games}}</td>
                </tr>
            % end
        </tbody>
    </table>
</div>