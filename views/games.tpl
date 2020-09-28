% rebase("_base.tpl")

<div class="container py-3">

    <div class="d-flex justify-content-between mb-3">
        <h2 class="mr-3">Vse igre</h2>
        <form action="/igre" method="POST">
            <button class="btn btn-primary" type="submit">
                Nova igra
            </button>
        </form>
    </div>

    <div class="row">
        % for game in games:
            <div class="col-sm-12 col-md-4 px-md-1 pb-2">
                <div class="card p-3">
                    % include("_matrix.tpl", game=game)
                    <div class="d-flex justify-content-between mt-3">
                        <span>{{game.state.progress()}} / 81</span>
                        % if game.state.solved():
                            <a class="btn btn-light disabled">
                                Rešeno
                            </a>
                        % else:
                            <a href="/igre/{{game.id}}"
                                class="btn btn-light">
                                Nadaljuj
                            </a>
                        % end
                    </div>
                </div>
            </div>
        % end
    </div>

</div>