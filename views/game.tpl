% rebase("_base.tpl")
% setdefault("errors", [[None] * 9] * 9)

<div class="container py-3">

    <form class="mx-auto" style="max-width: 32rem;" method="POST">

        % include("_matrix.tpl", game=game, editable=True, errors=errors)

        % if game.state.solved():
            <button class="btn btn-light mt-4 float-right" disabled>Rešeno</button>
        % else:
            <button class="btn btn-primary mt-4 float-right">Preveri</button>
        % end
    </form>

</div>